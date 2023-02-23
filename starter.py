# Keeping shell context out of application
from starter import create_app, db
from starter.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
