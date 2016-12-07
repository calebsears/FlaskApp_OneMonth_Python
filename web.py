from flask import Flask, render_template, request
app = Flask(__name__)
import weather

@app.route("/")
def index():
	name = request.values.get('name')
	location = request.values.get('location')
	forecast = None
	if location:
		forecast = weather.get_weather(location)
	return render_template('index.html', name=name, forecast=forecast)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
    app.run()