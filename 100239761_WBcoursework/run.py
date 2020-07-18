#import required libraries
from flask import Flask, render_template
from flask import request
from datetime import date
import csv

#create flask object
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('8BrooksLaneRental-Home.html')

@app.route('/8BrooksLaneRental-Home.html')
def home():
    return render_template('8BrooksLaneRental-Home.html')

@app.route('/8BrooksLaneRental-Gallery.html')
def gallery():
    return render_template('8BrooksLaneRental-Gallery.html')

@app.route('/8BrooksLaneRental-PointsofInterest.html')
def poi():
    return render_template('8BrooksLaneRental-PointsofInterest.html')

@app.route('/8BrooksLaneRental-Rental.html')
def rental():
    #upon launching the rental page, a reader to the csv file is initialised and the file is read and assigned to variable theBooking
    with open("static\\bookings.csv", "r") as inFile:
        reader = csv.reader(inFile)
        theBooking = [row for row in reader]
    return render_template('8BrooksLaneRental-Rental.html', theBooking = theBooking)

@app.route('/8BrooksLaneRental-Reviews.html')
def reviews():
    with open("static\\reviews.csv", "r") as inFile:
        reader = csv.reader(inFile)
        theReview = [row for row in reader]
    return render_template('8BrooksLaneRental-Reviews.html', theReview = theReview)

#writes submitted review data to the csv file
@app.route("/review", methods=["GET", "POST"])
def enterReview():
    if request.method == "POST":
        text = request.form["reviewText"]
        #calculates the date server-side to avoid client side tampering
        theDate = str(date.today())

        with open("static\\reviews.csv", "a", newline="") as inFile:
            writer = csv.writer(inFile)
            writer.writerow([text, theDate])

        return reviews()

    else:
        return render_templates("8BrooksLaneRental-Reviews.html")

#writes submitted rent application data to the csv file
@app.route("/application", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form["appName"]
        email = request.form["appEmail"]
        arrival = request.form["appStartDate"]
        departure = request.form["appEndDate"]

        with open("static\\bookings.csv", "a", newline="") as inFile:
            writer = csv.writer(inFile)
            writer.writerow([name, email, arrival, departure])

        return rental()

    else:
        return render_template("8BrooksLaneRental-Rental.html")
        

if __name__=='__main__':
	app.run(debug = True)

