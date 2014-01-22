from flask import Flask, request, render_template, send_from_directory
import os, csv

app = Flask(__name__)

recipes_break = {key: value for key, value in csv.reader(open("recipes_break"))}
recipes_lunch = {key: value for key, value in csv.reader(open("recipes_lunch"))}
recipes_dinner = {key: value for key, value in csv.reader(open("recipes_dinner"))}


#@app.route('/favicon.ico')
#def favicon():
#	return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def placeholder():
	return render_template('index.html')
@app.route('/breakfast', methods=['GET', 'POST'])
def findRecipeb():
	if request.method == 'GET':
		return render_template('breakfast.html')
	if request.method == 'POST':
		try:
			inputTime = recipes_break[(''.join([i for i in request.form['inputTime']]))]
		except KeyError:
			return render_template('breakfast.html', recipes_break = request.form['previousRecipes'], static = True)
		if request.form['previousRecipes'] == '':
			return render_template('breakfast.html', recipes_break = inputTime.replace(',', ', '), static = False)
		return render_template('breakfast.html', recipes_break = inputTime.replace(',', ', ') + "<hr>" + request.form['previousRecipes'], static = False)
@app.route('/lunch', methods=['GET', 'POST'])
def findRecipel():
	if request.method == 'GET':
		return render_template('lunch.html')
	if request.method == 'POST':
		try:
			inputTime = recipes_lunch[(''.join([i for i in request.form['inputTime']]))]
		except KeyError:
			return render_template('lunch.html', recipes_lunch = request.form['previousRecipes'], static = True)
		if request.form['previousRecipes'] == '':
			return render_template('lunch.html', recipes_lunch = inputTime.replace(',', ', '), static = False)
		return render_template('lunch.html', recipes_lunch = inputTime.replace(',', ', ') + "<hr>" + request.form['previousRecipes'], static = False)
@app.route('/dinner', methods=['GET', 'POST'])
def findReciped():
	if request.method == 'GET':
		return render_template('dinner.html')
	if request.method == 'POST':
		try:
			inputTime = recipes_dinner[(''.join([i for i in request.form['inputTime']]))]
		except KeyError:
			return render_template('dinner.html', recipes_dinner = request.form['previousRecipes'], static = True)
		if request.form['previousRecipes'] == '':
			return render_template('dinner.html', recipes_dinner = inputTime.replace(',', ', '), static = False)
		return render_template('dinner.html', recipes_dinner = inputTime.replace(',', ', ') + "<hr>" + request.form['previousRecipes'], static = False)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug = True)