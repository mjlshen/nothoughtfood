from flask import Flask, request, render_template
import os, csv

app = Flask(__name__)

recipes = {key: value for key, value in csv.reader(open("recipes"))}

@app.route('/', methods=['GET', 'POST'])
def findRecipe():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		try:
			inputTime = recipes[(''.join([i for i in request.form['inputTime']]))]
		except KeyError:
			return render_template('index.html', recipes = request.form['previousRecipes'], static = True)
		if request.form['previousRecipes'] == '':
			return render_template('index.html', recipes = inputTime.replace(',', ', '), static = False)
		return render_template('index.html', recipes = inputTime.replace(',', ', ') + "<hr>" + request.form['previousRecipes'], static = False)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)