# Dojo Form Project

A clean, minimalist Django web application that demonstrates handling multi-input forms, capturing radio button and checkbox values (arrays), and securely passing data between views using Django Sessions to prevent post-redirect data loss.

---

## Features
* **Form Handling & Validation:** Captures multiple input types including text, dropdowns, radio buttons, and textareas.
* **Multi-Select Array Capture:** Uses Django's `getlist()` method to process multiple checkboxes for spoken languages simultaneously.
* **Safe Redirect Pattern:** Implements Django Sessions (`request.session`) to transition data securely to the results page without query string clutter.


## Tech Stack
* **Backend:** Python / Django
* **Frontend:** HTML5 / CSS3 

---

## Project Structure
```text
dojo_project/
├── dojo_project/        # Project configuration (settings.py, urls.py)
├── dojo_app/            # Main application logic
│   ├── templates/       # HTML view templates (index.html)
│   ├── static/          # Frontend assets
│   │   └── css/
│   │       └── style.css
│   ├── views.py         # Form processing & session logic
│   └── urls.py          # App-level routing
├── db.sqlite3           # Local development database
└── manage.py            # Django command-line utility