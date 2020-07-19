from flask import Blueprint, request, jsonify
from .Api import Insta

bp_login = Blueprint('login', __name__)

@bp_login.route('/login', methods=['POST'])
def register():
    username, password = request.json['username'], request.json['password']
    insta = Insta(username, password)
    insta.login()
    result = insta.get_followers()
    return jsonify({ 'data' : result })

@bp_login.route('/followers', methods=['GET'])
def get_followers():
    username, password = request.json['username'], request.json['password']
    insta = Insta(username, password)
    insta.login()
    result = insta.get_followes_pic()
    return jsonify({ 'data' : result })

@bp_login.route('/unfollow', methods=['POST'])
def unfollow():
    ...    
