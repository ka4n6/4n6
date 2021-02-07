from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from datetime import datetime

app=Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
FLATPAGES_ROOT = 'pages'
POST_DIR = ['articles', 'research', 'resources', 'kannada']
pages = FlatPages(app)

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route("/")
def index():
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('index.html', pages=sorted_pages)

@app.route("/art")
def articles():
    posts = [p for p in pages if "articles" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('articles.html', pages=sorted_pages)


@app.route("/res")
def research():
    posts = [p for p in pages if "research" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('research.html', pages=sorted_pages)


@app.route("/reso")
def resources():
    posts = [p for p in pages if "resources" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('resources.html', pages=sorted_pages)
    


@app.route("/kan")
def kannada():
    posts = [p for p in pages if "kannada" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('kannada.html', pages=sorted_pages)
   

if __name__ == '__main__':
    app.run()