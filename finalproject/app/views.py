from flask import Flask, flash, redirect,render_template
from app import app, db, models
from .forms import LoginForm, CreateUserandAOE
import pdb



@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

    # option: views handles info in URL, spits out information, redirect to a new webpage 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

# % imported LoginForm class, made a LoginForm object, and sent it to the template
# validate_on_submit does all form processing for you 
# the flash method helps display info on the next page a user encounters. however it 
#   doesn't appear immediately, you need to tell the template to display this new information

# v anytime a user enters blah.com/createuser, it will run this function
@app.route('/createuser', methods=['GET','POST'])
def createuser():
    form = CreateUserandAOE()
    if form.validate_on_submit():
      print ('Form validated!') # parenthese forces evaluation of the string
      newuser = models.User() 
      newaoe = models.AOE()

      #pdb.set_trace()
      newuser.username = form.username.data
      newuser.email = form.email.data
      newuser.profile = form.profile.data

      newaoe.username = form.username.data
      newaoe.state = form.state.data
      newaoe.city = form.city.data
      newaoe.activity = form.activity.data

      db.session.add(newuser)
      db.session.add(newaoe)
      db.session.commit()
      flash('Registration successful')
      return redirect('/createuser')
    print ('Form not validated.')
    return render_template('createuser.html',
                            form=form)

