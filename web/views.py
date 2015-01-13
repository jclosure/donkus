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
        title="Donkus",
        message="The bear chased the princess.  The princess ate the bear.",
        year=datetime.now().year
    )

