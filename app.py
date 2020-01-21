# The entry file
from flask import Flask, render_template
from data import Articles

# to render html templates, Flask automatically looks fro the specified file in the 'templates'folder

# creat an instance of the Flask class. initiate the app.
# name is like a placeholder for the current module (app.py in this case)
app = Flask(__name__)

# put the app in debug mode. no need to restart the server everytime a chnage is made.
app.debug = True

# dummy data
article_items = Articles()

# create routes
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def articles():
  # pass on data to template
    return render_template('articles.html', articles=article_items)


@app.route('/article/<string:id>/')
def article(id):
  # pass on data to template
    return render_template('article.html', id=id)


# run this file
if __name__ == '__main__':
    app.run()
