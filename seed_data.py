import os
from app.main import create_app, db
from app.models.board import Board, PageAssignment
from app.models.page import Page
from app.models.section import Section, SectionAssignment, MediaAsset
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
        title="Default Board",
        slug_identifier="default-board"
    )
    db.session.add(board)
    db.session.flush()
    print("✅ Board created.")

    # --- PAGE ---
    page = Page(
        title="Default Page",
        slug_identifier="default-page",
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
    print("✅ Text Section created.")

    s2 = Section(
        title="Image Section",
        type="image",
        content="https://example.com/image.jpg",  # Example image URL
        meta="An example image section"
    )

    db.session.add(s2)
    db.session.flush()

    print("✅ Image Section created.")

    s3 = Section(
        title="Video Section",
        type="video",
        content="https://example.com/video.mp4",  # Example video URL
        meta="An example video section"
    )

    db.session.add(s3)
    db.session.flush()

    print("✅ Video Section created.")

    # --- MEDIA ASSET ---
    media_asset = MediaAsset(
        file_path="https://example.com/media.mp4",  # Example media URL
        media_type="video"
    )

    db.session.add(media_asset)
    db.session.flush()

    print("✅ Media Asset created.")

    # --- SECTION ASSIGNMENTS ---

    sa = SectionAssignment(
        page_id=page.id,
        section_id=s1.id,
        order=0
    )
    db.session.add(sa)
    sa2 = SectionAssignment(
        page_id=page.id,
        section_id=s2.id,
        order=1
    )
    db.session.add(sa2)
    sa3 = SectionAssignment(
        page_id=page.id,
        section_id=s3.id,
        order=2
    )
    db.session.add(sa3)

    db.session.commit()
    print("✅ Section assigned to page.")


    # --- APP SETTINGS ---
    app_setting = AppSetting(
        key="site_name",
        value="GitecBoard",
        description="The name of the site"
    )
    db.session.add(app_setting)
    app_setting2 = AppSetting(
        key="default_bgcolor",
        value="FFFFFF",
        description="The default background color for the site"
    )

    db.session.add(app_setting2)
    app_setting3 = AppSetting(
        key="default_textcolor",
        value="000000"
        , description="The default text color for the site"
    )
    db.session.add(app_setting3)
    db.session.commit()
    print("✅ App settings created.")
print("🎉 All seed data inserted successfully.")
