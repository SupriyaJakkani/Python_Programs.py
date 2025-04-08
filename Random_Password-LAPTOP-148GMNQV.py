import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w' 'x', 'y', 'z']
numbers = [0,1,2,3,4,5,6,7,8,9]
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']

char_in_password = int(input("how many alphabets you want in your password : "))
number_in_password = int(input("how many numbers you want in your password :"))
special_char = int(input("how many special characters you want : "))

password_list = []

for j in range(1, char_in_password+1):
    ch = random.choice(alphabets)
    password_list.append(ch)
for k in range(1, number_in_password+1):
    num = str(random.choice(numbers))
    password_list.append(num)
for l in range(1, special_char+1):
    sp= random.choice(special_characters)
    password_list.append(sp)

random.shuffle(password_list)
password = "".join(password_list)
print(f'Your Password is [ {password}]')
