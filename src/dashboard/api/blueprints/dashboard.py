from flask import Blueprint, render_template, abort


dashboard_api = Blueprint("dashboard", __name__)


@dashboard_api.route("/", methods=["GET"])
def dashboard():
    try:
        return render_template("index.html")
    except Exception:
        abort(404)
