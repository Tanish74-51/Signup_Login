import json

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

def main():
    print('Sign up : 1, Log in : 2')
    choice=input('Enter your choice: ')
    if choice=='1':
        signup()
    elif choice=='2':
        login()

    else:
        print('Invalid choice')



def signup():
    print('SignUp')
    email = valid_email()
    username = valid_username()
    password = valid_password()
    while True:
        password_test = input("Enter password again: ")
        if password == password_test:
            data.append({'email': email, 'username': username, 'password': password})
            break
        else:
            print('''Password not matched
    Try again''')

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print('Signed in')

def login():
    print('Login')
    while True:
        try:
            username_inp = input('Username: ')
            for dic in data:
                if dic['username'] == username_inp:
                    password_inp = input('Password: ')
                    if password_inp == dic['password']:
                        print('ACCESS ALLOWED')
                        break
                    else:
                        raise ValueError('Invalid password')
            else:
                raise ValueError('User does not exist')
            break
        except ValueError as e:
            print(e)
            continue




def valid_password():
    while True:
        problems=[]
        code=input('Create password: ')
        if len(code)!=8:
            problems.append('8 characters')
        if not any(ch.isalpha() for ch in code):
            problems.append('Alphabets')
        if not any(ch.isupper() for ch in code):
            problems.append('Uppercase alphabets')
        if not any(ch.isdigit() for ch in code):
            problems.append('Digits')
        if not any(ch in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~' for ch in code):
            problems.append('Special characters')
        if problems:
            print('Password must have '+', '.join(problems))
            continue
        else:
            return code

def valid_username():
    while True:
        problems = []
        name = input('Create username: ')
        if any(name==dic['username'] for dic in data):
            print('Username already taken')
            continue
        if not 4<=len(name)<=8:
            problems.append('4 to 8 characters')
        if not any(ch.isalpha() for ch in name):
           problems.append('at least one alphabets')
        if any(ch.isdigit() for ch in name):
            pass
        if any(ch in '!"#$%&\'()*+,/:;<=>?@[]^`{|}~' for ch in name):
            problems.append('only "_","-" or "."')
        if problems:
            print('Username must have ' + ', '.join(problems))
            continue
        else:
            return name

def valid_email():
    domains=[
        "com",
        "net",
        "org",
        "edu",
        "gov",
        "in",
        "uk",
        "us",
        "ca",
        "au",
        "co.in",
        "ac.in",
        "gov.in",
        "dev",
        "io",
        "tech",
        "ai",
        "app",
        "store",
    ]
    email_providers=[
        "gmail",
        "googlemail",
        "yahoo",
        "outlook",
        "hotmail",
        "live",
        "icloud",
        "aol",
        "protonmail",
        "zoho",
        "yandex",
        "mail",
        "gmx",
        "chitkara"
    ]
    while True:
        try:
            email = input('Enter your email: ')
            if email.count('@')!=1:
                raise ValueError
            name,domain=email.split('@')
            if not name:
                raise ValueError
            if '.' not in domain or domain.count('.')>2:
                raise ValueError
            domain= domain.split('.')
            if len(domain)==2:
                if domain[0] in email_providers and domain[1] in domains:
                    return email
                else:
                    raise ValueError
            elif len(domain)==3:
                if domain[0] in email_providers and '.'.join(domain[1:3]) in domains:
                    return email
                else:
                    raise ValueError
        except ValueError:
            print('Invalid email')
            continue




main()



