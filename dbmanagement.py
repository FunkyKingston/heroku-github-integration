from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

print('running dbmanagement.py')

# Code inspiration for this page from:
# - https://github.com/PrettyPrinted/youtube_video_code/tree/master/2019/07/25/Deploy%20a%20Flask%20App%20to%20Heroku%20With%20a%20Postgres%20Database%20%5B2019%5D/flask_qa


db = SQLAlchemy() # discussion of circular imports, same "issue" that I needed to handle: https://www.youtube.com/watch?v=44PvX0Yv368
# When not passing an app as input argument, db = SQLAlchemy(app), it is necessary to use 
# a flask "app context" to bind the SQLAlchemy object to the application (done here in appy.py)
# - https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
# - https://flask.palletsprojects.com/en/1.1.x/appcontext/


# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
# - class Model(object) definition: https://github.com/pallets/flask-sqlalchemy/blob/668758ac71012e272df9c7eefbfef6d472dbd642/flask_sqlalchemy/model.py
# - "all classes inherit from object" - https://docs.python.org/3/tutorial/classes.html
class Recipe(db.Model):
  __tablename__ = 'recipe'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  description = db.Column(db.Text())
  body = db.Column(db.Text())
  category = db.Column(db.String(50))
  pub_date = db.Column(db.DateTime, default=datetime.utcnow) # note, not datetime.utcnow(), we're passing in the function
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  #def __init__(self, ...) # skip and use the base class' own constructor...? in turn inherited from the default object class, SQLAlchemy: "class Model(object)"
  #def __init__(self, name, description, body, category, pub_date, user_id):
  def __init__(self, name, description, body, category, user_id):
    self.name = name
    self.description = description
    self.body = body
    self.category = category
    #self.pub_date = pub_date
    self.user_id = user_id

  def __repr__(self):
    return f"recipe with name: {self.name}, description: {self.description}, by user_id: {self.user_id}"


# Heroku PostgreSQL - Using the CLI (first $ heroku login)
# https://devcenter.heroku.com/articles/heroku-postgresql#using-the-cli
# $ heroku pg:info --app funky-github-stagingapp
# $ heroku pg:psql --app funky-github-stagingapp   <- requires that a local installation of postgres exists on your system
# funky-github-stagingapp::DATABASE=> SELECT * FROM articles;
#
# - in this video, https://www.youtube.com/watch?v=FKy21FnjKS0, also on heroku's postgres add-on, 
#   an admin user is created from a python script. Also uses a SECRET_KEY (environment variable/Heroku Config Var)

# To run the local postgres installation, $ psql -U postgres   (my local password set to '123456')
# - works after adding the bin directory of the PostgreSQL installation to the (e.g. Windows) path
#
# from postgresql terminal application ($ psql -U postgres -h localhost)
# insert into articles ( title, body, category) values ('Den bästa dagen','Den mätta dagen, den är aldrig störst. Den bästa dagen är en dag av törst. Nog finns det mål och mening i vår färd - men det är vägen, som är mödan värd','Dikter');


# one user can have multiple posts (but each post can only have one user)
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  # image_file = db.Column(db.String(30), nullable=False, default='default.jpg') # placed in static, use full path when grabbing the actual image
  password = db.Column(db.String(100), nullable=False) # 60 was too short for storing the hashed password
  authored_recipes = db.relationship('Recipe', backref='author', lazy=True)
  # - User (one) <-> Recipe (many)
  # - Due to backref='author', each recipe will have an author-property, recipe.author 

  # actually not a recommended way to declare the constructor?
  # random discussion from https://stackoverflow.com/questions/41222412/sqlalchemy-init-takes-1-positional-argument-but-2-were-given-many-to-man
  # - "...no explicitly defined __init__, it's using the _default_constructor() as constructor (unless you've overridden it), which accepts only keyword arguments in addition to self, the only positional argument."
  def __init__(self, username, email, password): 
    self.username = username
    self.email = email
    self.password = password

  def __repr__(self):
    return f"user with username: {self.username}, email: {self.email}" 