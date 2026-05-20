# Display Time Project

A clean, minimalist Django web application that displays the current date and time in a beautifully styled, responsive box interface. Built as part of the full-stack development curriculum.

---

## Features
* **Live Server Time:** Fetches and structures real-time data using Python's `datetime` module.
* **12-Hour Format:** Displays time in a highly readable format (`Oct 26, 2013 11:26 AM`).
* **Minimalist UI:** Clean, grid-aligned design with sharp borders and distinct text boxes.

## Tech Stack
* **Backend:** Python 3.11+ / Django 5.2+
* **Frontend:** HTML5 / CSS3 (Custom styling)

---

## 📂 Project Structure
```text
display_time/
├── display_time_project/    # Project configuration (settings.py, urls.py)
├── timer_app/               # Main application logic (views.py)
├── templates/               # Global HTML views (index.html)
└── static/                  # Frontend assets
    └── css/
        └── style.css        # Custom box layout & typography