#!/usr/bin/python3
"""
Views index
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """Status of API"""
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def stats():
    """Retrieve the num obj by type"""
    stat = {}

    for key, value in classes.items():
        stat[key] = storage.count(value)

    return jsonify(stat)
