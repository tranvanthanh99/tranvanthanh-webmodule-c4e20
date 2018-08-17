from flask import Flask, render_template, redirect
app = Flask(__name__)

# without render_template()

@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight,height):

    height_m = height/100
    BMI=weight/(height_m**2)

    if BMI < 16:
        return "Severely underweight"
    elif BMI < 18.5:
        return "Underweight"   
    elif BMI < 25:
        return "Normal"
    elif BMI < 30:
        return "Overweight"
    else :
        return "Obese" 


# with render_template()

@app.route('/bmi-2/<int:weight>/<int:height>')
def BMI_2(weight,height):

    height_m = height/100
    BMI=weight/(height_m**2)
    a= ((BMI*100)//1)/100
    condition = ""
    if BMI < 16:
        condition = "Severely underweight"
    elif BMI < 18.5:
        condition = "Underweight"  
    elif BMI < 25:
        condition = "Normal"
    elif BMI < 30:
        condition = "Overweight"
    else :
        condition = "Obese" 

    return render_template('bmi.html',BMI = a,condition = condition)



if __name__ == '__main__':
  app.run(debug=True)