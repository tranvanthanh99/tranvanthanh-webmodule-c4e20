from flask import *
import mlab
from mongoengine import *
from models.service import Service

app = Flask(__name__)

mlab.connect()

# # design pattern(MVC,MVP)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def New():
    return redirect(url_for('new-service'))

@app.route('/search/')
def search():

    all_service = Service.objects()
    return render_template('search.html',all_service=all_service)

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

if __name__ == '__main__':
  app.run(debug=True)
 

# setdefault input value
# radio button