from microdot import Microdot, Response
import numpy as np
app = Microdot()
Response.default_content_type = 'text/html'

coin_states = []  # Initialize empty coin_states list

def htmldoc():
    coin_texts = ["Heads" if coin_state == 0 else "Tails" for coin_state in coin_states]

    coins_html = ""
    for i, coin_text in enumerate(coin_texts):
        coins_html += f'''
            <svg width="200" height="200" viewBox="0 0 200 200">
                <a href="/toggle/{i}">
                    <circle style="fill:#000" cx="100" cy="100" r="90" />
                    <text x="50%" y="50%" font-size="24" fill='white' text-anchor="middle" dy=".3em">{coin_text}</text>
                </a>
            </svg>
        '''
    html = f'''
        <html>
            <head>
                <title> Click to Flip Coin </title>
            </head>
            <body>
                <div>
                    <h1> Click the Coin to Flip </h1>
                    <form action="/set_coins" method="post">
                        <label for="num_coins">Number of coins:</label>
                        <input type="number" id="num_coins" name="num_coins" min="1" required>
                        <input type="submit" value="Set">
                    </form>
                    {coins_html}
                </div>
            </body>
        </html>
    '''
    return html

def initCoinState():
    randVal = np.random.random()
    if(randVal > .5):
        return 1
    else:
        return 0

@app.route('/')
def home(request):
    for i in range(len(coin_states)):
        coin_states[i] = initCoinState()
    return htmldoc()

@app.route('/toggle/<int:coin_index>')
def toggle_coin(request, coin_index):
    coin_states[coin_index] = initCoinState()
    return htmldoc()

@app.route('/set_coins', methods=['POST'])
def set_coins(request):
    num_coins = int(request.form['num_coins'])
    global coin_states
    coin_states = [0] * num_coins
    for i in range(num_coins):
        coin_states[i] = initCoinState()
    return htmldoc()

app.run(debug=True, port=8008)
