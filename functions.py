import json


def load_json(filename):
    with open(filename, "rt", encoding='utf-8') as file:
        load_file = file.read()
    return json.loads(load_file)


def dump_json(filename, picture, content):
    try:
        frame = {"pic": picture, "content": content}
        with open(filename, "rt", encoding='utf-8') as file:
            data = json.load(file)
            data.append(frame)
            json.dump(data, open(filename, "w", encoding='utf-8'), indent=2, ensure_ascii=False)
    except Exception:
        print(f'Файл {filename} отсутствует или не хочет превращаться в список :(')


def check(filename):
    acc = ['png', 'jpeg', 'jpg']
    return filename.split(".")[-1].lower() in acc


