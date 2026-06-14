# Island Daily - Flask News Website

Island Daily is a beginner-friendly Python Flask news website with a modern Singapore newspaper-inspired layout. It includes a homepage, sticky navigation bar, article cards, full article pages, related articles, and responsive styling for desktop and mobile screens.

This project is inspired by the structure and professional feel of Singapore newspaper websites, but it uses original branding, layout details, styling, and article text.

## Features

- Python Flask backend
- Jinja2 HTML templates
- Responsive HTML and CSS layout
- Newspaper-style masthead
- Sticky navigation bar with working category section links
- Homepage hero article
- Secondary article cards
- Latest headlines sidebar
- Homepage category sections for Singapore, Business, World, Sport, Tech, and Opinion
- Individual article pages
- Related articles section
- Original Singapore-style news content
- Formula 1 Singapore Grand Prix article included
- Navbar links scroll to the correct homepage sections

## Project Structure

```text
news_project/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── article.html
└── static/
    └── style.css
```

## Technologies Used

- Python
- Flask
- Jinja2
- HTML5
- CSS3

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/mariorinaldi1907/News-Project.git
cd news_project
```

### 2. Create a virtual environment

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

### 5. Open the website

Visit this address in your browser:

```text
http://127.0.0.1:5000
```

## How the Backend Works

The backend is built with Flask in `app.py`.

- The homepage route `/` loads the main page.
- The article route `/article/<slug>` loads each separate article page.
- Article data is stored in a Python dictionary, so no database is required.
- Jinja templates display the article data dynamically.
