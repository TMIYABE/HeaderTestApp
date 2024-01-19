import os
import hashlib
import bs4
from PIL import Image
from flask import Flask, render_template, make_response, request, abort


app = Flask(__name__, static_folder='./static')

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/cors', methods=["GET","POST"])
def cors():
    return render_template('cors.html')

@app.route('/csrf/<val>', methods=["POST"])
def csrf(val):
    """
    不要
    """
    if "my-header" not in request.headers:
        abort(400)
    value = val
    return render_template('csrf.html', value=value)

@app.route('/cache', methods=['GET'])
def cache():
    """
	ブラウザの仕様により、リロードやURLフォームからの遷移ではキャッシュが利用されることなく、再びリソースの取得が行われる。
    リンクからの遷移の場合にキャッシュの利用が行われる。

	同じURLだけど表示されるhtmlが変わる仕様にしたい。
    そうしたら、Cache-Controlが有効な間に違うhtmlを取得しようとして、キャッシュされたhtmlが表示されたという検証ができそう
    
    JavaScript, CSS, 画像といった静的ファイルはブラウザにキャッシュされてしまう。
    ⇒それの対策としてCache Bustingという方法がある。
    参考：https://tech-blog.rakus.co.jp/entry/20190816/query-parameters/cache
    """
    #page = bs4.BeautifulSoup(open('app/templates/cache.html', encoding = 'utf-8'), 'html.parser')
    response = make_response(render_template('cache.html'))
    response.headers['Cache-Control'] = "max-age=100"
    #response.headers['ETag'] = hashlib.md5(page.encode())
    print("aaaa".encode())
    return response

@app.after_request
def after_request(response):
    #ここで任意のレスポンスヘッダを設定する
    response.headers['Access-Control-Allow-Origin'] = "http://localhost:9999"
    response.headers['Access-Control-Allow-Headers'] = "my-header"
    return response