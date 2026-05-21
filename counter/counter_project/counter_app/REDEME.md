# Django Counter Application

A simple and interactive web application built with Python and Django that tracks and manipulates user session data. The application maintains a counter per user session, allowing individuals to increment, jump-count, or reset their total visits/actions.

## Features

* **Session Tracking:** Keeps track of individual user interaction count without requiring a database or login.
* **Auto-Increment:** Automatically increments the counter by 1 every time the home page is loaded or refreshed.
* **Quick Add Button:** An explicit button to add +1 manually to the counter.
* **Custom Increment Form:** Allows users to input a specific number and increment the counter by that value instantly.
* **Reset functionality:** Clears the active session and resets the counter instantly back to its initial state.

---

## Tech Stack

* **Backend:** Python + & Django 
* **Frontend:** HTML5, CSS3 
* **State Management:** Django Session Framework

---

## Project Structure

```
counter/
│
├── counter_project/        # Django project configuration directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── counter_app/            # Main application directory
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css   # Custom styling
│   ├── templates/
│   │   └── index.html      # Main user interface
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py            # Core application logic
│
└── manage.py               # Django management script