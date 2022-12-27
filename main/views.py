from flask import Blueprint, render_template,request
import functions as f
import logging


POST_PATH = "posts.json"
logging.basicConfig(filename='basic.log', level=logging.INFO)

blueprint_main = Blueprint("blueprint_main", __name__, template_folder="templates")


@blueprint_main.route('/')
def page_main():
    return render_template("index.html")


@blueprint_main.route("/search")
def page_search():
    data = f.load_json(POST_PATH)
    search = request.args.get("s")
    logging.info("Выполнение поиска")
    return render_template("post_list.html", s=search, data=data)