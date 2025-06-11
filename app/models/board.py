# app/models/board.py

from app.main import db

class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the board
    title = db.Column(db.String(100), nullable=False) # Title of the board
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp()) # Timestamp for when the board was created
    slug_identifier = db.Column(db.String(100), nullable=False, unique=True) # Unique identifier for the board, used in URLs
    is_deleted = db.Column(db.Boolean, default=False) # Indicates if the board is deleted

    # Relationship to PageAssignment
    page_assignments = db.relationship(
        'PageAssignment',
        back_populates='board',
        cascade="all, delete-orphan"
    )


class PageAssignment(db.Model):
    __tablename__ = 'page_assignment'
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the page assignment
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False) # Foreign key to the board this page assignment belongs to
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False) # Foreign key to the page this assignment is for
    order = db.Column(db.Integer, default=0) # Order of the page in the board
    start_time = db.Column(db.DateTime, nullable=True) # Start time for the page assignment
    end_time = db.Column(db.DateTime, nullable=True) # End time for the page assignment

    board = db.relationship('Board', back_populates='page_assignments') # Relationship to Board
    page = db.relationship('Page', back_populates='page_assignments') # Relationship to Page


