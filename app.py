from flask import Flask, request, redirect, url_for, render_template
from models import db, Meme, Gif, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repository.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    memes = Meme.query.all()
    gifs = Gif.query.all()
    messages = Message.query.all()
    return render_template('index.html', memes=memes, gifs=gifs, messages=messages)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'meme' in request.files:
            meme = request.files['meme']
            db.session.add(Meme(content=meme.read().decode('utf-8')))
        if 'gif' in request.files:
            gif = request.files['gif']
            db.session.add(Gif(content=gif.read().decode('utf-8')))
        if 'message' in request.form:
            message = request.form['message']
            db.session.add(Message(content=message))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
