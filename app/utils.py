import os
from flask import jsonify


def success(data=None, message="ok", status=200):
    return jsonify({"success": True, "message": message, "data": data}), status


def error(message="error", status=400):
    return jsonify({"success": False, "message": message}), status


def read_prompt(filename, **kwargs):
    path = os.path.join(os.path.dirname(__file__), "prompts", filename)
    with open(path, "r") as f:
        template = f.read()
    return template.format(**kwargs)
