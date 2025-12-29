import json
import time
import random

try:
    with open('data.json', 'r') as f:
        data=json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data=[]



def main():
    while True:
        print('Sign up : 1, Log in : 2')
        choice=input('Enter your choice: ').strip()
        if choice=='1':
            signup()
        elif choice=='2':
            login()
        else:
            print('Invalid choice')



def signup():
    print('SignUp')
    email=valid_email()
    username=valid_username()
    password=valid_password()
    while True:
        password_test=input("Enter password again: ").strip()
        if password!=password_test:
            print('Password not matched\nTry again')
            continue
        else:
            data.append({'email': email,
                         'username': username,
                         'password': password})
            break

    print('Registered')

    data_save()

    return

def login():
    while True:
        print('Login')
        username_inp=input('Username: ').strip()
        for dic in data:
            if dic['username']!=username_inp:
                continue
            password_check(dic)
            return
        else:
            print('User does not exist')
            continue

def password_check(dic):
    while True:
        print('Forgot password? press 1')
        password_inp = input('Password: ')
        if password_inp=='1':
            reset_password(dic)
            return
        elif password_inp!=dic['password']:
            print('Invalid password')
            continue
        else:
            print('ACCESS ALLOWED')
            logged_in(dic)
            return

def valid_username():
    while True:
        problems=[]
        name=input('Create username: ').strip()
        if any(name==dic['username'] for dic in data):
            print('Username already taken')
            continue
        if ' ' in name:
            problems.append('not contain spaces')
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

def valid_password():
    while True:
        problems=[]
        code=input('Create password: ').strip()
        if len(code)!=8:
            problems.append('8 characters')
        if ' ' in code:
            problems.append('not contain spaces')
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

        email=input('Enter your email: ').strip()
        if any(email == dic['email'] for dic in data):
            print('Email already registered')
            continue
        if ' ' in email:
            print('Invalid email')
            continue
        if email.count('@')!=1:
            print('Invalid email')
            continue
        name,domain=email.split('@')
        if not name:
            print('Invalid email')
            continue
        if '.' not in domain:
            print('Invalid email')
            continue
        domain=domain.split('.')
        if len(domain)==2:
            if domain[0] in email_providers and domain[1] in domains:
                return email
            else:
                continue
        elif len(domain)==3:
            if domain[0] in email_providers and '.'.join(domain[1:3]) in domains:
                return email
            else:
                continue

def reset_password(dic):
    if otp_system(dic):
        while True:
            new_password=valid_password()
            new_password_test=input('Enter password again: ').strip()
            if new_password_test!=new_password:
                print('Passwords not matched\nPlease try again')
                continue
            else:
                dic['password'] = new_password
                print('Password reset successfully')
                break

    data_save()

def otp_system(dic):
    while True:
        print(f'OTP sent on {dic["email"]}')
        otp=generate_otp()
        if otp_check(otp):
            return True

        restart=input('Resend OTP? [y/n]: ')
        if restart == 'y':
            continue
        else:
            return False

def generate_otp():
    otp=random.randint(1000, 9999)
    print(f'OTP: {otp}')
    return otp

def otp_check(otp):
    time_start=time.time()
    for _ in range(3):
        try:
            otp_test=int(input('Enter OTP: '))
            time_end=time.time()
            if time_end>time_start+10:
                print('otp expired\nTry again')
                return False
            if otp_test==otp:
                print('OTP verified')
                return True
            else:
                print('Incorrect OTP')
                continue
        except ValueError:
            print('Incorrect input')
    else:
        print('Too many incorrect OTP attempts')
        return False

def logged_in(dic):
    while True:
        print('''====== ACCOUNT INFO ======''')
        print('Delete account: 1\nLog out: 2')
        choice=input('Enter your choice: ').strip()
        if choice=='1':
            if delete_acc(dic):
                return
            else:
                continue
        elif choice=='2':
            return
        else:
            print('Invalid choice')
            continue

def delete_acc(dic):
    print('Do you really wanna your Delete account? [y/n]: ')
    choice=input('Enter your choice: ').strip().lower()
    if choice=='y':
        while True:
            password=input('Enter your password: ').strip()
            if password==dic['password']:
                data.remove(dic)
                data_save()
                print('Account delete successfully')
                return True
            else:
                print('Incorrect password')
    else:
        return

def data_save():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
        main()



