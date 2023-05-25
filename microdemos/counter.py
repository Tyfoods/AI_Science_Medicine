from microdot import Microdot, Response
app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc(counter):
    return f'''
        <html>
            <head>
                <title>Counter Demo</title>
            </head>
            <body>
                <div>
                    <h1>Counter: {counter}</h1>
                    <a href="/change/{counter}/1"><button>Increment</button></a>
                    <a href="/change/{counter}/-1"><button>Decrement</button></a>
                </div>
            </body>
        </html>
        '''

@app.route('/')
def home(request):
    return htmldoc(0)

@app.route('/change/<current_counter>/<step>')
def change(request, current_counter, step):
    counter = int(current_counter) + int(step)
    return htmldoc(counter)

app.run(debug=True, port=8008)


# import base64
# import io
# from io import BytesIO
# import numpy as np
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# from microdot_asyncio import Microdot, Response
# app = Microdot()
# Response.default_content_type = 'text/html'


# @app.route("/")
# @app.route("/<points>")
# def hello(request,points = "10"):

#     points = int(points)

#     data = np.random.rand(points, 2)

#     fig = Figure()
#     FigureCanvas(fig)

#     ax = fig.add_subplot(111)

#     ax.scatter(data[:,0], data[:,1])

#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title(f'There are {points} data points!')
#     ax.grid(True)

#     img = io.StringIO()
#     fig.savefig(img, format='svg')
#     #clip off the xml headers from the image
#     svg_img = '<svg' + img.getvalue().split('<svg')[1]
    
    # return svg_img
    
    
# app.run(host="0.0.0.0",port=5000,debug = True)