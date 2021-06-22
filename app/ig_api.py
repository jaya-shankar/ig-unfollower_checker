

from instagram_private_api import Client
from instagram_private_api.errors import ClientLoginError
import os

def authenticate(username, password):
    try:
        myProfile=Client(auto_patch=True, authenticate=True,username=username, password=password)
    except ClientLoginError :
        return {}

    return myProfile

def get_followers(myProfile):
    user_id = myProfile.authenticated_user_id
    followers = myProfile.user_followers(user_id=user_id,rank_token=myProfile.generate_uuid())
    unverified_followers=[]
    for follower in followers["users"]:
        if not follower["is_verified"]:
            unverified_followers.append(follower)

    return unverified_followers

def get_following(myProfile):
    user_id     = myProfile.authenticated_user_id
    following   = myProfile.user_following(user_id=user_id,rank_token=myProfile.generate_uuid())
    unverified_following=[]
    for following in following["users"]:
        if not following["is_verified"]:
            unverified_following.append(following)

    return unverified_following

def get_unfollowers(followings,followers):
    unfollowers = []
    count       = 1
    followings_ids  = []
    followers_ids   = []
    for following in followings:
        followings_ids.append(following["pk"])
    for follower in followers:
        followers_ids.append(follower["pk"])

    for i in range(len(followings_ids)):
        if followings_ids[i] not in followers_ids:
            following["num"] = count
            followings[i]["num"] = count
            unfollowers.append(followings[i])
            count+=1
    return unfollowers