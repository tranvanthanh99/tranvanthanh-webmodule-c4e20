from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):

    users = {
        "quan": {
            "name" : "Nguyen Anh Quan",
            "age" : 20,
            "sex": "male"
        },
        "tuananh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 23,
            "sex": "male"
        },
        "thanh":{
            "name": "Trần Văn Thành",
            "age": 18,
            "sex": "male"
        }
    }
    
    if username in users:
        return render_template('users.html',username=users[username])
    else:
        return "User not found"
   
   
if __name__ == '__main__':
  app.run(debug=True)