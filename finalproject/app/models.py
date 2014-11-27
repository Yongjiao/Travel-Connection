from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    profile = db.Column(db.Text(700))
    aoes = db.relationship('AOE', backref='expertise', lazy='dynamic')

    def __repr__(self):
        return '<User %r %d %r %r>' % (self.username, self.id, self.email, self.profile)
       #tells Python how to print objects of the User class, used for debugging 


class AOE(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Integer, db.ForeignKey('user.username'))
	state = db.Column(db.String(2))
	city = db.Column(db.String(100))
	activity = db.Column(db.String(100))

	def __repr__(self):
		return '<AOI> %d %r %r %r %r>' % (self.id, self.username, self.state, self.city, self.activity)

#class Ratings(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	ratinguser = db.Column(db.Integer, db.ForeignKey('User.id'))
#	rateduser = db.Column(db.Integer, db.ForeignKey('User.id'))
#	rating = db.Column(db.Float(1))
#	comment = db.Column(db.String(500))
#	time = db.Column(db.DateTime)

#	def __repr__(self):
#		return '<Ratings> %d %d %d %r' % (self.ratinguser, self.rateduser, self.rating, self.comment)

#class Messages(db.Model):
#	mess_id = db.Column(db.Integer, primary_key=True)
#	sender = db.Column(db.Integer, db.ForeignKey('User.id'))
#	receiver = db.Column(db.Integer, db.ForeignKey('User.id'))
#	text = db.Column(db.String(5000))
#	time = db.Column(db.DateTime)

#	def __repr__(self):
#		return '<Messages> %d %d %d %r' % (self.mess_id, self.sender, self.receiver, self.text)