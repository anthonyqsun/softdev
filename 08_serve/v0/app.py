# 10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen
# SoftDev
# 2022-10-06

from flask import Flask
app = Flask(__name__) # Creates Instance of flask class

@app.route("/") # Assigns the function to root directory
def hello_world():
    print(__name__) # Print in terminal
    return "No hablo queso!"  # Will return to webpage of the localhost

app.run()  # Runs
                
