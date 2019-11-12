from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#db = SQLAlchemy(app)


class Articles(db.Model):
  __tablename__ = 'articles'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  body = db.Column(db.Text())
  category = db.Column(db.String(50))