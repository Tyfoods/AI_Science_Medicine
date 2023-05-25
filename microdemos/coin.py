from microdot import Microdot, Response
import numpy as np
app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc():
    global coin_state
    coin_text = "Heads" if coin_state == 0 else "Tails"
    html = f'''
        <html>
            <head>
                <title> Click to Flip Coin </title>
            </head>
            <body>
                <div>
                    <h1> Click the Coin to Flip </h1>
                    <svg width="200" height="200" viewBox="0 0 200 200">
                        <a href="/toggle">
                            <circle style="fill:#000" cx="100" cy="100" r="90" />
                            <text x="50%" y="50%" font-size="24" fill='white' text-anchor="middle" dy=".3em">{coin_text}</text>
                        </a>
                    </svg>
                </div>
            </body>
        </hmtl>

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
    global coin_state
    coin_state = initCoinState()
    return htmldoc()

@app.route('/toggle')
def toggle_coin(request):
    global coin_state
    coin_state = initCoinState()
    # coin_state = 1 - coin_state
    return htmldoc()

app.run(debug=True, port=8008)