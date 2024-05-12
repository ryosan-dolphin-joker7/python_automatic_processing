from flask import Flask

# Flaskオブジェクトを生成 --- (*1)
app = Flask(__name__)

#「/」へアクセスがあった場合の処理 --- (*2)
@app.route("/")
def root():
    return "Hello!"

#「/test」へアクセスがあった場合の処理 --- (*3)
@app.route("/test")
def test():
    return "Test..."

# Webサーバーを起動 --- (*4)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
