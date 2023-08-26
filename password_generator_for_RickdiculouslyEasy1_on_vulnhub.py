import string

Band_name = ("The", "Flesh", "Curtains")

letter = list(string.ascii_uppercase[0:26])
digit = range(0, 10)

for Band in Band_name :
        for letters in letter :
                for digits in digit :
                        print(letters+str(digits)+Band)
