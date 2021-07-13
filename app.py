from todoapp import create_app, db
from todoapp.models import Todo
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)
@app.shell_context_processor
# For debugging
def create_context():
    return dict(db=db, todo=Todo)

app.run(debug=True)