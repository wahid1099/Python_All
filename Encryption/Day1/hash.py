import hashlib


# Rtrams

# smart
# Splkiyoanr
# lion

email='jkr@gmail.com'
pwd='Chairontablewith3legs'
pwd_encode=pwd.encode()
print(pwd_encode)
pwd_hash=hashlib.md5(pwd_encode).hexdigest()
print(pwd_hash)

user_email='Wahid@gmail.com'
user_password='Chairontablewith3legs'


hassed_your_password=hashlib.md5(user_password.encode()).hexdigest()

if email == user_email and pwd_hash == hassed_your_password:
    print("Right user")

else:
    print("Wrong user")


hacker_email="Wahid@gmail.com"
hacker_password="18059cafe9a5a40cd5498cbf241211c6"

print(pwd)
print(pwd_hash)