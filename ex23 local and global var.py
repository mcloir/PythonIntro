x = 10 # global var

def function ():
    x = 20 # local var
    print(x)

print(x)
function()
print(x) # the global var did not changed


i = 0

def increment():
    global i # the global word allows to change the value of the global var "i"
    i += 1

increment()
print(i)

def external():
    x = 10
    def internal():
        nonlocal x # nonlocal allows to change the value of the var local of the function.
        x = 20
    
    internal()
    print(x)
external()