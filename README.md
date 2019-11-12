# heroku-github-integration


The initial idea of this repository is to try out Heroku's continuous delivery workflow, connecting a Heroku *pipeline* (https://devcenter.heroku.com/articles/pipelines) to this GitHub repository and enabling *review apps* (https://devcenter.heroku.com/articles/review-apps-new) to review code changes in apps separate from the production app. To this end, the following excellent tutorial was followed:
- *Continuous Delivery with Heroku and GitHub*, https://www.youtube.com/watch?v=_tiecDrW6yY


In addition, in order to showcase some additional Heroku configuration steps, this repository contains a small Flask app, connected to a PostgreSQL database provided by the *Heroku Postgres Add-on* service, https://elements.heroku.com/addons/heroku-postgresql. For example, this means that we need to play around with Heroku *Config Vars*, https://devcenter.heroku.com/articles/config-vars.


The youtube channel *Traversy Media* contains many tutorials on the topic of Flask, including database integration. The code in this repository is sort of a mixture of code from the following highly recommended tutorials:
- *Python Flask From Scratch (5 parts)*, https://www.youtube.com/watch?v=zRwy8gtgJ1A
- *REST API With Flask & SQL Alchemy*, https://www.youtube.com/watch?v=PTZiDnuC86g
- *Build & Deploy A Python Web App | Flask, Postgres & Heroku*, https://www.youtube.com/watch?v=w25ea_I89iM
