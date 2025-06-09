# app/models/page.py
from app.main import db

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    section_assignments = db.relationship(
        'SectionAssignment',
        back_populates='page',
        cascade='all, delete-orphan',
        lazy=True
    )

    page_assignments = db.relationship(
        'PageAssignment',
        back_populates='page',
        cascade='all, delete-orphan',
        lazy=True
    )

class SectionAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    order = db.Column(db.Integer, default=0)

    page = db.relationship('Page', back_populates='section_assignments')
    section = db.relationship('Section', back_populates='section_assignments')
