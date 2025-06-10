# app/models/admin.py

from app.main import db
from werkzeug.security import generate_password_hash, check_password_hash

def does_username_exist(username):
    return AdminUser.query.filter_by(username=username).first() is not None

def is_user(username):
    return does_username_exist(username)

class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)  # Optional email field
    first_name = db.Column(db.String(50), nullable=True)  # Optional first name
    last_name = db.Column(db.String(50), nullable=True)  # Optional last name
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    is_system_admin = db.Column(db.Boolean, default=False, nullable=False) # Indicates if this is a system admin user - do not allow deletion

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AppSetting(db.Model):
    __tablename__ = 'app_settings'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<AppSettings {self.key}: {self.value}>"