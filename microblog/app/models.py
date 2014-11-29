from hashlib import md5
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index=True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    firstname = db.Column(db.String(32), index=True, nullable=True)
    lastname = db.Column(db.String(32), index=True, nullable = True)
    phone = db.Column(db.String(32), nullable=True)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(300))
    last_seen = db.Column(db.DateTime)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
    
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname

    def __repr__(self):
        return '<User %r %r %r %r %r %r %r>' % (self.id, self.nickname, self.email, self.firstname, self.lastname, self.phone, self.about_me)    
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class AreaOfInterests(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    country = db.Column(db.String(64))
    state = db.Column(db.String(64))
    city = db.Column(db.String(64))
    area = db.Column(db.String(120), nullable=True)
    #area is things like fishing, retaurant, hiking, etc.
    
    def __repr__(self):
        return '<AreaOfInterests %r %r %r %r %r %r>' % (self.id, self.user_id, self.country, self.state, self.city, self.area)

class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rater_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    rated_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    rates = db.Column(db.Float, nullable = False)
    comment = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime)

    rater = db.relationship('User', foreign_keys = 'Ratings.rater_id')
    rated = db.relationship('User', foreign_keys = 'Ratings.rated_id')

    def __repr__(self):
        return '<Ratings %r %r %r %r %r %r>' % (self.id, self.rater_id, self.rated_id, self.rates, self.comment, self.timestamp)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    text = db.Column(db.Text, nullable = False)
    time = db.Column(db.DateTime)
    
    sender = db.relationship('User', foreign_keys = 'Messages.sender_id')
    receiver = db.relationship('User', foreign_keys = 'Messages.receiver_id')

    def __repr__(self):
        return '<Messages %r %r>' % (self.id, self.sender_id, self.receiver_id, self.text, self.time)
