from microdot import Microdot
app = Microdot()

@app.route('/')
def index(request):
    return 'Hello, everyone!'

@app.route('/mpcr')
def index(request):
    return 'Hello, MPCR Lab Researchers!'

@app.route('/sandbox')
def index(request):
    return 'Hello, MPCR Sandbox Researchers!'

app.run(debug=True, port=8008)

