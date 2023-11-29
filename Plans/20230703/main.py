from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '这是我的第一次的python学习写的程序代码'


if __name__ == "__main__":
    app.run()
