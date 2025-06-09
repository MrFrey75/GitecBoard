from app.main import db
from datetime import datetime

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False, default="text")
    content = db.Column(db.Text, nullable=False)
    meta = db.Column(db.Text, nullable=True)

    start_time = db.Column(db.DateTime, nullable=True)  # When section becomes visible
    end_time = db.Column(db.DateTime, nullable=True)    # When section expires

    section_assignments = db.relationship(
        'SectionAssignment',
        back_populates='section',
        cascade='all, delete-orphan',
        lazy=True
    )

    def is_visible(self):
        now = datetime.utcnow()
        if self.start_time and now < self.start_time:
            return False
        if self.end_time and now > self.end_time:
            return False
        return True
