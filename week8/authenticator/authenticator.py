import sys
import hashlib
import logging


class User:
    def __init__(self, name, password, admin, login_attempts):
        self.username = name
        self.__password = password

        self.admin = False
        if admin == 'admin':
            self.admin = True
        elif admin != 'standard':
            raise ValueError(f"malformed db record\nprovided: {
                             admin}\nrequired: 'admin' or 'standard'")

        self.__login_attempts = 0
        try:
            self.__login_attempts = int(login_attempts)
        except ValueError:
            raise ValueError(f"malformed db record\nprovided: {
                             login_attempts}\nrequired: integer")

    def authenticate(self, password):
        if self.__login_attempts >= 3:
            return False

        if password == self.__password:
            self.reset_login_attempts()
            return True

        self.__login_attempts += 1
        if self.__login_attempts >= 3:
            logging.warning(f"Locking account of {self.username}")
        return False

    def check_privileges(self):
        print(f"{'admin' if self.admin else 'standard'}")

    def reset_login_attempts(self):
        self.__login_attempts = 0

    def log_activity(self):
        print(f"Here are the logs of {self.username}")


class Database:
    def __init__(self):
        self.file = 'userdb.csv'
        self.current_user = None
        self.options = {
            'help': 'prints this help message',
            'status': 'prints current privilege level',
            'login': 'prompts for username and password',
            'logout': 'switches back to guest accout',
            'exit': 'exits the program'
        }
        self.users = []

        try:
            with open(self.file, 'r') as csv:
                user_records = csv.readlines()
        except FileNotFoundError:
            exit_with_msg(f"File '{self.file}' not found")

        for ur in user_records:
            fields = ur.rstrip().split(",")
            if len(fields) == 4:
                try:
                    new_user = User(*fields)
                    self.users.append(new_user)
                except Exception as e:
                    exit_with_msg(e)
            else:
                exit_with_msg(f"Malformed line in '{self.file}':\n{ur}")

    def logout(self):
        logging.info(f"User {self.current_user.username} logged out")
        self.current_user = None
        print('Logging out...')

    def login(self):
        name = input('Enter your username:')
        password = input('Enter your password:')
        h = hashlib.sha256()
        h.update(password.encode())
        hashed = h.digest().hex()
        for u in self.users:
            if name == u.username:
                if u.authenticate(hashed):
                    print(f"{name} authenticated")
                    self.current_user = u
                    logging.info(
                        f"User {u.username} authenticated successfully"
                    )
                    return True
                else:
                    logging.warning(
                        f"Failed login attempt for user {u.username}"
                    )
                    print('Wrong credentials')
                    return False
        logging.warning('Non-existant user login attempt')
        print('Wrong credentials')
        return False

    def run_repl(self):
        user_input = ''
        while user_input != 'exit':
            prompt_name = "guest"
            prompt_sign = '$'
            if self.current_user is not None:
                prompt_name = self.current_user.username
                if self.current_user.admin:
                    prompt_sign = '#'

            user_input = input(f"{prompt_name}{prompt_sign} ")

            if user_input == 'help':
                for o in self.options:
                    print(o, '\t', self.options[o])
            elif user_input == 'login':
                if self.current_user is not None:
                    print(f"Already logged in as {self.current_user.username}")
                else:
                    self.login()
            elif user_input == 'logout':
                if self.current_user is None:
                    print('Not logged in')
                else:
                    self.logout()
            elif user_input == 'status':
                if self.current_user is None:
                    print('guest')
                else:
                    self.current_user.check_privileges()
            elif user_input != 'exit':
                options = []
                for k in self.options:
                    options.append(k)
                print(
                    f"Invalid command.\nPossible commands are: {options}"
                )

        print('Closing')


def exit_with_msg(message, status=1):
    print(message, file=sys.stderr)
    sys.exit(status)


def main():
    logging.basicConfig(
        filename='auth.log',
        format='%(asctime)s\t[%(levelname)s]\t%(message)s',
        level=logging.INFO
    )
    db = Database()
    db.run_repl()
    sys.exit(0)


main()
