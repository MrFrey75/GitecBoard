# app/main.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import re
from markdown import markdown as md_lib

# Initialize SQLAlchemy (used later with app context)
db = SQLAlchemy()

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # -------------------------------------------
    # Configuration Section
    # -------------------------------------------

    # Define the base directory (this file's location)
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Define the full path to the SQLite DB
    db_path = os.path.join(basedir, '../data/infoboard.db')

    # Set SQLAlchemy config
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'  # SQLite file path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking (improves performance)

    # Set Flask secret key (used for sessions, cookies, etc.)
    app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")

    # -------------------------------------------
    # Extensions Initialization
    # -------------------------------------------

    # Bind SQLAlchemy to the Flask app
    db.init_app(app)

    # -------------------------------------------
    # Blueprint Registration
    # -------------------------------------------

    # Import and register route blueprints
    try:
        from app.routes.display import bp as display_bp
        app.register_blueprint(display_bp)
    except ImportError:
        pass  # Fail silently if the blueprint isn't available yet

    try:
        from app.routes.admin import bp as admin_bp
        app.register_blueprint(admin_bp)
    except ImportError:
        pass

    # -------------------------------------------
    # Database Setup
    # -------------------------------------------

    # Import models and create database tables
    with app.app_context():
        from app.models import board, page, section, admin
        db.create_all()

    # -------------------------------------------
    # Template Filters
    # -------------------------------------------

    # Custom Jinja filter to render Markdown to HTML
    @app.template_filter('markdown')
    def render_markdown(text):
        return md_lib(text, output_format="html5")

    # Custom Jinja filter to extract YouTube video ID from URL
    @app.template_filter('youtube_id')
    def extract_youtube_id(url):
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
        return match.group(1) if match else url

    CORS(app)  # allow all for now; restrict in prod!

    return app
