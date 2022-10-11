# 10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen
# SoftDev
# 2022-10-06
#Time Spent: 1 Hour

"""
DISCO:
* how to use flask
* we can render html thru the return
* csv library is very useful to parse csv files

QCC:
* Why does app.debug = True give us an error? (/usr/bin/python3: No module named thonny.plugins.cpython.app)

OPS SUMMARY:
* We refactored our numbercruncher.py file to return a dictionary that contains jobs and their weights / generate a weighted random job
* We then followed the flask templates from 00_flask
* We made the information more presentable by wrapping it with HTML

"""
import random
import numbercruncher
from flask import Flask
app = Flask(__name__)

jobDict = numbercruncher.generate_dict("occupations.csv")

@app.route("/")
def disp_random_occ():
    s = ""
    job = str(numbercruncher.give_weighted_job(jobDict)).lower()
    s += "<h1>10 items or fewer express checkout lane </h1> <h2> Daniel Liu, Anthony Sun, Jasmine Yuen </h2>"
    s += f"<p>Your best bet is the <i> <a style = \"color: hsl({random.randrange(0,256)},90%,30%)\" href=\"https://www.google.com/search?q=how+to+apply+to+ {job.replace(' ','+')}\"> {job}</a></i> job </p>"
    s += "All the occupations are: " + numbercruncher.get_all_occupations(jobDict)
    return s

app.debug = True
app.run()
