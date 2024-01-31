import functools

user = {'username': 'abdul',
        'access_level': 'admin'}


def make_secure(func):
    """Wrapping decorator should come before nested
    function definition. This @wrap is used almost
    in every decorator."""

    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"
    return  secure_function

@make_secure
def get_password(panel):
        if panel == 'admin':
                return '1234'
        elif panel == 'billing':
                return 'SUPER SECURE PASSWORD'

print(get_password('billing'))