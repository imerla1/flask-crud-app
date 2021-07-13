from flask import render_template, url_for, redirect, Blueprint, request, jsonify, json
from todoapp.models import Todo
from todoapp import db

main = Blueprint("main", __name__)

# Delete, update

@main.route("/", methods=["GET", "POST"])
@main.route("/index")
def index():
    t = Todo.query.all()
    return render_template('index.html', data=t)


@main.route("/add/<string:content>", methods=["POST", "GET"])
def add(content):
    cnt = str(content)
    t = Todo(data=cnt)
    db.session.add(t)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('main.index'))
    except:
        return 'Error'

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.data = request.form['content']

        try:
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            return 'Error'

    else:
        return render_template('update.html', task=task)


@main.route('/finished/<int:id>', methods=['GET', 'POST'])
def finished(id):
    task = Todo.query.get_or_404(id)

    try:
        task.finished = True
        
        db.session.commit()
        return redirect(url_for('main.index'))
    except:
        return "Error"

    