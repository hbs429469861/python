#!/usr/bin/python


# login
# check 3 input

_USERNAME = "admin"
_USERPWD = "123"

flag =False
for i in range(3):
    username = input("username: ");
    pwd = input("password: ");
    if username.__eq__(_USERNAME) & pwd.__eq__(_USERPWD):
        print("login %s success",username);
        flag = True;
        break;
    else:
        print("invalid username or password")

else:
    print("more 3 login exit")
