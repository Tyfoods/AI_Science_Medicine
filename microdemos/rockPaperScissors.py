from microdot import Microdot, Response
import random

app = Microdot()
Response.default_content_type = 'text/html'

# Game state
game_state = {
    'player_score': 0,
    'computer_score': 0,
    'player_choice': None,
    'computer_choice': None,
}

# Game logic
choices = ['rock', 'paper', 'scissors']
def game_logic(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    else:
        return 'computer'

def htmldoc():
    return f'''
        <html>
            <head>
                <title>Rock Paper Scissors</title>
            </head>
            <body>
                <h1>Rock Paper Scissors</h1>
                <p>Player Score: {game_state['player_score']}</p>
                <p>Computer Score: {game_state['computer_score']}</p>
                <p>Player Choice: {game_state['player_choice']}</p>
                <p>Computer Choice: {game_state['computer_choice']}</p>
                <a href="/play/rock">Rock</a>
                <a href="/play/paper">Paper</a>
                <a href="/play/scissors">Scissors</a>
            </body>
        </html>
        '''

@app.route('/')
def home(request):
    return htmldoc()

@app.route('/play/<choice>')
def play(request, choice):
    global game_state
    game_state['player_choice'] = choice
    game_state['computer_choice'] = random.choice(choices)
    result = game_logic(game_state['player_choice'], game_state['computer_choice'])
    if result == 'player':
        game_state['player_score'] += 1
    elif result == 'computer':
        game_state['computer_score'] += 1
    return htmldoc()

app.run(debug=True, port=8008)