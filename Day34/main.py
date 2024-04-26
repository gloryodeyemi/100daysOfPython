# Python Typing: Type Hints and Arrows
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You can drive.")
else:
    print("You have to pay a fine.")