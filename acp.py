from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculate" , methods=['POST' , 'GET'])

def calculate():
	bmi=''
	if request.method == 'POST' and 'Weight' in request.form and 'Height' in request.form:
		weight = float(request.form.get('Weight'))
		height = float(request.form.get('Height'))
		bmi = round(weight/((height/100)**2),2)
	return render_template("index.html",bmi=bmi)	

@app.route('/')
def index():
	return render_template('index.html')


app.run(host='0.0.0.0', port=8080)