from flask import Blueprint, g

mod = Blueprint('user', __name__, url_prefix='/user')
# mod = Blueprint('user', __name__, url_prefix='/<user_url_slug>')

# @mod.url_value_preprocessor
# def get_profile_owner(endpoint, values):
#     #query = User.query.filter_by(url_slug=values.pop('user_url_slug'))
#     #g.profile_owner = query.first_or_404()
#     g.user = values.pop('user_url_slug')

# @mod.url_defaults
# def add_language_code(endpoint, values):
#     values.setdefault('demo user', g.user)


@mod.route('/')
def index():
	return g.user

@mod.route('/hello')
def hello():
	return 'hello ' + g.user

@mod.route('/helloworld')
def helloworld():
	return 'hello world ' + g.user
