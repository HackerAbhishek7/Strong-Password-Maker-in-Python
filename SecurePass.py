# radhe radhe

# Tuples are unchangable and ordered

Secure = (('and','&'),('o','0'),('a','@'),('1','|'),('i','e'))  #tuple

def makeSecure(password):
    for a,b in Secure:
        password = password.replace(a,b)
    return password

if __name__ == "__main__":

    password = input("Enter Your Desired Password: ")
    passWord = makeSecure(password)
    print(f"Your Secured PassWord Is: {passWord}")