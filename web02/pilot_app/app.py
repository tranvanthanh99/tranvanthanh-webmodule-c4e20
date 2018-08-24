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

@app.route('/search/<g>')
def search(g):

    all_service = Service.objects(gender = g,yob__lte=1998,height__lte=165,address__icontains='Hà Nội')
    return render_template('search.html',all_service=all_service)

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

        new_service=Service(
            name=name,
            yob=yob,
            phone=phone
        )
        new_service.save()

        return redirect(url_for('admin')) 

if __name__ == '__main__':
  app.run(debug=True)
 

# setdefault input value
# radio button