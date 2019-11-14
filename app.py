# Standard library imports
import os
# Third party imports
from flask import Flask, render_template, request
# Local application imports
from dbmanagement import db, Articles
#import dbmanagement # -> would need to use (namespace) dbmanagement.db, dbmanagement.articles


app = Flask(__name__)
config_file = 'config.py'
app.config.from_pyfile(config_file) # (runs config.py) option to configuring in this file using e.g. app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# alternative, about using app.config.from_envvar(), https://www.youtube.com/watch?v=7RWro4VF_9c


print("db:", db)

# Introduction into Contexts https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
app.app_context().push()
db.init_app(app) # now, from python running in a terminal >>> from app import db >>> db.create_all() 
print("db:", db)



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
  os.environ['ENV'] = 'dev'
  app.run(debug=True)
else:
  os.environ['ENV'] = 'prod'

# Question: Is it necessary to include app.run()? 
# Answer: The run-command runs flask's internal web-server so the app can be tested locally. If however Apache, NGINX or some other web server loads your app it runs directly on the server

# The below command will run the app (in web.py) using a Heroku 'web' dyno
# web: FLASK_APP=web.py python -m flask run --host=0.0.0.0 --port=$PORT
