from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid, models
from forms import LoginForm, EditForm, RatingsForm, MessagesForm
from models import User
from datetime import datetime

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
    
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        nickname = User.make_unique_nickname(nickname)
        user = User(nickname = nickname, email = resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/user/<nickname>', methods = ['GET', 'POST'])
@login_required
def user(nickname):
    user = User.query.filter_by(nickname = nickname).first()
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    # posts = [
    #     { 'author': user, 'body': 'Test post #1' },
    #     { 'author': user, 'body': 'Test post #2' }
    # ]
    comments = user.get_comments().all()
    useraoi = user.get_aoi()
    #rating other users
    form = RatingsForm()
    if form.validate_on_submit():
        rating = models.Ratings(rater_id = g.user.id,
            rated_id = user.id,
            comment = form.comment.data, 
            rates= form.rates.data,
            timestamp = datetime.now())
        db.session.add(rating)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('user', nickname=nickname))
    return render_template('user.html',
        user = user,
        comments = comments,  
        useraoi = useraoi,
        form = form,
        nickname = nickname)

@app.route('/edit', methods = ['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    guseraoi=g.user.get_aoi()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.firstname = form.firstname.data
        g.user.lastname = form.lastname.data
        g.user.phone = form.phone.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        guseraoi.country=form.country.data
        guseraoi.state=form.state.data
        guseraoi.city=form.city.data
        guseraoi.area=form.area.data
        db.session.add(guseraoi)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
        form.firstname.data = g.user.firstname
        form.lastname.data = g.user.lastname
        form.phone.data = g.user.phone
        form.country.data = guseraoi.country
        form.state.data = guseraoi.state
        form.city.data = guseraoi.city
        form.area.data = guseraoi.area
    return render_template('edit.html',
        form = form)

@app.route('/message/<nickname>', methods = ['GET', 'POST'])
@login_required
def sendMessage(nickname):
    #if browse his or her own profile
    if g.user.nickname == nickname:
        user = g.user
        messages = user.get_guser_messages().all()
        return render_template('gusermessage.html',
            messages = messages)
    else: 
    #if browse other's profile    
        user = User.query.filter_by(nickname = nickname).first()
        if user == None:
            flash('User ' + nickname + ' not found.')
            return redirect(url_for('index'))
        messages = user.get_user_messages(g.user).all()
        form = MessagesForm()
        if form.validate_on_submit():
            message = models.Messages(sender_id = g.user.id,
                receiver_id = user.id,
                text = form.text.data, 
                time = datetime.now())
            db.session.add(message)
            db.session.commit()
            flash('Your message is sending!')
            return redirect(url_for('user', nickname=nickname))
        return render_template('message.html',
            form = form,
            messages = messages)


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500  
    
