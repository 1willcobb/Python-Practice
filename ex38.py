class Player:
    def __init__(self, name):
        self.name = name
        self.pack = [0,2,1]

def test():
    print(Player.pack[2])

will = Player("Will")
savannah = Player("Sav")

print(will)
print(savannah)
savannah.pack[0] = 5
will.pack[0] = 25
print(will.pack)
print(savannah.pack)
test()
