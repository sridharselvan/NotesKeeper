import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='/') 
app.static_folder="static"
app_route = app.route

@app.route('/', defaults={'path': 'index'}, methods=['GET', 'POST'])
@app.route('/<path:path>.html', methods=['GET', 'POST'])
def views(path):
    html_path = 'htmls/{}.html'.format(path)
    return app.send_static_file(html_path)

if __name__ == '__main__':
    app.run(port=4770, debug=True)