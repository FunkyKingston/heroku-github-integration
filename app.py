from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy

# from .dbmanagement.. (relative path) only works from __init__.py (?)
from dbmanagement import db, Articles

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
  app.debug = True
  app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
  app.debug = False
  app.config['SQLALCHEMY_DATABASE_URI'] = ''

#db = SQLAlchemy(app) # db = SQLAlchemy() created in dbmanagement.py
db.init_app(app)


# Home
@app.route('/')
def home():
  #return 'Hello World from Heroku, integrated with GitHub!'
  return render_template('home.html', var=__name__)


# About
@app.route('/about')
def about():
    return render_template('about.html')
	

# Articles
@app.route('/articles')
def articles():
    return render_template('articles.html')
	
	
# when ran on heroku, __name__ is set to "web", since if this file is being imported from another module, __name__ isset to that module’s name.
if __name__ == '__main__':
  app.run(debug=True)

# Question: Is it necessary to include app.run()? 
# Answer: The run-command runs flask's internal web-server so the app can be tested locally. If however Apache, NGINX or some other web server loads your app it runs directly on the server

# The below command will run the app (in web.py) using a Heroku 'web' dyno
# web: FLASK_APP=web.py python -m flask run --host=0.0.0.0 --port=$PORT
