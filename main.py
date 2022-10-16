def main():
    height = get_height()
    for i in range(height):
        print("#")


#get hight adjusted 
def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0:
            return n
        
    
main()