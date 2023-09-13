#Missing opsys -> Russain Roulette
#ONLY RUN THIS IF YOU'RE FEELING LUCKY

# We want to make it clear that ���������� is not responsible for any outcomes, results, or
# consequences that may arise from using our products or services. While we strive to provide accurate
# information and quality services, individual circumstances and choices can significantly impact outcomes.
#------------------------------------------------------------------------------------------------------------
import os
import random

WinSysPath = "C:\Windows\System32"

PlayGame = input("Do you want to play a game? Y/N\n")
PlayGame.capitalize()

if PlayGame == "Yes" or PlayGame == "Y":
    chamber = input("\nWhich chamber would you like to load? 1-6\n")
    LoadedChamber = int(chamber)

    DeadChamber = random.randint(1, 6)

    print("The chamber has been loaded...\n")

    FeelingLucky = input("\nAll that\'s left is pulling the trigger... Y/N\n")
    FeelingLucky.capitalize()

    if FeelingLucky == "Yes" or FeelingLucky == "Y":
        if LoadedChamber != DeadChamber:
            print("*Click* You\'re safe...")
        else:
            os.remove(WinSysPath)
    else:
        print("You\'ve backed out...")
else:
    print("Ending it before it even started.")
