#!/usr/bin/env python3
"""Flask app to serve the calculator UI and evaluate expressions via Python safe_eval."""
from flask import Flask, request, jsonify, send_from_directory
import os

from calculator import safe_eval

app = Flask(__name__, static_folder="ui", static_url_path="")


@app.route("/eval", methods=["POST"])
def eval_expr():
    data = request.get_json(silent=True) or {}
    expr = data.get("expr")
    if expr is None:
        return jsonify({"error": "missing 'expr' in JSON payload"}), 400
    try:
        result = safe_eval(expr)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
