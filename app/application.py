from flask import Flask,request,render_template
from flask.wrappers import Response
from . import ig_api
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main(name = None):
    if request.method == 'POST':
        
        username = request.form["username"]
        password = request.form["password"]
        profile = ig_api.authenticate(username=username, password=password)
        if profile == {}:
            return "Failure"
        else:
            followers       = ig_api.get_followers(profile)
            followings      = ig_api.get_following(profile)
            unfollowers     = ig_api.get_unfollowers(followings,followers)
            profile.logout()
        return render_template('main.html', users= unfollowers)
        
    else:
        return render_template('main.html', name=name)


