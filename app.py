from flask import Flask, request, render_template, send_from_directory
from main.views import blueprint_main
from loader.views import blueprint_add_post


app = Flask(__name__)


app.register_blueprint(blueprint_main)


app.register_blueprint(blueprint_add_post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

