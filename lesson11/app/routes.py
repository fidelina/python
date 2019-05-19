                      from flask import render_template, redirect
from . import app
from app.models import Post
from app.forms import PostForm
from app import db

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fidelina', 'female': 'woman'}
    list1 = {'str': "One"}
    posts = [
        {
            'author': {'username': 'Марк'},
            'body': 'O, hi, Mark!'
        },
        {
            'author': {'username': 'Боб'},
            'body': 'Совы не то, чем кажутся'
        },
        {
            'author': {'username': 'Билл'},
            'body': 'Помни! Реальность — иллюзия, вселенная — голограмма, скупай золото, пока! '
        }
    ]
    print(Post, type(Post))
    return render_template('index.html', title='Home', user=user, list1=list1,  posts=Post.query.all())


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(title=form.title.data, text=form.text.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/index')

    return render_template('create.html', title='Create', form=form)