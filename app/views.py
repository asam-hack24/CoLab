from app import app
from flask import Flask, session, redirect, url_for, escape, request, Response, render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


messages = ['A','B','C']

@app.route('/get_messages')
def get_messages():
    if request.headers.get('accept') == 'text/event-stream':
        def script():
            #a lot of code goes here
            print(messages)
            while messages:
                yield "data: %s\n\n"%messages.pop(0)

        return Response(script(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))
    
    
@app.route('/send', methods=['POST'])
def send():
    print(request.form['message'])
    messages.append(request.form['message'])
    return ""
