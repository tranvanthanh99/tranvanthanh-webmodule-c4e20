from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.user import User
from models.order import Order
from datetime import datetime

app = Flask(__name__)

app.secret_key = "a super secret key"

mlab.connect()

# # design pattern(MVC,MVP)

@app.route('/')
def index():
    if "loggedin" in session:

        if session['loggedin']:
            return render_template('index.html', session=session['loggedin'])
        else:
            
            return render_template('index.html', session=session['loggedin'])
    else:
        session['loggedin'] = False
        return render_template('index.html', session=session['loggedin'])
    

@app.route('/create')
def New():

    return redirect(url_for('new-service'))

@app.route('/search/')
def search():
    if "loggedin" in session:

        if session['loggedin']:
            all_service = Service.objects()
            return render_template('search.html',all_service=all_service)
        else:
            
            return redirect(url_for('login', session=session['loggedin']))
    else:
        session['loggedin'] = False
        return redirect(url_for('login', session=session['loggedin']))

@app.route('/detail/<service_id>')
def detail(service_id):

    service_detail = Service.objects.with_id(service_id)
    if service_detail is not None:
        return render_template('detail.html',service_detail=service_detail)
    else:
        return "Not Found"

@app.route('/update-service/<service_id>', methods = ["GET","POST"])
def updateS(service_id):

    new_service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template('update.html',new_service=new_service)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        height = form['height']
        address = form['address']
 
        new_service.update(
            name=name,
            yob=yob,
            phone=phone,
            gender=gender,
            height=height,
            address=address
        )
        return redirect(url_for('admin'))

    

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service=all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Not Found"
    
@app.route('/new-service', methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service=Service(
            name=name,
            yob=yob,
            phone=phone,
            gender=gender
        )
        new_service.save()

        return redirect(url_for('admin')) 

@app.route('/order/<service_id>')
def order(service_id):
    order = Order(
        user_id = session['id'],
        service_id = service_id,
        time = datetime.now(),
        is_accepted = False
    )
    order.save()
    return render_template('order.html')

@app.route('/sign-up', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template('sign-up.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        email = form['email']
        fullname = form['fullname']

        new_user=User(
            username=username,
            password=password,
            email=email,
            fullname=fullname
        )
        new_user.save()

        return redirect(url_for('login')) 

@app.route('/log-in',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('log-in.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        all_users = User.objects()
        for i in range(len(all_users)):
            if username in all_users[i]['username']:
                if username == all_users[i]['username'] and password == all_users[i]['password']:
                    session['id'] = str(all_users[i]['id'])
                    session['loggedin'] = True

                    return redirect(url_for('search'))
                else:
                    continue
            else:
                continue
        return "Sai tên tài khoản hoặc mật khẩu"

@app.route('/logout')
def logout():
    session['loggedin']=False
    del session['id']
    return redirect(url_for('index'))
        

if __name__ == '__main__':
  app.run(debug=True)
 

# setdefault input value
# radio button