# GitecBoard

A modular, modern digital information board system for schools, offices, or wherever you want to broadcast info without the corporate bloat. Built with Flask (Python), SQLite, and a Vue/Material admin console that doesn’t suck.

---

## Features

* **Digital Boards**: Manage one or many “boards,” each displaying scheduled pages and sections.
* **Granular Content**: Pages and sections let you build up information your way.
* **Admin API**: Modern, RESTful JSON API (Flask) for all board/page/section CRUD.
* **Decoupled Admin Console**: Future-proofed with a Vue + Material UI dashboard (plug in your own flavor if you hate ours).
* **Seed Data Support**: Easy resets and migrations for fast development and demo.
* **Open-Source First**: No vendor lock-in, no black-box logic, no mystery meat.

---

## Project Structure

```
.
├── app/
│   ├── main.py          # Flask app factory
│   ├── models/          # SQLAlchemy ORM models (Board, Page, Section, Admin)
│   ├── routes/          # Flask blueprints (API, admin, display)
│   ├── templates/       # (If you want classic Flask views)
│   └── static/          # Static files and (eventually) the Vue admin build
├── seed_data.py         # DB bootstrap/reset utility
├── run.py               # Main entry point
├── requirements.txt     # Python dependencies
└── readme.md
```

---

## Quickstart (Dev)

1. **Clone it**

   ```bash
   git clone https://github.com/MrFrey75/GitecBoard.git
   cd GitecBoard
   ```

2. **Set up Python**

   * Python 3.10+ recommended (but if it runs on older, enjoy the entropy).

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Seed your database**
   *Wipes and recreates everything—great for dev, don’t do it in prod.*

   ```bash
   python seed_data.py
   ```

4. **Run the Flask API**

   ```bash
   python run.py
   ```

   * Default: [http://localhost:5000](http://localhost:5000)

5. **API Endpoints**

   * RESTful CRUD for boards/pages/sections at `/api/admin/*`
   * Example:

     * `GET /api/admin/boards`
     * `POST /api/admin/pages`
     * etc.

6. **Vue Admin Console (Coming Soon!)**

   * Modern SPA dashboard.
   * Will live in `/app/static/admin/` or run as a separate dev server.
   * Connects via the Flask API—flexible, headless, not bound to Flask templates.

---

## Roadmap

* [x] Flask modular backend with models and REST API
* [x] Board, page, section management via API
* [ ] Vue/Material Admin SPA (plug-and-play)
* [ ] Authentication (JWT or classic session—TBD)
* [ ] User management and audit logging
* [ ] Prebuilt info widgets (calendar, weather, bell schedule, etc.)

---

## Contributing

PRs and issues welcome! Build the tools you wish someone else would.

---

## License

MIT. Free as in speech, not as in surveillance capitalism.

---

**Go ahead, fork it, break it, make it yours.**