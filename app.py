from flask import Flask
from models import db, User
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.protected import protected_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
JWTManager(app)

# Register routes
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(protected_bp, url_prefix="/protected")

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
