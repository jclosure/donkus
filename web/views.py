"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import json
from web import app

from donkus import map

dictget = lambda d, *k: [d[i] for i in k]

def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

def room_serializer(o):
    if isinstance(o, map.Room):
        o.paths = [(o.name, o.paths[path].name) for path in o.paths]
    if isinstance(o, set):
        return list(o)
    return o.__dict__




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    data = map.generate()
    for room in data:
        room.paths = [(room.name, room.paths[path].name) for path in room.paths]

    data_string = json.dumps(data, default=jdefault)

    return render_template(
        'index.html',
        title="Donkus",
        message="Walkthrough Adventure Game",
        data=data_string,
        year=datetime.now().year
    )




