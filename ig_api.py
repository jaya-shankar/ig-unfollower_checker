

from instagram_private_api import Client
import os

def get_unfollowers(username, password):
    print("Authenticating....")
    myProfile=Client(auto_patch=True, authenticate=True,username=username, password=password)
    print("Authenticated")

    user_id=myProfile.authenticated_user_id

    followers=myProfile.user_followers(user_id=user_id,rank_token=myProfile.generate_uuid())

    following=myProfile.user_following(user_id=user_id,rank_token=myProfile.generate_uuid())

    followers=followers["users"]
    followers_username=[]
    for i in followers:
        followers_username.append(i["username"])

    following_username=[]
    following=following["users"]
    for i in following:
        following_username.append(i["username"])

    result=[]
    print("followers"+str(len(followers_username)))

    print("following"+str(len(following_username)))



    for f in following_username:
        if f not in followers_username:
            result.append(f)
