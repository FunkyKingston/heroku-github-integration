import os 

print('running config.py')

if os.environ.get('ENV') == 'dev':
  env = 'dev'
else: # os.environ['ENV'] is (set in app.py to) 'prod'
  env = 'heroku'


if env == 'dev':
  # ran as Query in the articles database in pgadmin: ALTER USER postgres WITH PASSWORD '123456';
  # 'postgresql://<username>:<password>@<uri>/<name of database>'
  SQLALCHEMY_DATABASE_URI = 'postgresql://funkykingston:123456@localhost/blog' 
elif env == 'heroku':
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SECRET_KEY = os.environ.get('SECRET KEY')
#else
  # to do: handle this case

SQLALCHEMY_TRACK_MODIFICATIONS = False
