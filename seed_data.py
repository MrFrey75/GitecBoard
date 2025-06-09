import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from app.main import create_app, db
from app.models.board import Board, PageAssignment
from app.models.page import Page, SectionAssignment
from app.models.section import Section

# Set hardcoded timezone to Eastern Standard Time
EASTERN = ZoneInfo("America/New_York")

# Define absolute DB path
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "infoboard.db"))

# Delete the database if it exists
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"🗑️ Deleted existing database at {db_path}")
else:
    print(f"📂 No existing database found. Creating new one.")

# Initialize Flask app and database
app = create_app()

with app.app_context():
    db.create_all()

    # Create sections
    s1 = Section(type="text", content="🌈 Welcome to GitecBoard!", meta="intro")
    s2 = Section(type="text", content="✨ Today's magical events are posted here.", meta="announcement")
    s3 = Section(type="text", content="🦄 Remember to bring glitter to class.", meta="reminder")
    s4 = Section(type="text", content="🔮 Weather forecast: 100% chance of rainbows.", meta="weather")
    s5 = Section(type="image", content="https://picsum.photos/id/237/800/300", meta="cute dog image")
    s6 = Section(type="markdown", content="## This is _Markdown_ with **style**!")
    s7 = Section(type="html", content='<p style="color:red">🔥 Raw HTML section!</p>')
    s8 = Section(type="youtube", content="aqz-KE-bpKQ")
    s9 = Section(
        type="text",
        content="🕒 This message self-destructs in 30 seconds!",
        start_time=datetime.now(EASTERN),
        end_time=datetime.now(EASTERN) + timedelta(seconds=30),
        meta="temporary"
    )

    db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    db.session.commit()

    # Create pages
    p1 = Page(name="Welcome Page")
    p2 = Page(name="Updates Page")

    db.session.add_all([p1, p2])
    db.session.commit()

    # Assign sections to pages
    db.session.add_all([
        SectionAssignment(page_id=p1.id, section_id=s1.id, order=1),
        SectionAssignment(page_id=p1.id, section_id=s2.id, order=2),
        SectionAssignment(page_id=p1.id, section_id=s5.id, order=3),
        SectionAssignment(page_id=p2.id, section_id=s3.id, order=1),
        SectionAssignment(page_id=p2.id, section_id=s4.id, order=2),
        SectionAssignment(page_id=p2.id, section_id=s6.id, order=3),
        SectionAssignment(page_id=p2.id, section_id=s7.id, order=4),
        SectionAssignment(page_id=p2.id, section_id=s8.id, order=5),
        SectionAssignment(page_id=p2.id, section_id=s9.id, order=6),
    ])
    db.session.commit()

    # Create board
    board = Board(identifier="GitecBoard")
    db.session.add(board)
    db.session.commit()

    # Assign pages to board
    db.session.add_all([
        PageAssignment(board_id=board.id, page_id=p1.id, order=1, transition_type="fade"),
        PageAssignment(board_id=board.id, page_id=p2.id, order=2, transition_type="slide"),
    ])
    db.session.commit()

    print("✅ Seed data inserted for board 'GitecBoard'")
