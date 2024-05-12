from flask import Flask
import glob

# Flaskオブジェクトを生成 --- (*1)
app = Flask(__name__)

#「/」へアクセスがあった場合の処理 --- (*2)
@app.route("/")
def root():
    # ファイル一覧を列挙 --- (*3)
    files = glob.glob('static/*')
    # HTMLでファイル一覧のリンクを表示 --- (*4)
    html = '<html><meta charset="utf-8"><body>'
    html += '<h1>ファイル一覧</h1>'
    for f in files:
        html += '<p><a href="{0}">{0}</a></p>'.format(f)
    html += '</body></html>'
    return html

# Webサーバーを起動 --- (*5)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
