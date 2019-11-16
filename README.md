# heroku-github-integration

## Heroku's continuous delivery workflow

The main idea of this repository is to try out Heroku's continuous delivery workflow, connecting a Heroku *pipeline* (https://devcenter.heroku.com/articles/pipelines) to this GitHub repository and enabling *review apps* (https://devcenter.heroku.com/articles/review-apps-new) to review code changes in apps separate from the public-facing production app. To this end, the following excellent tutorial was used for guidance:
- *Continuous Delivery with Heroku and GitHub*, https://www.youtube.com/watch?v=_tiecDrW6yY

To try out review apps, a second (local) git branch (e.g. named *develop*), was used to push code to GitHub and create pull requests into the master branch on GitHub using its GUI. This second branch is currently deleted from the repository.


## Hosting a Flask app using Heroku and Heroku Add-ons

In addition, in order to showcase some additional Heroku configuration steps, this repository contains a small Flask app, connected to a PostgreSQL database provided by the *Heroku Postgres Add-on* service, https://elements.heroku.com/addons/heroku-postgresql. For example, this means that we need to play around with Heroku *Config Vars*, https://devcenter.heroku.com/articles/config-vars.


The youtube channel *Traversy Media* contains many tutorials on the topic of Flask, including database integration. The code in this repository is sort of a mixture of code from the following highly recommended tutorials:
- *Python Flask From Scratch (5 parts)*, https://www.youtube.com/watch?v=zRwy8gtgJ1A
- *REST API With Flask & SQL Alchemy*, https://www.youtube.com/watch?v=PTZiDnuC86g
- *Build & Deploy A Python Web App | Flask, Postgres & Heroku*, https://www.youtube.com/watch?v=w25ea_I89iM


## Expanding on the Flask app

...


### To do: Features to implement

- Use *gunicorn* instead of the internal Flask server
- Add password encryption (e.g. using *sha256_crypt* from *passlib.hash*)
- Use *wtforms* instead of standard forms
- Freshen up the design of the page (adapt the current use of bootstrap, add some css, logo pictures, ...)
- Add user control, such that a logged in user only can edit/delete one's own articles (e.g. with *Flask-Login*, https://hackersandslackers.com/authenticating-users-with-flask-login/)
- Separate app.py into \_\_init__.py (initialize app and database in here) and routes.py, place in a package (a folder) and run (app.run()) it from a run.py outside of the folder


