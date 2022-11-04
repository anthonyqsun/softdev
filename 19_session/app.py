from flask import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
print(app.secret_key)

@app.route("/", methods = ['GET','POST'])
def foo():
    session['username'] = 'laptopnation'
    session['password'] = 'whatever'

    try:
        username = request.form['username']
        password = request.form['password']
    except:
        return render_template("login.html", message="")
    
    if request.method=="POST":
        if username != session['username']:
            return render_template("login.html", message="bad username")

        if password != session['password']:
            return render_template("login.html", message="bad password")

        return render_template("response.html", username=username)
    
    return render_template("login.html", message="")
        
@app.route("/logout")
def boo():
    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()