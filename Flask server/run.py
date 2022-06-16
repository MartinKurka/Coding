from bitcoin import CurrentBtcPrice
from request_btc import get_btc_current_price
from web import main
from flask import Flask, render_template
import subprocess as sp
import os

app = Flask(__name__)

imagefolder = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = imagefolder


@app.route("/")
def hello():
   date, price_usd, price_czk = get_btc_current_price()
   templateData = {
      'img': os.path.join(app.config['UPLOAD_FOLDER'], 'btc_export.png'),
      'title' : 'Meteostanice',
      'bitcoin': [date, int(price_usd), int(price_czk)],
      }
   return render_template('index.html', **templateData)

@app.route("/milovice")
def milovice():
   city = "Milovice"
   coordinations = {"lat": 50.22622179742758, "lon": 14.870976579184042}
   req = main(coordinations, city)
   # req = "ppp"
   templateData = {
      'title' : "Milovice",
      'json_file': req
      }
   return render_template('milovice.html', **templateData)

@app.route('/hrazany')
def hrazany():
   city = "Hrazany"
   coordinations = {"lat": 49.734889, "lon": 14.401448}
   req = main(coordinations, city)
   # req = "ppp"
   templateData = {
      'title': 'Hrazany',
      'json_file': req
   }
   return render_template('hrazany.html', **templateData)

@app.route('/praha')
def praha():
   city = "Praha 6 - Na Dlouhém lánu"
   coordinations = {"lat": 50.09544884869726, "lon": 14.358753027015418}
   req = main(coordinations, city)
   # req = "ppp"
   templateData = {
      'title': 'Praha 6 - Na Dlouhém lánu',
      'json_file': req
   }
   return render_template('praha.html', **templateData)

@app.route('/system_info')
def system_info():
   # Linux
   # output = sp.getoutput('python3.8 informations.py')

   # windows
   output = sp.getoutput('system_info.py')
   templateData = {
      'info': output,
   }
   return render_template('system_info.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)