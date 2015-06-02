"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import json
from web import app

from donkus import map
from donkus import dictable


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    data = map.generate()
    for room in data:
        room.paths = [(room.name, room.paths[path].name) for path in room.paths]

    return render_template(
        'index.html',
        title="Donkus",
        message="Walkthrough Adventure Game",
        data=dictable.todict(data),
        monkey="chimp",
        year=datetime.now().year
    )




