# Whatever: Elizabeth, Maya, Anthony
# SoftDev
# K12
# 2022-10-18
# time-spent: 1 hr

from flask import Flask, render_template, request #import modules


app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/auth", methods=['GET', 'POST']) # /auth is referenced in form action in the html #, methods=['GET', 'POST']) # By default the user can both post and request info but passing the methods parameter specifies which operations can be done
def authenticate():
    if request.method =='POST': #forces post request
        name = request.form['name'] #allows you to access name
    return render_template("response.html", name=request.form['name'], req=str(request.method))


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
