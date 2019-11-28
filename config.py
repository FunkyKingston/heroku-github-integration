import os 

print('running config.py')

#env = 'dev'
env = 'heroku'

if env == 'dev':
  # 'postgresql://<username>:<password>@<uri>/<name of database>'
  SQLALCHEMY_DATABASE_URI = 'postgresql://funkykingston:123456@localhost/flask_recipe_page' 
  # - for the local case, make sure to create the database first, 
  #   i.e. create a database named 'flask_recipe_page' in pgadmin
  SECRET_KEY = 'secret123' # necessary for using flask 'session'. not too worried about displaying this secret_key ...
else: # elif env == 'heroku':
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SECRET_KEY = os.environ.get('SECRET_KEY') # necessary for using flask 'session'. 



SQLALCHEMY_TRACK_MODIFICATIONS = False
