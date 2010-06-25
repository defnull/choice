import os, sys
import bottle
import choice

gamedir = './'
games = {}
games['test'] = 'Test Game'
sessions = {}
app = bottle.Bottle()

class Game(object):
    def __init__(self, name, title):
        with open(os.path.join(gamedir, name+'.plot')) as fp:
            source = fp.read()
            self.graph = choice.parse(source)
        self.current = self.graph
        self.name = name
        self.title = title

    def get_text(self):
        return self.current.text

    def get_html(self):
        return '<p>'+self.current.text.strip().replace('\n\n','</p><p>')+'</p>'

    def get_choices(self):
        return [(i, c[1]) for i, c in enumerate(self.current.choices)]

    def choice(self, num):
        try:
            self.current = self.current.choices[int(num)][0]
        except IndexError:
            return None
        while not self.current.text and len(self.current.choices) == 1:
            self.current = self.current.choices[0][0]

@app.get('/')
@bottle.view('index')
def index():
    return dict(games=games)

@app.post('/')
@bottle.view('index')
def newgame():
    game = bottle.request.forms.get('game')
    if game not in games:
        return dict(error='not-a-game', game=game, games=games)
    game = Game(game, games[game])
    uid = id(game)
    sessions[uid] = game
    bottle.redirect('/game/%d' % uid)

@app.get('/game/:uid#[0-9]+#')
@bottle.view('scene')
def proceed(uid):
    uid = int(uid)
    if uid not in sessions:
        bottle.abort(404, "Game not found")
    game = sessions[uid]
    choice = bottle.request.GET.get('choice')
    if choice and choice.isdigit():
        game.choice(int(choice))
        bottle.redirect('/game/%d' % uid)
        
    return dict(game=game)

@app.get('/main.css')
def css():
    return bottle.static_file('main.css','static')

if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0')
else:
    application = app