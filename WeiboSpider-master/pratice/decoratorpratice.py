def authenticated(method):
    def wrapper(user,*args):
        if not is_user_valid(user):
            print("redirect to login page")
            return False
        return method(user,*args)
    return wrapper

@authenticated
def buid(user,build_name):
    print("build  "+build_name)
    return


def is_user_valid(user):
    if user == "user":
        return True
    return False

buid("user1","base")