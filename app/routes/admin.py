from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.main import db
from app.models.board import Board
from app.models.page import Page
from app.models.section import Section

bp = Blueprint('admin', __name__, url_prefix='/admin')

# --- BOARDS ---
@bp.route('/boards')
def boards():
    boards = Board.query.all()
    return render_template('admin/boards.html', boards=boards)

@bp.route('/boards/add', methods=['POST'])
def add_board():
    name = request.form['name']
    slug_identifier = request.form['slug_identifier']
    board = Board(name=name, slug_identifier=slug_identifier)
    db.session.add(board)
    db.session.commit()
    flash('Board added!')
    return redirect(url_for('admin.boards'))

@bp.route('/boards/<int:board_id>/edit', methods=['POST'])
def edit_board(board_id):
    board = Board.query.get_or_404(board_id)
    board.name = request.form['name']
    board.slug_identifier = request.form['slug_identifier']
    db.session.commit()
    flash('Board updated!')
    return redirect(url_for('admin.boards'))

@bp.route('/boards/<int:board_id>/delete')
def delete_board(board_id):
    board = Board.query.get_or_404(board_id)
    db.session.delete(board)
    db.session.commit()
    flash('Board deleted!')
    return redirect(url_for('admin.boards'))

# --- PAGES ---
@bp.route('/pages')
def pages():
    pages = Page.query.all()
    return render_template('admin/pages.html', pages=pages)

@bp.route('/pages/add', methods=['POST'])
def add_page():
    title = request.form['title']
    slug = request.form['slug']
    page = Page(title=title, slug=slug)
    db.session.add(page)
    db.session.commit()
    flash('Page added!')
    return redirect(url_for('admin.pages'))

@bp.route('/pages/<int:page_id>/edit', methods=['POST'])
def edit_page(page_id):
    page = Page.query.get_or_404(page_id)
    page.title = request.form['title']
    page.slug = request.form['slug']
    db.session.commit()
    flash('Page updated!')
    return redirect(url_for('admin.pages'))

@bp.route('/pages/<int:page_id>/delete')
def delete_page(page_id):
    page = Page.query.get_or_404(page_id)
    db.session.delete(page)
    db.session.commit()
    flash('Page deleted!')
    return redirect(url_for('admin.pages'))

# --- SECTIONS ---
@bp.route('/sections')
def sections():
    sections = Section.query.all()
    return render_template('admin/sections.html', sections=sections)

@bp.route('/sections/add', methods=['POST'])
def add_section():
    title = request.form['title']
    content = request.form['content']
    section = Section(title=title, content=content)
    db.session.add(section)
    db.session.commit()
    flash('Section added!')
    return redirect(url_for('admin.sections'))

@bp.route('/sections/<int:section_id>/edit', methods=['POST'])
def edit_section(section_id):
    section = Section.query.get_or_404(section_id)
    section.title = request.form['title']
    section.content = request.form['content']
    db.session.commit()
    flash('Section updated!')
    return redirect(url_for('admin.sections'))

@bp.route('/sections/<int:section_id>/delete')
def delete_section(section_id):
    section = Section.query.get_or_404(section_id)
    db.session.delete(section)
    db.session.commit()
    flash('Section deleted!')
    return redirect(url_for('admin.sections'))
