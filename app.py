from flask import Flask, render_template

app = Flask(__name__, static_url_path='/Love_files', static_folder='Love_files')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
