from app import app
@app.route("/dashboard")
def teachers():
    return("This is Dashboard!!")