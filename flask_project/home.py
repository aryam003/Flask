from flask import Flask

app=Flask(__name__)


@app.route('/')
def fun():
    return "welcome"

app.run()