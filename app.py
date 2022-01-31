import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post


def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    return posts


def delete_post(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def draw_main_page():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)

    if post is None:
        abort(404)

    return render_template('post.html', post=post)


def add_post(title, content):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (title, content))
    conn.commit()
    conn.close()


def update_post(title, content, id):
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ?'
                 ' WHERE id = ?',
                 (title, content, id))
    conn.commit()
    conn.close()



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Введите заголовок!')
        else:
            add_post(title, content)
            return redirect(url_for('draw_main_page'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            update_post(title, content, id)
            return redirect(url_for('draw_main_page'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    delete_post(id)
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('draw_main_page'))


if __name__ == '__main__':
    app.run()
