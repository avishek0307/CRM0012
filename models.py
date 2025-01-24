from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(20))

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    source = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64))

class Pipeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    stage = db.Column(db.String(64))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact', backref='pipelines')
