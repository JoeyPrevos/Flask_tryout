from flask import Flask
app =
@app.route('/')
def home():
    return "<p>Hello world!</p>"