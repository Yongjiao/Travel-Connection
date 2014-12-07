from app import db,models
from datetime import datetime

a=models.AreaOfInterests(id=1, country='US', state='TX', city='Houston',area='Drinking')
db.session.add(a)
db.session.commit()
a=models.AreaOfInterests(id=2,country='US', state='NY', city='New York City',area='Fine Dining')
db.session.add(a)
db.session.commit()
a=models.AreaOfInterests(id=3,country='US', state='CA', city='San Francisco',area='Museums')
db.session.add(a)
db.session.commit()
a=models.AreaOfInterests(id=4,country='US', state='TX', city='Houston',area='Drinking')
db.session.add(a)
db.session.commit()
a=models.AreaOfInterests(id=5,country='US', state='WA', city='Seattle',area='Coffee')
db.session.add(a)
db.session.commit()




AOI = models.AreaOfInterests.query.all()
print AOI