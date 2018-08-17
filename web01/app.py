from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts =[
        {
        "title":"Thơ con cóc" ,
        "content":"""
            Hôm nay trăng lên cao quá
            Anh muốn hôn em vào má
            """,
        "author":"Tuấn Anh",
        "author_sex":1
        },
        {
        "title":"Thơ con cóc" ,
        "content":"""
            Hôm nay trăng lên cao quá
            Anh muốn hôn em vào má
            """,
        "author":"Tuấn Anh",
        "author_sex":1
        }
    ]
    return render_template('index.html',posts=posts)

@app.route('/hello')
def say_hello():
    return "hello from the other side"

@app.route('/say-hi/<name>/<age>')
def say_hi(name,age):
    return "Hi {},you`re {} years old".format(name,age)

@app.route('/sum/<int:x>/<int:y>')

def sum2(x,y):
    return str(x+y)

if __name__ == '__main__':
  app.run(debug=True)
 