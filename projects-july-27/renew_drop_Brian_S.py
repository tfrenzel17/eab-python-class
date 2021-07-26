# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random, sys

#initial values
renew = 0
dropped = 0

while True: #main loop for the whole simulation
    print('%s Renewals, %s Drops'%(renew,dropped))  # scoreboard
    while True:
        print('How many input interactions did partner have with EAB?')
        print('(Enter an integer, or "q" to quit)')
        impactInt = input() #player input
        if impactInt == "q":
            print("Quitting the program ...")
            #sys.exit()
            break #I was using sys.exit, but break seems to work just as well.

        # this section checks to see if the input is an integer
        try:
            impactInt = int(impactInt)
            break
        except ValueError:
            print("ERROR: input was not an integer or 'q'")

    #once we've identified the # of input interactions, we set the renewal probability here.
    renew_prob = .3
    if 0 < impactInt < 3:
        renew_prob = .5
    elif 2 < impactInt <5:
        renew_prob = .7
    elif impactInt > 4:
        renew_prob = .8

    # we generate a random number (0,1), and if it is less than our renewal prob, we renew!
    if random.random() <= renew_prob:
        print("RESULT: They Renewed!")
        renew += 1
    else:
        print("RESULT: They dropped. Bummer.")
        dropped += 1
    

