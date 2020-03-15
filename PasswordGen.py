import sys
import random
def verify():
	if(True):
		quit()
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
n=int(input("Number of characters in you password?(higher than 6)"))
x=0;
password=""
while(x<=n):
	password+=random.choice(chars)
	x+=1
print(password)
verify()
