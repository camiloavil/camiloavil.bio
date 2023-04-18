import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/www", StaticFiles(directory="www"), name='images')

@app.get('/', response_class=HTMLResponse)
def get_root():
    content = open("www/index.html").read()
    return HTMLResponse(content=content)

@app.get("/banner", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <body>
        <img src="www/banner.png">
        </body>
    </html>
    """

@app.get("/logo.png", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <body>
        <img src="www/favicon.png">
        </body>
    </html>
    """


@app.get("/autor", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <img src="www/favicon.png">
        <h1>Camilo Avila</h1>
        </body>
    </html>
    """

@app.get('/credits')
def get_credits():
    return {'autor':'Camilo Avila'}

if __name__== '__main__':
    # print (f'Inicio')
    uvicorn.run(app, host="0.0.0.0", port=8000)
