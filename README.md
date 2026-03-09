# 🚀 Django Multi-Project Showcase

[![Django](https://img.shields.io/badge/Django-4.1.13-092e20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Storage-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A collection of 5 distinct Django applications integrated into a single repository, showcasing various web development patterns from E-commerce to Social Networking.

---

## 📱 Featured Applications

### 🛒 [Auctions Bidding](file:///c:/Umair/django_py_any_where/auctions)

A robust auction platform where users can list items, bid in real-time, and manage their watchlists.

- **Key Features**: Real-time bidding, category sorting, watchlist management, and comment systems.
- **Concepts**: User Authentication, Model Relationships, Complex Form Handling.

### 📢 [Ads Posting](file:///c:/Umair/django_py_any_where/ads)

A classified ads application for posting and managing various listings with image support.

- **Key Features**: Image uploads, owner-based CRUD permissions, search functionality.
- **Concepts**: Media handling, Custom Mixins, View Inheritance.

### 📧 [Single-Page E-mail](file:///c:/Umair/django_py_any_where/mail)

A modern, single-page application (SPA) mail client for internal communication.

- **Key Features**: Dynamic inbox loading, sent/archived folders, compose interface without page reloads.
- **Concepts**: JavaScript Fetch API, Asynchronous UI updates, Single Page Architecture.

### 🤝 [Social Network](file:///c:/Umair/django_py_any_where/network)

A Twitter-like social platform for connecting with others and sharing updates.

- **Key Features**: Following/Unfollowing, profile customization, post likes, and paginated feeds.
- **Concepts**: Recursive model relationships, API-driven interactions, pagination.

### 📚 [Wiki App](file:///c:/Umair/django_py_any_where/wiki)

An encyclopedia application allowing users to search, create, and edit entries.

- **Key Features**: Markdown-to-HTML conversion, random page fetch, smart search.
- **Concepts**: File I/O, Markdown processing, URL routing.

---

## 🛠️ Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/umairny/django_py_any_where.git
   cd django_py_any_where
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

---

## 📁 Project Structure

```text
├── ads/            # Ads Posting App
├── auctions/       # Auctions Bidding App
├── home/           # Central landing page logic
├── mail/           # Single-page Mail App
├── network/        # Social Network App
├── wiki/           # Wiki application
├── myproject/      # Core settings and configuration
└── manage.py       # Django project manager
```

---

## 🌐 Deployment

This project is configured for deployment on **PythonAnywhere**.

[Home of all code](https://github.com/umairny/django_py_any_where)
