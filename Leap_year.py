from idlelib.mainmenu import default_keydefs

def is_leap(year: int)-> bool:

    if (year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                leap_year=True

            else:
                leap_year = False

        else:
            leap_year = True

    else:
        leap_year = False


print(is_leap(1990))