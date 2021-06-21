from flask import Flask,request,render_template
import ig_api
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main(name = None):
    if request.method == 'POST':
        print(request.args)
        pass
    else:
        return render_template('main.html', name=name)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        ig_api.get_unfollowers(username = username, password = password)
        return "Success"
    else:
        return "get in result"