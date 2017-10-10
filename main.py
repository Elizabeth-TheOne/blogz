from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build_a_blog:123456@localhost:8889/build_a_blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Colum(db.INteger, primary_key=True)
    title = db.Column(db.String(120))

@app.route('/newpost', methods=['GET', 'POST'])

def add_blog():
    return render_template('')


@app.route('/blog', methods=['POST', 'GET'])
def index():
    if request.args:
        blog_id = request.args.get("id")
        blog = Blog.query.get(blog_id)

        return render_template('blogentry.html, blog=blog')
    else:
        blogs = Blog.query.all()
        
        return render_template('blog.html')

    
    tasks = Task.query.filter_by(completed=False).all()
    completed_tasks = Task.query.filter_by(completed=True).all()
    return render_template('todos.html',title="Get It Done!", 
        tasks=tasks, completed_tasks=completed_tasks)


@app.route('/delete-task', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')
if not title_error and not body_error:
    new_blog = Blog(blog_title, blog_body
    db.session.sdd(new_blog)
    db.session.commit()
    query_parm_url = "/blog?id+" +str(new_blog.id)
    return redirect(query_parm_url)

if __name__ == '__main__':
    app.run()