# app/routes/display.py

from flask import Blueprint, render_template, redirect
from app.models.board import Board
from datetime import datetime

bp = Blueprint('display', __name__, url_prefix='/')


@bp.route('/')
def index():
    # Redirect to the first available board
    board = Board.query.first()
    if board:
        return redirect(f'/{board.identifier}')
    return "No boards found", 404


@bp.route('/<identifier>')
def show_board(identifier):
    board = Board.query.filter_by(identifier=identifier).first_or_404()

    # Filter section assignments by visibility (if start_time or end_time set)
    now = datetime.now()
    for page_assignment in board.page_assignments:
        page = page_assignment.page
        visible_assignments = []
        for sa in page.section_assignments:
            section = sa.section
            if (not section.start_time or now >= section.start_time) and \
               (not section.end_time or now <= section.end_time):
                visible_assignments.append(sa)
        page.section_assignments = visible_assignments

    return render_template("board.html", board=board)
