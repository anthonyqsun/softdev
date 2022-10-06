# 10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen
# SoftDev
# 2022-10-06

from flask import Flask
app = Flask(__name__) # creates instance of flask

@app.route("/") # specifies route
def hello_world():
    print(__name__) # print working name to terminal
    return "No hablo queso!"  # output to webpage

app.run()  # runs
                
