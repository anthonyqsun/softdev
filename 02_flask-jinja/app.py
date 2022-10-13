'''
10 items or fewer express checkout line: Daniel, Anthony, Jasmine
Softdev pd02
k10
2022-10-13
time spent: 0.3 hr
'''

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...) -> it will throw an error saying render_template is not defined

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page? -> http://127.0.0.1/my_foist_template
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best. -> 1st argument is template file in /templates; other arguments are field replacements in html file

if __name__ == "__main__":
    app.debug = True
    app.run()
