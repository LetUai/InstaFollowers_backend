from flask import Blueprint, request
import instaloader
import json

L = instaloader.Instaloader()


bp_login = Blueprint('login', __name__)

@bp_login.route('/login', methods=['POST'])
def register():
    username, password = request.json['username'], request.json['password']
    L.login(username,password)
    profile = instaloader.Profile.from_username(L.context, username) 
    followers = set(profile.get_followers()) 
    followers = list(followers)
    seguidores = []

    for i in range(len(followers)): 
        seguidores.append(str(followers[i]).split(' ')[1])
    
    retorno = json.dumps(seguidores)
    return str(retorno)

@bp_login.route('/followers', methods=['GET'])
def get_followers():
    ...

@bp_login.route('/unfollow', methods=['POST'])
def unfollow():
    ...    
