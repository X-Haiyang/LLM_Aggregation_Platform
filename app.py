from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__, static_folder='static/dist', template_folder='static/dist')

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/<path:path>')
def serve_vue(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # 如果路径不存在或为空，则返回 index.html
        return send_from_directory(app.template_folder, 'index.html')


if __name__ == '__main__':
    app.run()
