# app/models/board.py

from app.main import db

class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    slug_identifier = db.Column(db.String(100), nullable=False, unique=True)
    is_deleted = db.Column(db.Boolean, default=False)

    # Relationship to PageAssignment
    page_assignments = db.relationship(
        'PageAssignment',
        back_populates='board',
        cascade="all, delete-orphan"
    )


class PageAssignment(db.Model):
    __tablename__ = 'page_assignment'
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    order = db.Column(db.Integer, default=0)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    board = db.relationship('Board', back_populates='page_assignments')
    page = db.relationship('Page', back_populates='page_assignments')


