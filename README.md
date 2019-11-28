# heroku-github-integration

## Heroku's continuous delivery workflow

The main idea of this repository is to try out Heroku's continuous delivery workflow, connecting a Heroku *pipeline* (https://devcenter.heroku.com/articles/pipelines) to this GitHub repository. The pipeline always contains the following:

- A public facing webpage (/Heroku app): https://funky-github-productionapp.herokuapp.com/
- A *staging app*, representing the project's master development branch. At any time, the state of the staging app can be promoted to the public facing *production app*: https://funky-github-stagingapp.herokuapp.com/

Furthermore, by enabling *review apps* at Heroku (https://devcenter.heroku.com/articles/review-apps-new), pull requests into the master branch can be reviewed in a temporary *review app* before being integrated into the master branch/staging app. To this end, a second (local) git branch (named *develop*), was used to push code to GitHub, after which the GitHub GUI was used to create pull requests into the master branch. (The *develop* branch is currently deleted from the repository.)

This excellent tutorial was used for guidance: 
- *Continuous Delivery with Heroku and GitHub*, https://www.youtube.com/watch?v=_tiecDrW6yY


## Hosting a Flask app using Heroku and Heroku Add-ons

To gain familiarity with Heroku hosting, including its *Config Vars* and *Add-ons*, a small Flask app was created and configured appropriately. The app connects to a PostgreSQL database provided by the *Heroku Postgres Add-on* service, https://elements.heroku.com/addons/heroku-postgresql. When enabling this add-on (On the *Resource* page of the app in the Heroku dashboard), the *Config Var* `DATABASE_URL` is set automatically.

In order to use *SQLAlchemy* with the Flask app, the app is configured by setting `SQLALCHEMY_DATABASE_URI` in `app.config[]`. "*Config Vars* are exposed to your app’s code as environment variables" (https://devcenter.heroku.com/articles/config-vars), so `DATABASE_URL` is retrieved as:

```SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')```


The youtube channel *Traversy Media* contains many tutorials on the topic of Flask, including database integration. The code in this repository is inspired by the following highly recommended tutorials:
1. *Python Flask From Scratch (5 parts)*, https://www.youtube.com/watch?v=zRwy8gtgJ1A
2. *REST API With Flask & SQL Alchemy*, https://www.youtube.com/watch?v=PTZiDnuC86g
3. *Build & Deploy A Python Web App | Flask, Postgres & Heroku*, https://www.youtube.com/watch?v=w25ea_I89iM


## About the Flask app

The app runs a webpage where it is possible to make posts about your favorite food recipes! There is a simple login functionality in place, such that only logged in users are allowed to make posts. The data about users and recipes are are stored and fetched from a PostgreSQL database, either run locally or on Heroku (specified by `env` in config.py).


### Setting up the database

Video (3.) in the previous section shows the steps to set up the database both locally as well as on Heroku. In short:

1. Go to pgadmin and under *Databases*, create a database named *flask_recipe_page* (which matches the database name specified in config.py as part of the `SQLALCHEMY_DATABASE_URI` path). No such step is necessary for Postgres on Heroku.


2. Enter a python shell (from the folder that contains app.py) and run: 

```
>>> from app import db
>>> db.create_all()
```

To access a python shell inside the Heroku app, run in a local terminal: `heroku run python -a funky-github-stagingapp`


### To do: Some features that could be nice to implement

- Improve the form-functionality for user registration and posting recipes. E.g. *wtforms* provides nice functionality for form validation, password confirmation, etc.
- Add user control, such that a logged in user only can edit/delete one's own articles (e.g. using *flask-login*, https://hackersandslackers.com/authenticating-users-with-flask-login/).
- Use *gunicorn* instead of the internal Flask server, https://devcenter.heroku.com/articles/python-gunicorn. Make sure it's installed (add gunicorn and suitable version to requirements.txt) and insert *web: gunicorn app:app* (*web: gunicorn <name_of_python_file>:<name_of_app_to_run>*) into the Procfile. 
- Separate app.py into \_\_init__.py (initialize app and database in here) and routes.py, place in a package (a folder) and run (app.run()) it from a run.py outside of the folder.


