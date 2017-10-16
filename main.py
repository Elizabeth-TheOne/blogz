from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:123456@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(50))
    body = db.Column(db.String(100))

    def __init__(self, title, body, owner):
        self.title = title
        self.body = body  
        self.owner = owner  

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    blogs = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

@app.route('/blog')
def display_blog():

    if request.args:
        blog_id = request.args.get("id")
        blog = Blog.query.get(blog_id)
        return render_template('blogentry.html', page_title="Blog Entry", blog=blog)

    else:
        blogs = Blog.query.all()
        
        return render_template('blog.html', blogs=blogs)
        
@app.route('/newpost', methods=['GET', 'POST'])
def add_post():
    if request.method == 'GET':
         return render_template('newpost.html')

    if request.method == 'POST':    
        title = request.form['title']
        body = request.form['body']
        session = [username, blog]
        title_error = ""
        body_error = ""

        if title == "":
            title_error = "Put some words in Title field" 
        if body == "":
            body_error = "Put some words in the Blog field"    

        if not title_error and not body_error:
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()
            query_param_url = "/blog?id=" + str(new_blog.id)    
            return redirect(query_param_url)
        else:
            return render_template('newpost.html', title_error=title_error, body_error=body_error)        

if __name__ == '__main__':
    app.run()