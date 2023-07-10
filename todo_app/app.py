from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kullanici_adi:sifre@localhost/todoapp'
db = SQLAlchemy(app)

#ToDo modeli
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Todo %r>' % self.title
    
#Ana Sayfa
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

#Todo Ekleme
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect('/')

#Todo Güncelleme
@app.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    todo = Todo.query.get(todo_id)
    todo.title = request.form['title']
    db.session.commit()
    return redirect('/')

@app.route('/add', methods=["POST"])
def add():
    title = request.form['title']
    reminder_str = request.form['reminder']
    reminder = datetime.strptime(reminder_str, '%Y-%m-%dT%H:%M')
    new_todo = Todo(title=title, reminder=reminder)
    db.session.add(new_todo)
    db.session.commit()
    return redirect('/')
    

#Todo Bitir
@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = True
    db.session.commit()
    return redirect('/')

#Todo Silme
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)




    