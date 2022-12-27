from flask import Blueprint, render_template, request
from functions import dump_json
from functions import check
import logging



POST_PATH = "post.json"
UPLOAD_FOLDER = "uploads/images"
logging.basicConfig(filename='basic.log', level=logging.INFO)


blueprint_add_post = Blueprint("add_post", __name__, template_folder="templates")


@blueprint_add_post.route('/post')
def page_post_form():
    return render_template("post_form.html")


@blueprint_add_post.route("/post", methods=["POST"])
def page_post_upload():
    content = request.values.get("content")
    picture = request.files.get("picture")
    filename = picture.filename
    if check(filename):
        if content and picture:
            picture.save(f'./uploads/images/{filename}')
            dump_json(POST_PATH, filename, content)
            return render_template("post_uploaded.html", filename=filename, content=content)
        else:
            logging.error("Ошибка загрузки")
            return 'Ошибка загрузки<link rel="stylesheet" href="../static/style.css">'
    else:
        logging.info("Загруженный файл - не картинка")
        return 'Загруженный файл - не картинка<link rel="stylesheet" href="../static/style.css">'