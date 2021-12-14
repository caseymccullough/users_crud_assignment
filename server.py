from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", all_users = users)

@app.route("/user/new")
def new():
    return render_template('new_user.html') # doesn't exist yet.

@app.route("/user/create", methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route("/user/<int:id>")
def showOne(id):
    data = { "id": id}
    user = User.get_one(data)
    print ("user inside showOne")
    print(user)
    return render_template("single_user.html", user = user)

@app.route("/user/edit/<int:id>")
def editOne(id):
    data = {"id": id}
    user = User.get_one(data)
    print("user in editOne", user)
    return render_template("edit_user.html", user = user)

@app.route("/user/update", methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')
    
@app.route("/user/delete/<int:id>")
def deleteOne(id):
    data = {
        "id": id
        }
    result = User.destroy(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)
