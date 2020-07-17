from flask import Blueprint

bp_login = Blueprint('login', __name__)

@bp_login.route('/login', methods=['POST'])
def register():
    ...

@bp_login.route('/followers', methods=['GET'])
def get_followers():
    ...

@bp_login.route('/unfollow', methods=['POST'])
def unfollow():
    ...    
