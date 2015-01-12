"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from web import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title="Story Time",
        message="Come close to the fire and look into my eyes.",
        year=datetime.now().year
    )

