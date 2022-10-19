# Whatever: Elizabeth, Maya, Anthony
# SoftDev
# K14
# 2022-10-20
# time-spent: 0.2 hr

from flask import Flask, render_template #import modules


app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    return render_template( 'index.html' )

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
