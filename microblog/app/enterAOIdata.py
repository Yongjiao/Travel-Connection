
from app import db,models
from datetime import datetime

user1 = models.User.id(1)
user2 = models.User.get(2)
user3 = models.User.get(3)
user4 = models.User.get(4)
user5 = models.User.get(5)

a=models.AreaOfInterests(user_id=1, country='US', state='TX', city='Houston',area='Drinking')
db.session.add(a)
db.session.commit()
b=models.AreaOfInterests(user_id=2,country='US', state='NY', city='New York City',area='Fine Dining')
db.session.add(b)
db.session.commit()
c=models.AreaOfInterests(user_id=3,country='US', state='CA', city='San Francisco',area='Museums')
db.session.add(c)
db.session.commit()
d=models.AreaOfInterests(user_id=4,country='US', state='TX', city='Houston',area='Drinking')
db.session.add(d)
db.session.commit()
e=models.AreaOfInterests(user_id=5,country='US', state='WA', city='Seattle',area='Coffee')
db.session.add(e)
db.session.commit()




AOI = models.AreaOfInterests.query.all()
print (AOI)
