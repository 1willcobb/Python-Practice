weapon_choices = {
	"AXE" : {
		"NAME" : "axe",
		"STRENGTH" : 6,
		"DURABILITY" : 6,
		"RANGE" : 0
	},
	"MACE" : {
		"NAME" : "mace",
		"STRENGTH" : 7,
		"DURABILITY" : 4,
		"RANGE" : 2
	},
	"SWORD" : {
		"NAME" : "sword",
		"STRENGTH" : 6,
		"DURABILITY" : 5,
		"RANGE" : 1
	},
	"LANCE" : {
		"NAME" : "lance",
		"STRENGTH" : 8,
		"DURABILITY" : 2,
		"RANGE" : 4
	},
	"BOW" : {
		"NAME" : "bow",
		"STRENGTH" : 5,
		"DURABILITY" : 5,
		"RANGE" : 10
	},
	"DAGGER" : {
		"NAME" : "dagger",
		"STRENGTH" : 4,
		"DURABILITY" : 7,
		"RANGE" : 0
	},
	"HAMMER" : {
		"NAME" : "hammer",
		"STRENGTH" : 8,
		"DURABILITY" : 8,
		"RANGE" : 2
	},
}

pack = {}

def get_weapon(weapon_index, weapon_number):
	while len(pack) <= weapon_index:
		print("These are your weapon choices")
		for weapon in weapon_choices.keys():
			print(weapon.title())
		weapon_1 = input(f"Choose your {weapon_number} weapon > ")
		if weapon_1.strip().lower() == weapon_choices["AXE"]["NAME"]:
			pack["AXE"] = weapon_choices["AXE"]
		if weapon_1.strip().lower() == weapon_choices["MACE"]["NAME"]:
			pack["MACE"] = weapon_choices["MACE"]
		if weapon_1.strip().lower() == weapon_choices["SWORD"]["NAME"]:
			pack["SWORD"] = weapon_choices["SWORD"]
		if weapon_1.strip().lower() == weapon_choices["LANCE"]["NAME"]:
			pack["LANCE"] = weapon_choices["LANCE"]
		if weapon_1.strip().lower() == weapon_choices["BOW"]["NAME"]:
			pack["BOW"] = weapon_choices["BOW"]
		if weapon_1.strip().lower() == weapon_choices["DAGGER"]["NAME"]:
			pack["DAGGER"] = weapon_choices["DAGGER"]
		if weapon_1.strip().lower() == weapon_choices["HAMMER"]["NAME"]:
			pack["HAMMER"] = weapon_choices["HAMMER"]


'''def Release() :
    while True :
        print('Please select one of the following?\nCompletion = 0\nRelease ID = 1\nVersion ID = 2\nBuild ID = 3\n')
        a = int(input("Please select the type of release required: "))
        if 0 <= a < 4 :
            files(a)
			print("g")
            break
        else :
            print('Try Again')
						

						Trying to figure it out
'''

print(weapon_choices[1])