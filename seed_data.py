import os
from app.main import create_app, db
from app.models.board import Board, PageAssignment
from app.models.page import Page
from app.models.section import Section, SectionAssignment
from app.models.admin import AdminUser

db_path = os.path.join(os.path.dirname(__file__), "data", "infoboard.db")

# Delete the database if it exists
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"🗑️ Deleted existing database at {db_path}")

# Create fresh app and tables
app = create_app()
with app.app_context():
    db.create_all()

    # Create an admin user
    admin = AdminUser(username="admin")
    admin.set_password("admin")
    db.session.add(admin)

    # Create a board
    board = Board(name="Main Board", identifier="main")
    db.session.add(board)

    # Create a page
    page = Page(name="Welcome Page")
    db.session.add(page)
    db.session.flush()  # so page.id is available

    # Assign page to board
    pa = PageAssignment(board_id=board.id, page_id=page.id, order=0)
    db.session.add(pa)

    # Create a section
    s1 = Section(type="text", content="🌈 Welcome to GitecBoard!", meta="intro")
    db.session.add(s1)
    db.session.flush()

    sa = SectionAssignment(page_id=page.id, section_id=s1.id, order=0)
    db.session.add(sa)

    db.session.commit()
    print("✅ Seed data inserted successfully.")
