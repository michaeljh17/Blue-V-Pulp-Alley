# __author__ = 'User'

from league_model import LeagueModel
from ViewModel.TableBuilder import TableBuilder


lm = LeagueModel()
lm.set_abilities_file(lm.read_file("Abilities.txt"))

# Debugging:
for a in lm.get_all_abilities():
    # print(a)
    pass
print("\r")

lm.add_league("Buffalo")

lm.get_current_league().add_character("L", char_type="Leader", health="d10",
                                      brawl="3d10", shoot="2d10", dodge="3d8",
                                      might="3d10", finesse="2d10",
                                      cunning="3d8", arg1="Mighty",
                                      arg2="Brash", arg3="Crafty")
print("\r")

lm.get_current_league().add_character("J", char_type="SideKick", health="d8",
                                      brawl="2d6", shoot="3d6", dodge="2d6",
                                      might="3d8", finesse="2d8",
                                      cunning="3d8", arg1="Mighty",
                                      arg2="Brash", arg3="")
print("\r")

lm.get_current_league().add_character("A", char_type="Ally", health="d6",
                                      brawl="2d6", shoot="2d6", dodge="1d6",
                                      might="1d6", finesse="1d6", cunning="1d6",
                                      arg1="Mighty", arg2="",
                                      arg3="")

print("\r")
lm.get_current_league().add_character("W", char_type="Follower", health="d6",
                                      brawl="1d6", shoot="1d6", dodge="1d6",
                                      might="1d6", finesse="1d6", cunning="1d6",
                                      arg1="Mighty", arg2="",
                                      arg3="")
print("\r")
l = lm.get_current_league().find_character("L")
w = lm.get_current_league().find_character("W")

# Testing export strings array
print("League export")
# print(str(lm.export_league()))
tableB = TableBuilder()
tableB.build_table(lm.export_league())
print("\r")

if l is not None:
    print("Some of " + str(l) + "'s skills and abilities:")
    print("Health: " + l.get_health().get_number_dice()
          + l.get_health().get_dice_type().name)
    print("Brawl: " + l.get_brawl().get_number_dice()
          + l.get_brawl().get_dice_type().name)
    print("Might: " + l.get_might().get_number_dice()
          + l.get_might().get_dice_type().name)
    print("Ability 1: " + l.get_abilities()[0].get_name())

    print("\r")
    print("League name: " + l.get_my_league().get_name())
    # the above line is the same as: print(lm.get_current_league())

    print("\r")
    print("Character name = " + str(l))
    print("\r")

    l.replace_ability(l, "Mighty", "Brash")
    print("\r")
    """
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
    """

if l is not None and w is not None:
    print("\r")
    # Interesting test (if two characters add the same ability):
    if l.get_ability_1 is w.get_ability_1:
        print("The instances of " + l.get_abilities()[0].get_name() +
              " and " + w.get_abilities()[0].get_name() + " for " +
              str(l) + " and " + str(w) + " are the same")

    else:
        print("The instances of " + l.get_abilities()[0].get_name() +
              " and " + w.get_abilities()[0].get_name() + " for " +
              str(l) + " and " + str(w) + " are different.")



# if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
