import os
import sys
import random, string
def percent(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    percentage = '{0:.2f}'.format((num1 / num2 * 100))
    return percentage
print("::::    ::: ::::::::::: ::::::::::: :::::::::   ::::::::    ::::::::  :::::::::: ::::    :::")
print(":+:+:   :+:     :+:         :+:     :+:    :+: :+:    :+:  :+:    :+: :+:        :+:+:   :+:")
print(":+:+:+  +:+     +:+         +:+     +:+    +:+ +:+    +:+  +:+        +:+        :+:+:+  +:+")
print("+#+ +:+ +#+     +#+         +#+     +#++:++#:  +#+    +:+  :#:        +#++:++#   +#+ +:+ +#+")
print("+#+  +#+#+#     +#+         +#+     +#+    +#+ +#+    +#+  +#+   +#+# +#+        +#+  +#+#+#")
print("#+#   #+#+#     #+#         #+#     #+#    #+# #+#    #+#  #+#    #+# #+#        #+#   #+#+#")
print("###    #### ###########     ###     ###    ###  ########    ########  ########## ###    ####")
print("")
print("Welcome to the random nitro code generator!")
print("Press enter to start...")
print("_______________________________________________________________________________________")
enter = input("")
if enter == "":
    amount = int(input("How many codes do you want?: "))
    linkadd = input("Should we add \"https://discord.gift/\" to the beggining? (Y or N): ")
    clear = input("Should we clear codes.txt first? (Y or N): ")
    if clear == "y":
        f = open('codes.txt', 'r+')
        f.truncate(0)
    elif clear == "Y":
        f = open('codes.txt', 'r+')
        f.truncate(0)
    gen = 0
    codestring=""
    while gen != amount: 
        code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        codelink = "https://discord.gift/" + code
        
        if linkadd == "n":
            codestring += code + "\n"
        elif linkadd == "N":
            codestring += code + "\n"
        else:
            codestring += codelink + "\n"

        perc = str(percent(gen,amount))
        perc = perc[:-3]
        print("Generating... " + "(%" + perc + ")                                     " + str(gen) + "/" + str(amount), end='\r')
        gen += 1
    with open("codes.txt", "a") as myfile:
        myfile.write(codestring)
    print("_______________________________________________________________________________________")
    print("All codes have been appended to the codes file. Press enter to close the program.")
    enter = input("")
    if enter == "":
        sys.exit()
