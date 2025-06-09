# app/models/board.py
from app.main import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False)

    page_assignments = db.relationship(
        'PageAssignment',
        back_populates='board',
        cascade='all, delete-orphan',
        lazy=True
    )

class PageAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    order = db.Column(db.Integer, default=0)
    transition_type = db.Column(db.String(50))

    board = db.relationship('Board', back_populates='page_assignments')
    page = db.relationship('Page', back_populates='page_assignments')
