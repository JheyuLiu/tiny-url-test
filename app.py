from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegexConverter(BaseConverter):
    regex = r'[A-Za-z0-9]{9}'

app.url_map.converters['regex'] = RegexConverter

@app.route('/<regex:uid>', methods=['GET'])
def get_url(uid):
    id = str(uid)
    return jsonify({"short_id": id})

@app.route('/', methods=['GET', 'POST'])
def add_item():
    if request.method == 'GET':
        return jsonify({"data": "hello"})
    elif request.method == 'POST':
        return jsonify({"url": "https://www.google.com",
                        "shortenUrl": "https://shortenurl.org/g20hi3k9"})

if __name__ == '__main__':
    app.run(debug=False)