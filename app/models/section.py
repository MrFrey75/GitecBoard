# app/models/section.py

from app.main import db

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    content = db.Column(db.Text)
    meta = db.Column(db.String(100), nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    section_assignments = db.relationship('SectionAssignment', back_populates='section', cascade='all, delete-orphan')


class SectionAssignment(db.Model):
    __tablename__ = 'section_assignment'
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    order = db.Column(db.Integer, default=0)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    section = db.relationship('Section', back_populates='section_assignments')
    page = db.relationship('Page', back_populates='section_assignments')

class MediaAsset(db.Model):
    __tablename__ = 'media_asset'
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    media_type = db.Column(db.Enum('image', 'video', name='media_type_enum'), nullable=False)