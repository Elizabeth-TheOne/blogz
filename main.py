from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build_a_blog:123456@localhost:8889/build_a_blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    title = db.Column(db.String(100))

def _init_(self, title, body):
    self.title = title
    self.body = body    

@app.route('/blog', methods=['POST', 'GET'])
def index():
    if request.args:
        blog_id = request.args.get("id")
        blog = Blog.query.get(blog_id)

        return render_template('blogentry.html, blog=blog')
    else:
        blogs = Blog.query.all()
        
        return render_template('blog.html')
        
@app.route('/newpost', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'GET':
         return render_template('newpost.html', title=add_blog_entry)

    if request.method == 'POST':    
        blog_title = request.form('title')
        blog_body = request.form('body')
        title_error = ""
        body_error = ""

    if len(blog_title) < 1:
        title_error = "Invalid Title"

    if len(blog_body) < 1:
        body_error = "Invalid Body"
   
@app.route('/delete-task', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')

    if not title_error and not body_error:
        new_blog = Blog(blog_title, blog_body)
        db.session.sdd(new_blog)
        db.session.commit()
        query_parm_url = "/blog?id+" + str(new_blog.id)    
        return redirect(query_parm_url)

    if __name__ == '__main__':
         app.run()