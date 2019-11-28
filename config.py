import os 

print('running config.py')

#env = 'dev'
env = 'heroku'

if env == 'dev':
  # 'postgresql://<username>:<password>@<uri>/<name of database>'
  SQLALCHEMY_DATABASE_URI = 'postgresql://funkykingston:123456@localhost/flask_recipe_page' 
  # make sure to create the database first, e.g. (local case) create a database named 'flask_recipe_page' in pgadmin
else:
#elif env == 'heroku':
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SECRET_KEY = os.environ.get('SECRET KEY') # not in use with the current Heroku hosted postgres database, would use e.g. for standalone mongodb atlas
#else:
  # to do: handle this case

SQLALCHEMY_TRACK_MODIFICATIONS = False
