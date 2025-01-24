from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    from views import contacts, leads, pipelines
    app.register_blueprint(contacts.bp)
    app.register_blueprint(leads.bp)
    app.register_blueprint(pipelines.bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
