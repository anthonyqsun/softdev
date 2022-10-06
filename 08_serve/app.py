# 10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen
# SoftDev
# 2022-10-06

import numbercruncher
from flask import Flask
app = Flask(__name__)

@app.route("/")
def disp_random_occ():
    jobDict = numbercruncher.generate_dict("occupations.csv") 
    s = ""
    s += "<h1>10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen presents:</h1>"
    s += "<p>your best bet at having a job: " + give_weighted_job(jobDict)+"</p>"



app.run()

