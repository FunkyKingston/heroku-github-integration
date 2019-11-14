from flask_sqlalchemy import SQLAlchemy

# When not passing an app as input argument, db = SQLAlchemy(app), it is necessary to use 
# a flask "app context" to bind the SQLAlchemy object to the application (done here in appy.py)
# - https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
# - https://flask.palletsprojects.com/en/1.1.x/appcontext/
db = SQLAlchemy() 

print('running dbmanagement.py')

class Articles(db.Model):
  __tablename__ = 'articles'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  body = db.Column(db.Text())
  category = db.Column(db.String(50))

  def __init__(self, title, body, category):
    self.title = title
    self.body = body
    self.category = category