from todoapp import create_app, db

app = create_app()

@app.shell_context_processor
# For debugging
def create_context():
    return dict(db=db)

app.run(debug=True)