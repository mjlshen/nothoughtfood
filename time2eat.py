from flask import Flask, request, render_template
import os, csv

app = Flask(__name__)

recipes = {key: value for key, value in csv.reader(open("recipes"))}

@app.route('/', methods=['GET', 'POST'])
def unscrambleWord():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		try:
			inputAnagrams = recipes[(''.join([i for i in request.form['inputAnagrams']]))]
		except KeyError:
			return render_template('index.html', anagrams = request.form['previousAnagrams'], static = True)
		if request.form['previousAnagrams'] == '':
			return render_template('index.html', anagrams = inputAnagrams.replace(',', ', '), static = False)
		return render_template('index.html', anagrams = inputAnagrams.replace(',', ', ') + "<hr>" + request.form['previousAnagrams'], static = False)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000)
	app.run(host='0.0.0.0', port=port)