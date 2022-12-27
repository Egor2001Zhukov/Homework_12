from flask import Blueprint, render_template


blueprint_main = Blueprint("blueprint_main", __name__)


@blueprint_main.route('/')
def page_main():
    return render_template("index.html")
