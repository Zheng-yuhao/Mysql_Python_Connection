"""
The view
"""
from interface import login_registration_interface as li


# login-interface
def login():
    print('The login function is working >>> ')
    user = input('Type your user_id >>> : ').strip()
    pwd = input('Type your password >>> : ').strip()
    flag, msg = li.login_interface(user,pwd)
    if flag:
        print(msg)
    else:
        print(msg)

# Registration-interface
def register():
    print('Registration function is working >>> ')
    user = input('Type your user_id >>> : ').strip()
    pwd = input('Type your password >>> : ').strip()
    flag,msg = li.registration_interface(user,pwd)
    if flag:
        print(msg)
    else:
        print(msg)




dicts = {
    '0': login,
    '1': register
}


def run():
    while True:
        print('=' * 10)
        print('Welcome to the login and registration system')
        print('=' * 20)

        choice = input('Please choose the service by typing a number(0 or 1) >>> : ').strip()
        if not choice.isdigit():
            print('Error,please type the number.')
            continue
        dicts[choice]()
