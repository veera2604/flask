from models import *

import os

file_name=os.listdir()
print(file_name)



@app.before_request
def create():
    db.create_all()

@app.route("/")
def home():
    return "hello"

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        id=request.form["id"]
        name=request.form["name"]
        email=request.form["email"]
        
        value=Data(id=id,name=name,email=email)
        db.session.add(value)
        db.session.commit()
        
        return "data addedd sussessfull"
        
    return render_template("login.html")

@app.route("/view")
def view():
    
    value=Data.query.all()
    
    return render_template("view.html",value=value)

app.run(debug=True)
