# from flask import Flask, send_from_directory, abort
# import os
#
# app = Flask(__name__, static_folder='static/dist', template_folder='static/dist')
#
# @app.route('/')
# def index():
#     return send_from_directory(app.template_folder, 'index.html')
#
# @app.route('/<path:path>')
# def serve_vue(path):
#     if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
#         return send_from_directory(app.static_folder, path)
#     else:
#         # 如果路径不存在或为空，则返回 index.html
#         return send_from_directory(app.template_folder, 'index.html')
#
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/api/llm', methods=['POST'])
def get_responses():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # 假设有两个模型 API
    model_urls = [
        'https://model1.example.com/generate',
        'https://model2.example.com/generate'
    ]

    responses = []
    for url in model_urls:
        try:
            r = requests.post(url, json={'prompt': prompt})
            r.raise_for_status()
            responses.append(r.json()['response'])
        except requests.RequestException as e:
            responses.append(f'Error calling {url}: {str(e)}')

    return jsonify(responses)


if __name__ == '__main__':
    app.run(debug=True)