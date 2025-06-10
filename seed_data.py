import os
from app.main import create_app, db
from app.models.board import Board, PageAssignment
from app.models.page import Page
from app.models.section import Section, SectionAssignment
from app.models.admin import AdminUser, AppSetting

# --- PATH SETUP ---
current_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(current_dir, "data")
db_path = os.path.join(db_dir, "infoboard.db")
os.makedirs(db_dir, exist_ok=True)

if os.path.exists(db_path):
    os.remove(db_path)
    print(f"🗑️ Deleted existing database at {db_path}")

app = create_app()
with app.app_context():
    # --- ADMIN USER ---
    admin = AdminUser(
        username="admin",
        email="afrey@gi-tec.net",
        first_name="Admin",
        last_name="User",
        is_system_admin=True
    )
    admin.set_password("admin")
    db.session.add(admin)
    db.session.commit()
    print("✅ Admin user created.")

    # --- BOARD ---
    board = Board(
        name="Default Board",
        slug_identifier="default-board"
    )
    db.session.add(board)
    db.session.flush()
    print("✅ Board created.")

    # --- PAGE ---
    page = Page(
        title="Default Page"
    )
    db.session.add(page)
    db.session.flush()
    print("✅ Page created.")

    # --- PAGE ASSIGNMENT ---
    pa = PageAssignment(
        board_id=board.id,
        page_id=page.id,
        order=0
    )
    db.session.add(pa)
    db.session.commit()
    print("✅ Page assigned to board.")

    # --- SECTION ---
    s1 = Section(
        title="Intro Section",
        type="text",
        content="🌈 Welcome to GitecBoard!"
    )
    db.session.add(s1)
    db.session.flush()
    print("✅ Section created.")

    # --- SECTION ASSIGNMENT ---
    sa = SectionAssignment(
        page_id=page.id,
        section_id=s1.id,
        order=0
    )
    db.session.add(sa)
    db.session.commit()
    print("✅ Section assigned to page.")

print("🎉 All seed data inserted successfully.")
