from flask import Flask, render_template, request, redirect, url_for, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def index():
    items = db.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'image_url': request.form['image_url'],
        'category': request.form['category'],
        'month': request.form['month'],
        'progress': int(request.form['progress'])
    }
    db.insert(data)
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    db.remove(doc_ids=[item_id])
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['POST'])
def edit(item_id):
    db.update({
        'title': request.form['title'],
        'description': request.form['description'],
        'image_url': request.form['image_url'],
        'category': request.form['category'],
        'month': request.form['month'],
        'progress': int(request.form['progress'])
    }, doc_ids=[item_id])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
