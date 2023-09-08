from flask import Flask, render_template
import random

app = Flask(__name__)

#Routes HTML
@app.route('/')
@app.route('/index')
def index():
    random_number = random.randint(1, 1000)
    return render_template('index.html', random_number = random_number)

#Routes End
if __name__ == "__main__":
    app.debug = True
    app.run()
