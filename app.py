from flask import Flask, render_template,url_for
App=Flask(__name__)
@App.route('/')
def home():
    return "hello home Page"
@App.route("/Amir")
def index(name="Amir"):
    return name*3
@App.route("/<name>")
def homes(name=None):
    return render_template("/index.html",name="Amir")

if __name__=="__main__":
    App.run(debug=True)

