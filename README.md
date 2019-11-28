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
- *Python Flask From Scratch (5 parts)*, https://www.youtube.com/watch?v=zRwy8gtgJ1A
- *REST API With Flask & SQL Alchemy*, https://www.youtube.com/watch?v=PTZiDnuC86g
- *Build & Deploy A Python Web App | Flask, Postgres & Heroku*, https://www.youtube.com/watch?v=w25ea_I89iM


## About the Flask app

...

### Setting up the database

...

### To do: Some features that could be nice to implement

- Use *gunicorn* instead of the internal Flask server, https://devcenter.heroku.com/articles/python-gunicorn
- Separate app.py into \_\_init__.py (initialize app and database in here) and routes.py, place in a package (a folder) and run (app.run()) it from a run.py outside of the folder
- Add user control, such that a logged in user only can edit/delete one's own articles (e.g. with *Flask-Login*, https://hackersandslackers.com/authenticating-users-with-flask-login/)


