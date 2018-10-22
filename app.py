from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('homepage.html')

@app.route('/anime')
def anime():
	animes = ['Bebop', 'Golden-Kamuy', 'Jojos-Bizarre-Adventure',
			'Akira', 'Fate-Zero', 'Unlimited-Blade-Works',
			'Fullmetal-Alchemist-Brotherhood', 'Kizumonogatari', 'Redline']
	return render_template('anime.html', names = animes)

@app.route('/games')
def games():
	games = ['PoE-Deadfire', 'Nier-Automata', 'Spiderman',
			'Monster-Hunter-World', 'VA-11-Hall-A', 'Fate-Grand-Order',
			'Persona-5', 'Breath-of-the-Wild', 'Splatoon-2']
	return render_template('games.html', names = games)

@app.route('/anime/<animename>')
def anime_name(animes):
	return render_template('base.html')

@app.route('/games/<gamename>')
def game_name(games):
	return render_template('base.html')

