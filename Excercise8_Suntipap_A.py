import time

print("Menu")
print("","                   S","     M","     L")
print("-------------------------------------")
print("- Hot Americano","   60","    80","    100")
print("  Iced Americano","  70","    90","    110")
print("- Hot Cappuccino","  70","    90","    120")
print("  Iced Cappuccino"," 80","    100","   130")
print("- Hot Mocha","       80","    100","   140")
print("  Iced Mocha","      90","    110","   150")
print("-------------------------------------")
print("*This price does not include 10% service charge")
print("-------------------------------------")

usernameinput = input("Username : ")
passwordinput = input("Password : ")
while usernameinput != "s" or passwordinput != "1":
    print("Wrong Username or Password")
    usernameinput = input("Username : ")
    passwordinput = input("Password : ")
else:
    import time
    print("---------------")
    print("SELECT COFFEE")
    print("---------------")
    print("1.Americano")
    print("2.Cappuccino")
    print("3.Mocha")
    print("---------------")
    coffeeinput = int(input("Coffee no. "))
    print("               ")
    print("---------------")
    print("HOT OR ICED ?")
    print("---------------")
    print("1.Hot")
    print("2.Iced")
    print("---------------")
    typeinput = int(input("Hot(1) Iced (2) : "))
    print("               ")
    print("---------------")
    print("SELECT CUP SIZE")
    print("---------------")
    print("1.Small")
    print("2.Medium")
    print("3.Large")
    print("---------------")
    sizeinput = int(input("Size no. "))
    print("               ")
    print("---------------")
    print("HOW MANY CUP?")
    print("---------------")
    amountinput = int(input("Amount : "))
    print("---------------")

    i = 10
    a = 60
    am = 70
    al = 80

    c = 70
    cm = 90
    cl = 120

    m = 70
    mm = 90
    ml = 120
    charge = 10

    # Americano
    if coffeeinput == 1:
        # Hot
        if typeinput == 1:
            print("Hot Americano")
            print("---------------")
            # Size
            if sizeinput == 1:  # Hot Small
                time.sleep(1)
                print("Receipt")
                print("Hot Americano(S)", "x", amountinput, "  : ", a * amountinput)
                print("Service charge 10%     : ", (a * amountinput) * charge / 100)
                print("Total (THB)            : ", a * amountinput + (a * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 2:  # Hot Medium
                time.sleep(1)
                print("Receipt")
                print("Hot Americano(M)", "x", amountinput, "   : ", am * amountinput)
                print("Service charge 10%      : ", (am * amountinput) * charge / 100)
                print("Total (THB)             : ", am * amountinput + (am * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 3:  # Hot Large
                time.sleep(1)
                print("Receipt")
                print("Hot Americano(L)", "x", amountinput, "    : ", al * amountinput)
                print("Service charge 10%       : ", (al * amountinput) * charge / 100)
                print("Total (THB)              : ", al * amountinput + (al * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            else:
                print("Error! wrong input found, plese try again.")
        # Iced
        if typeinput == 2:
            print("Iced Americano")
            print("---------------")
            if sizeinput == 1:  # Small Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Americano(S)", "x", amountinput, "   : ", (a + i) * amountinput)
                print("Service charge 10%       : ", ((a + i) * amountinput) * charge / 100)
                print("Total (THB)              : ", (a + i) * amountinput + ((a + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 2:  # Medium Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Americano(M)", "x", amountinput, "  : ", (am + i) * amountinput)
                print("Service charge 10%      : ", ((am + i) * amountinput) * charge / 100)
                print("Total (THB)             : ", (am + i) * amountinput + ((am + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 3:  # Large Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Americano(L)", "x", amountinput, "  : ", (al + i) * amountinput)
                print("Service charge 10%      : ", ((al + i) * amountinput) * charge / 100)
                print("Total (THB)             : ", (al + i) * amountinput + ((al + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            else:
                print("Error! wrong input found, plese try again.")
        if typeinput > 2:
            print("Error! wrong input found, plese try again.")
    # Cappuccino
    if coffeeinput == 2:
        # Hot
        if typeinput == 1:
            print("Hot Cappuccino")
            print("---------------")
            # Size
            if sizeinput == 1:  # Hot Small
                time.sleep(1)
                print("Receipt")
                print("Hot Cappuccino(S)", "x", amountinput, " : ", c * amountinput)
                print("Service charge 10%     : ", (c * amountinput) * charge / 100)
                print("Total (THB)            : ", c * amountinput + (c * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 2:  # Hot Medium
                time.sleep(1)
                print("Receipt")
                print("Hot Cappuccino(M)", "x", amountinput, "  : ", cm * amountinput)
                print("Service charge 10%      : ", (cm * amountinput) * charge / 100)
                print("Total (THB)             : ", cm * amountinput + (cm * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 3:  # Hot Large
                time.sleep(1)
                print("Receipt")
                print("Hot Cappuccino(L)", "x", amountinput, "   : ", cl * amountinput)
                print("Service charge 10%       : ", (cl * amountinput) * charge / 100)
                print("Total (THB)              : ", cl * amountinput + (cl * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            else:
                print("Error! wrong input found, plese try again.")
        # Iced
        if typeinput == 2:
            print("Iced Cappuccino")
            print("---------------")
            if sizeinput == 1:  # Small Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Cappuccino(S)", "x", amountinput, "  : ", (c + i) * amountinput)
                print("Service charge 10%       : ", ((c + i) * amountinput) * charge / 100)
                print("Total (THB)              : ", (c + i) * amountinput + ((c + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 2:  # Medium Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Cappuccino(M)", "x", amountinput, " : ", (cm + i) * amountinput)
                print("Service charge 10%      : ", ((cm + i) * amountinput) * charge / 100)
                print("Total (THB)             : ", (cm + i) * amountinput + ((cm + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 3:  # Large Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Cappuccino(L)", "x", amountinput, " : ", (cl + i) * amountinput)
                print("Service charge 10%      : ", ((cl + i) * amountinput) * charge / 100)
                print("Total (THB)             : ", (cl + i) * amountinput + ((cl + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            else:
                print("Error! wrong input found, plese try again.")
    # Mocha
    if coffeeinput == 3:
        # Hot
        if typeinput == 1:
            print("Hot Mocha")
            print("---------------")
            # Size
            if sizeinput == 1:  # Hot Small
                time.sleep(1)
                print("Receipt")
                print("Hot Mocha(S)", "x", amountinput, "      : ", m * amountinput)
                print("Service charge 10%     : ", (m * amountinput) * charge / 100)
                print("Total (THB)            : ", m * amountinput + (m * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 2:  # Hot Medium
                time.sleep(1)
                print("Receipt")
                print("Hot Mocha(M)", "x", amountinput, "       : ", mm * amountinput)
                print("Service charge 10%      : ", (mm * amountinput) * charge / 100)
                print("Total (THB)             : ", mm * amountinput + (mm * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 3:  # Hot Large
                time.sleep(1)
                print("Receipt")
                print("Hot Mocha(L)", "x", amountinput, "        : ", ml * amountinput)
                print("Service charge 10%       : ", (ml * amountinput) * charge / 100)
                print("Total (THB)              : ", ml * amountinput + (ml * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            else:
                print("Error! wrong input found, plese try again.")

        # Iced Mocha
        if typeinput == 2:
            print("Iced Mocha")
            print("---------------")
            if sizeinput == 1:  # Small Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Mocha(S)", "x", amountinput, "       : ", (m + i) * amountinput)
                print("Service charge 10%       : ", ((m + i) * amountinput) * charge / 100)
                print("Total (THB)              : ", (m + i) * amountinput + ((m + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 2:  # Medium Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Mocha(M)", "x", amountinput, "      : ", (mm + i) * amountinput)
                print("Service charge 10%      : ", ((mm + i) * amountinput) * charge / 100)
                print("Total (THB)             : ", (mm + i) * amountinput + ((mm + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            elif sizeinput == 3:  # Large Iced
                time.sleep(1)
                print("Receipt")
                print("Iced Mocha(L)", "x", amountinput, "      : ", (ml + i) * amountinput)
                print("Service charge 10%      : ", ((ml + i) * amountinput) * charge / 100)
                print("Total (THB)             : ", (ml + i) * amountinput + ((ml + i) * amountinput) * charge / 100)
                print("---------------")
                print("Enjoy your drinks")
            else:
                print("Error! wrong input found, plese try again.")

    if coffeeinput > 3:
        print("Error! wrong input found, plese try again.")
        if typeinput > 2:
            print("Error! wrong input found, plese try again.")
