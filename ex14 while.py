i = 0
while i <= 14:
    print(i)
    i += 1

password = "password"
try0 = ""

while try0 != password:
    try0 = input("Enter the password: ")
    if try0 != password:
        print("Wrong password, bro")
print("Access granted")