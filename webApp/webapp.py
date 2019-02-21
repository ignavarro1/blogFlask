from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ydh9QcKsNSCIisad98123bcbajJJHA'

header = {'Content-Type': 'application/json'} 
posts = []

@app.route('/', methods=['GET'])
def index():
	posts = requests.post('http://localhost:4999/get', headers=header).json()
	return render_template('index.html', posts=posts)

@app.route('/admin/posts/create', methods=['GET', 'POST'])
def create():
	if (request.method == "POST"):
		post = {
			'title': request.form['title'],
			'content':request.form['content']
		}
		requests.post('http://localhost:4999/create', headers=header, json=post)
		return redirect('/admin/posts/create')
	else:
		return render_template('create.html')


if __name__ == '__main__':
	app.run()