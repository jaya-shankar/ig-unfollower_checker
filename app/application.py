from flask import Flask,request,render_template
from instagram_private_api.errors import ClientThrottledError,ClientError
from flask.wrappers import Response
from . import ig_api
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main(name = None):
    if request.method == 'POST':
        
        username = request.form["username"]
        password = request.form["password"]
        try:
            profile = ig_api.authenticate(username=username, password=password)
        except ClientThrottledError:
            return "Please Try again Later"
        except ClientError: 
            return "Please turn offf two factor authentication and try again"
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


