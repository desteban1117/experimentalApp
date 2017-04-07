from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   import RPi.GPIO as GPIO
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(18,GPIO.OUT)
   if(GPIO.input(18) == 1): return render_template('on.html')
   else: return render_template('off.html')
   

@app.route('/on', methods=['GET', 'POST'])
def on():
   import RPi.GPIO as GPIO
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(18,GPIO.OUT)
   if(GPIO.input(18) == 1):
        GPIO.output(18, False)
        return render_template('off.html')
   else:
        GPIO.output(18, True)
        return render_template('on.html')
  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
