from api import db
from datetime import datetime

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	date = db.Column(db.Text, nullable=False, default=datetime.now().strftime("%d-%m-%Y %H:%M"))

	def __init__(self, title, content):
		self.title = title
		self.content = content

	def __repr__(self):
		return '<Titulo {self.title} \nContenido {self.content}>'