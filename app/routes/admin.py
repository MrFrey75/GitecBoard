# app/routes/admin.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.board import Board

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
def dashboard():
    boards = Board.query.all()
    return render_template("admin/dashboard.html", boards=boards)

@admin_bp.route("/boards/create", methods=["GET", "POST"])
def create_board():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        identifier = request.form.get("identifier", "").strip()

        if not name or not identifier:
            flash("Both name and identifier are required.", "danger")
            return redirect(url_for("admin.create_board"))

        board = Board(name=name, identifier=identifier)
        db.session.add(board)
        db.session.commit()
        flash("Board created successfully!", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/create_board.html")

@admin_bp.route("/boards/<int:board_id>/edit")
def edit_board(board_id):
    board = Board.query.get_or_404(board_id)
    return render_template("admin/edit_board.html", board=board)
