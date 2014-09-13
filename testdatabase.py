from app import db, models 
u = models.User(nickname='john', email='john@email.com', role=models.ROLE_USER)
db.session.add(u)
db.session.commit()

u = models.User(nickname='susan', email='susan@email.com', role=models.ROLE_USER)
db.session.add(u)
db.session.commit()
