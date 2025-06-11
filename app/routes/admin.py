# app/routes/admin.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.board import Board
from app.models.page import Page
from app.models.section import Section
from app.main import db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=['GET', 'POST'])
def dashboard():
    # Handle add, edit, delete for Boards, Pages, Sections in POST if needed
    boards = Board.query.filter_by(is_deleted=False).all()
    pages = Page.query.filter_by(is_deleted=False).all()
    sections = Section.query.filter_by(is_deleted=False).all()
    return render_template('dashboard.html', boards=boards, pages=pages, sections=sections)
