from flask import Flask, render_template, request, redirect, url_for
from vehicle import add_vehicles, get_any_vehicles
from drivers import get_drivers, assign_driver

app = Flask(__name__)

@app.route('/vehicle', methods=['POST'])
def Vehicle_route():
   Vehicle_ID = request.form['Vehicle_ID']
   location = request.form['Location']
   add_vehicles(Vehicle_ID, location)
   message = "Vehicle"+ Vehicle_ID + "added at", + location
   return render_template ('home.html', message)                                             
  

@app.route('/')
def home(): 
   return render_template('home.html')


@app.route('/vehicle_list')
def vehicle_list():
   get_vehicles = get_any_vehicles()
   

   return render_template("about.html")


@app.route('/about')
def about ():
   return render_template("about.html")


if __name__=="__main__":
   app.run(debug=True)