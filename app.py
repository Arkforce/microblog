from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for posts
posts = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    global next_id
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        posts.append({'id': next_id, 'title': title, 'content': content})
        next_id += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
