from wheather_api import DayInWeek, api_req
    

from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route("/")
def hello():
   # req = api_req()
   req = "ppp"
   now = datetime.datetime.now()
   timeString = now.strftime("-%m-%d %H:%M:%S")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'json_file': req
      }
   return render_template('index.html', **templateData)

@app.route('/next')
def next():
    return render_template('next.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)