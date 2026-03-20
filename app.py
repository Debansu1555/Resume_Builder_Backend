from flask import Flask
from config import Config
from models import db
from routes.resume_routes import resume_bp
from flask_mail import Mail
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Enable CORS (for React frontend)
CORS(app)

# Initialize database
db.init_app(app)

# Initialize Mail
mail = Mail(app)

# Register Blueprint
app.register_blueprint(resume_bp, url_prefix="/api")

# Create tables automatically
with app.app_context():
    db.create_all()

# Default route (for testing)
@app.route("/", methods=["GET"])
def home():
    return "Resume Builder Backend Running 🚀"

# Run server
if __name__ == "__main__":
    app.run(debug=True)