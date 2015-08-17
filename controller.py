__author__ = 'User'

from league_model import LeagueModel

lm = LeagueModel()
lm.set_abilities_file(lm.read_file("Abilities.txt"))

# Debugging:
for a in lm.get_all_abilities():
    # print(a)
    pass
print("\r")

lm.add_league("Buffalo")

lm.get_current_league().add_character("L", char_type="Leader", health="d10", brawl="2d10", shoot="3d10", dodge="3d8",
                                      might="3d10", finesse="2d10", cunning="2d8", arg1="Mighty", arg2="Brash",
                                      arg3="Crafty")
print("\r")

lm.get_current_league().add_character("J", char_type="SideKick", health="d6", brawl="2d6", shoot="3d6", dodge="2d6",
                                      might="3d8", finesse="2d8", cunning="3d8", arg1="Mighty", arg2="Brash")
print("\r")
lm.get_current_league().add_character("W", char_type="Follower", health="d6", brawl="1d6", shoot="1d6", dodge="1d6",
                                      might="1d6", finesse="1d6", cunning="1d6", arg1="Mighty", arg2="",
                                      arg3="")
print("\r")
j = lm.get_current_league().find_character("J")
w = lm.get_current_league().find_character("W")

# Testing export strings array
print("League export")
print(lm.export_league())
#print(lm.get_current_league().find_character("J").export_character())
print(j.export_character())

if j is not None:
    print("Some of " + str(j) + "'s skills and abilities:")
    print("Health: " + j.get_health().get_number_dice() + j.get_health().get_dice_type().name)
    print("Brawl: " + j.get_brawl().get_number_dice() + j.get_brawl().get_dice_type().name)
    print("Might: " + j.get_might().get_number_dice() + j.get_might().get_dice_type().name)
    print("Ability 1: " + j.get_ability_1().get_name())

    print("\r")
    print("League name: " + j.get_my_league().get_name())
    # the above line is the same as: print(lm.get_current_league())

    print("\r")
    print("Character name = " + str(j))
    print("\r")

    print(str(j) + "'s abilities:")
    for abili in j.get_abilities():
        print(abili.get_name())
    print("\r")

    l = lm.get_current_league()
    l.char_remove_ability("Brash", "J")
    print("\r")

    l.char_add_ability("Mighty", "J")
    print("\r")

    print(str(j) + "'s abilities:")
    for abili in j.get_abilities():
        print(abili.get_name())
    print("\r")

    l.char_add_ability("Sharp", "J")
    print("\r")

    print(str(j) + "'s abilities:")
    for abili in j.get_abilities():
        print(abili.get_name())
    print("\r")

    l.char_add_ability("Clever", "J")
    print("\r")
    print(str(j) + "'s abilities:")
    for abili in j.get_abilities():
        print(abili.get_name())
    print("\r")

if j is not None and w is not None:
    # Interesting test (if two characters add the same ability):
    if j.get_ability_1 is w.get_ability_1:
        print("The instances of " + j.get_ability_1().get_name() + " and " + w.get_ability_1().get_name() + " for " +
              str(j) + " and " + str(w) + " are the same")

    else:
        print("The instances of " + j.get_ability_1().get_name() + " and " + w.get_ability_1().get_name() + " for " +
              str(j) + " and " + str(w) + " are different.")



# if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
