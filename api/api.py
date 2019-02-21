from flask import Flask, abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import models
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)


class CreatePost(Resource):
	def post(self):
		title = request.json['title']
		content = request.json['content']
		newPost = models.Post(title,content)
		db.session.add(newPost)
		db.session.commit()
		return 1

class GetPosts(Resource):
	def post(self):
		allPosts = models.Post.query.all()
		res = []
		for p in allPosts:
			res.append({
				'id': p.id,
				'title': p.title,
				'content': p.content,
				'date': p.date
			})
		return res

api.add_resource(CreatePost,'/create')
api.add_resource(GetPosts,'/get')

if __name__ == '__main__':
		app.run(port=4999)