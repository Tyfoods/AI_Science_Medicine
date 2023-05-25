from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

system_state = {
    'water_pump': False,
    'air_pump': False,
}

def htmldoc(water_pump_status, air_pump_status):
    return f'''
        <html>
            <head>
                <title>Aquaponics System Control</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                    }}
                    h1 {{
                        background-color: #4CAF50;
                        color: white;
                        padding: 20px;
                    }}
                    .container {{
                        padding: 20px;
                    }}
                    button {{
                        border: none;
                        color: white;
                        padding: 10px 20px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 10px 2px;
                        cursor: pointer;
                        border-radius: 4px;
                        width: 200px;
                    }}
                    .on {{
                        background-color: #4CAF50;
                    }}
                    .on:hover {{
                        background-color: #45a049;
                    }}
                    .off {{
                        background-color: #f44336;
                    }}
                    .off:hover {{
                        background-color: #da190b;
                    }}
                </style>
            </head>
            <body>
                <h1>Aquaponics System Control</h1>
                <div class="container">
                    <a href="/toggle/water_pump">
                        <button class="{('on' if water_pump_status == 'ON' else 'off')}" style="width:200px;">
                            Water Pump: {water_pump_status}
                        </button>
                    </a>
                    <br>
                    <a href="/toggle/air_pump">
                        <button class="{('on' if air_pump_status == 'ON' else 'off')}" style="width:200px;">
                            Air Pump: {air_pump_status}
                        </button>
                    </a>
                </div>
            </body>
        </html>
    '''

@app.route('/')
def control(request):
    return htmldoc(
        'ON' if system_state['water_pump'] else 'OFF',
        'ON' if system_state['air_pump'] else 'OFF'
    )

@app.route('/toggle/<component>')
def toggle(request, component):
    system_state[component] = not system_state[component]
    return htmldoc(
        'ON' if system_state['water_pump'] else 'OFF',
        'ON' if system_state['air_pump'] else 'OFF'
    )

app.run(debug=True, port=8008)