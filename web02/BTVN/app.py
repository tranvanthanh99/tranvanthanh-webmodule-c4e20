from flask import Flask, render_template
import mlab
from mongoengine import *
from models.customers import Customer
from models.service import Service

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):

    all_service = Service.objects(gender = g,yob__lte=1998,height__lte=165)
    return render_template('search.html',all_service=all_service)


@app.route('/customer/<g>/<s>')
def customer(g,s):
    all_customers = Customer.objects(gender = g, Status = s)
    top_10 = all_customers[0:10]
    return render_template('customer.html',all_customers=top_10)

if __name__ == '__main__':
  app.run(debug=True)
 
 