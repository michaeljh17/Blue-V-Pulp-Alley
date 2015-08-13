__author__ = 'User'

from league_model import LeagueModel

lm = LeagueModel()
lm.set_abilities_file(lm.read_file("abilities.txt"))

# Debugging:
for a in lm.get_all_abilities():
    # print(a)
    pass

lm.add_league("Buffalo")
lm.get_current_league().add_character("J", char_type="SideKick", health="d6", brawl="2d6", shoot="3d6", dodge="2d6",
                                      might="3d8", finesse="2d8", cunning="3d8", arg1="Mighty", arg2="Brash",
                                      arg3="")
print("\r")
c = lm.get_current_league().find_character("J")
if c is not None:
    print("Some of " + str(c) + "'s skills and abilities:")
    print("Health: " + c.get_health().get_number_dice() + c.get_health().get_dice_type().name)
    print("Brawl: " + c.get_brawl().get_number_dice() + c.get_brawl().get_dice_type().name)
    print("Might: " + c.get_might().get_number_dice() + c.get_might().get_dice_type().name)
    print("Ability 1: " + c.get_ability_1())

    print("\r")
    print("League name: " + c.get_my_league().get_name())
    # print(lm.get_current_league())

    c = lm.get_current_league().find_character("J")
    print("\r")
    print("Character name = " + str(c))
    print("\r")

    print(str(c) + "'s abilities:")
    for abili in c.get_abilities():
        print(abili.get_name())
    print("\r")

    l = lm.get_current_league()
    l.char_remove_ability("Brash", "J")
    print("\r")

    print(str(c) + "'s abilities:")
    for abili in c.get_abilities():
        print(abili.get_name())
    print("\r")

    l.char_add_ability("Sharp", "J")
    print("\r")

    print(str(c) + "'s abilities:")
    for abili in c.get_abilities():
        print(abili.get_name())
    print("\r")

    l.char_add_ability("Clever", "J")
    print("\r")

    print(str(c) + "'s abilities:")
    for abili in c.get_abilities():
        print(abili.get_name())
