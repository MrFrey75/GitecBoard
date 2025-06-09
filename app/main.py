# app/main.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Safe and portable SQLite database path
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '../data/infoboard.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)

    # Register blueprints
    try:
        from app.routes.display import bp as display_bp
        app.register_blueprint(display_bp)
    except ImportError:
        pass  # Display route doesn't exist yet

    # Create tables if they don't exist
    with app.app_context():
        from app.models import board, page, section
        db.create_all()

    # Add custom Jinja filters
    from markdown import markdown as md_lib
    import re

    @app.template_filter('markdown')
    def render_markdown(text):
        return md_lib(text, output_format='html5')

    @app.template_filter('youtube_id')
    def extract_youtube_id(url):
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
        return match.group(1) if match else url

    return app
