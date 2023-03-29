from app import app

@app.route('/home')
def homePage():
    return {
        "Hello Pokemon User": "Welcome!"
    }

@app.route('/')
def landingPage():
    return {
        "Oh hello there": "Clutch"
    }