#more comments
def main():
    height = get_height()
    for i in range(height):
        print("#")
    print(math(3))


#get hight adjusted 
def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0:
            return n
        

def math(a, b):
    return a * b

def addition(b, c, d):
    return b + c + d
    
main()