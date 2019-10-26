from webapp import app

@app.route('/records')
def records():
    return "records"

@app.route('/createbook')
def createbook():
    return "createbook"

@app.route('/info')
def home():
    return "Info"