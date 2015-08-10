__author__ = 'User'

from league import League

# s = Skill("Health", EDice.d10, 2)

# print(s.get_skill_name())

# print(s.get_dice_type().name)

# s.set_dice_type(EDice.d6)

# print(s.get_dice_type().name)

# print(s.get_number_dice())

#c = Character("Jeff")
#c.add_skill("health", EDice.d8, 2)
#health = c.get_health()
#print(health.get_number_dice().name)

# c.add_skill("Health", EDice.d6, 2)
# health = c.get_health()
# print(health.get_number_dice().name)

# l = League("Buffalo")
# try:
#    c = l.add_character("J", "Follower", "d6", "1d6", "1d6", "1d6", "1d6", "1d6")
#    if c is not None:
#        print(c.get_health().get_number_dice() + c.get_health().get_dice_type().name)
#        print(c.get_brawl().get_number_dice() + c.get_brawl().get_dice_type().name)
#        print(c.get_might().get_number_dice() + c.get_might().get_dice_type().name)
# except TypeError as e:
#    print(e)

l = League("Buffalo")
c = l.add_character("J", char_type="Follower", health="d6", brawl="1d6", shoot="1d6", dodge="1d6", might="1d6",
                    finesse="1d6", cunning="1d6")
if c is not None:
    print("Health: " + c.get_health().get_number_dice() + c.get_health().get_dice_type().name)
    print("Brawl: " + c.get_brawl().get_number_dice() + c.get_brawl().get_dice_type().name)
    print("Might: " + c.get_might().get_number_dice() + c.get_might().get_dice_type().name)
    print ("League: " + c.get_my_league().get_name())
    print(l)