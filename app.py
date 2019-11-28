# Standard library imports
import os
# Third party imports
from flask import Flask, render_template, request, redirect, url_for, session, flash
from passlib.hash import sha256_crypt

# flask-login, https://hackersandslackers.com/authenticating-users-with-flask-login/
# also see: Corey Schafer: "Python Flask Tutorial: Full-Featured Web App Part 6 - User Authentication", https://www.youtube.com/watch?v=CSHx6eCkmv0

# Local application imports
from dbmanagement import db, Recipe, User #import dbmanagement # -> would need to use (namespace) dbmanagement.db, etc.


app = Flask(__name__)
config_file = 'config.py'
app.config.from_pyfile(config_file) # (runs config.py) option to configuring in this file using e.g. app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# - example of instead using app.config.from_envvar(), https://www.youtube.com/watch?v=7RWro4VF_9c

app.app_context().push() # Introduction into Contexts https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
db.init_app(app) 
# --- Create the database & tables ---
# Locally: 
# - in pgadmin (PostgreSQL's admin GUI)!, create a database with the name "flask_recipe_page", matching what's specified in config.py
# - run python in a terminal and >>> from app import db >>> db.create_all() 
#   - this creates the tables, that can now be seen e.g. in pgadmin
# On Heroku: 
# - 
# - go to the dashboard->More->Run console, type in python and you get a terminal!
#   (or use Heroku's CLI, by running "heroku run python" in a local terminal)




posts = [
  {
    'author': 'Tomas',
    'name': 'Kristina\'s Muesli',
    'description': 'Add fresh fruit/berries and yoghurt!',
    'body': 'Oats, Nuts, Coconut flakes, ...',
    'date_posted': 'November 26, 2019'
  },
  {
    'author': 'Kempe',
    'name': 'Kalle\'s Jambalaya',
    'description': 'Open up a bottle of hungarian "finvin"',
    'body': 'Lots of veggies and love, some wine for the chef',
    'date_posted': 'November 27, 2019'  
  },
  {
    'author': 'Kempe',
    'name': 'Kalle\'s Floor-Marinated Macaroni',
    'description': 'The 3 second rule does not apply',
    'body': 'Fast macaroni. Use water tower floor for best result',
    'date_posted': 'October 10, 2007'
  }
]


# Home
@app.route('/')
def home():
  #return 'Hello World from Heroku, integrated with GitHub!'
  return render_template('home.html', var=__name__)


# About
@app.route('/about')
def about():
  return render_template('about.html')
	

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST': # ...and form.validate(), ish
    username = request.form['username']
    email = request.form['email']
    if username == '' or request.form['password'] == '':
      return render_template('register.html', message='Please enter required fields') # any (easy) way to add the message without re-rendering the page?
    password = sha256_crypt.hash( request.form['password'] )
    
    # Entry1: MamaJamaica / mama@kingstontown.jm / 123456
    # to delete entry using SQL Query in pgadmin: DELETE FROM public."user" WHERE username = 'MamaJamaica';
    user = User(username, email, password) # <- works for Traversy Media in https://www.youtube.com/watch?v=w25ea_I89iM, I guess because he writes his own constructor __init__(), but he only has one table so not sure how this approach will handle db.ForeignKey(), db.relationship()
    # print(user)
    db.session.add(user) # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
    db.session.commit()
    #flash('You are now registered and can log in', 'success') # 'success' is a message category
    return redirect(url_for('login'))

  return render_template('register.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
  
  if request.method == 'POST':
    username = request.form['username']
    #password_candidate = sha256_crypt.hash( request.form['password'] )
    password_candidate = request.form['password'] # password candidate shouldn't be hashed, sha256_crypt.verify() handles that
    user = User.query.filter_by(username=username).first()
    # - or? user = db.session.query(User).filter(User.username==username).first()
    #print(user)
    if not user or not sha256_crypt.verify(password_candidate, user.password):
      print('Login failed')
      return render_template('login.html', message='Login failed')
      #Add? return render_template('login.html', message=error_message)
    else: # everything ok
      print('Login succeeded')
      #login_user(user) # from flask_login, don't use for now...
      session['logged_in'] = True
      session['username'] = username
      return redirect(url_for('recipes'))
      
  #if session['logged_in'] == True:
  #  return redirect(url_for('dashboard'))

  return render_template('login.html')
  

# Logout
@app.route('/logout')
def logout():
  session.clear()
  #flash('You are now logged out', 'success') # from flask import flash - haven't added this to base layout.html or elsewhere at this point...
  return redirect(url_for('login'))

  
# Dashboard
@app.route('/dashboard')
def dashboard():
  #posts = Recipe.query.all() # add sorting by newest post to query
  
  # fetch only recipes by logged in user...
  # TO DO: add "@is_logged_in"-lock to routes with recipe ids corresponding to other users
  current_user = User.query.filter_by(username=session['username']).first()
  posts = current_user.authored_recipes
  return render_template('dashboard.html', posts=posts)


# Recipes
@app.route('/recipes')
def recipes():
  posts = Recipe.query.all() # add sorting by newest post to query
  #print(posts[0].author.username)
  #type(posts[0].pub_date): <class 'datetime.datetime'>
  # - t = posts[0].pub_date has t.day, t.month, t.year, t.hour, etc.!
  return render_template('recipes.html', posts=posts)


# Add Recipe
@app.route('/add_recipe', methods=['GET','POST'])
def add_recipe():
  if request.method == 'POST':

    name = request.form['name']
    description = request.form['description']
    body = request.form['name']
    category = request.form['category'] 
    user_id = ''

    # "@is_logged_in" checkwill be made (once the functionality 
    # is added) upon trying to access the /add_recipe route
    #if session['logged_in'] == True:
      
    current_user = User.query.filter_by(username=session['username']).first()
    if user:
      user_id = current_user.id
      recipe = Recipe(name, description, body, category, user_id)
      print(recipe)
      # recipe.save() # does this also work? anyway, one advantage of add, commit - can commit multiple changes simultaneously
      db.session.add(recipe) # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
      db.session.commit()
      return redirect(url_for('recipes'))

    #else:
    #  print('user_id missing') # shouldn't occur once @is_logged_in-check is added to the route

  return render_template('add_recipe.html')


# Edit Recipe
#@app.route('/edit_recipe/<string:id>', methods=['GET','POST'])
#def edit_recipe(id):
#  return redirect(url_for('dashboard'))

# Delete Recipe
#@app.route('/delete_recipe/<string:id>', methods=['GET','POST'])
#def delete_recipe(id):
  # to do: cur.execute("DELETE FROM recipe WHERE id = ?", (id,)) <- nja detta är utan SQLAlchemy med en cur = conn.cursor(...) från sqlite3 package
  # - nåt i stil med db.session.delete... , motsvarnade db.session.add(data) där data = Recipe(,,,)
#  return redirect(url_for('dashboard'))


# when ran on heroku, __name__ is set to "web", since if this file is being imported from another module, __name__ isset to that module’s name.
if __name__ == '__main__':
  app.run(debug=True)


# change from flask's internal web server, use gunicorn 
# (which is a wsgi, web server gateway interface):
# add gunicorn to requirements.txt, pip install it in the env locally and use the same version!
# change the Procfile to, "web: gunicorn app:app"
# - also, in a file runtime.txt, add "python-3.7.3" (https://devcenter.heroku.com/articles/python-runtimes)


# Question: Is it necessary to include app.run()? 
# Answer: The run-command runs flask's internal web-server so the app can be tested locally. If however Apache, NGINX or some other web server loads your app it runs directly on the server

# The below command will run the app (in web.py) using a Heroku 'web' dyno
# web: FLASK_APP=web.py python -m flask run --host=0.0.0.0 --port=$PORT
