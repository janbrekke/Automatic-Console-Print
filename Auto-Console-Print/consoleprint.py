###############################################################
# date: 2019/02/19                                            #
# name: Jan Brekke                                            #
# description:                                                #
# Make the print("Hello GITHUB WORLD")                        #
# Function look like it's being typed automatically in        #
# the terminal window                                         #               
#                                                             #
###############################################################
# This function can be used by adding the def function        #
# somewhere in the begining of the code.                      #
# To use it you exchange the "print" word with "consoleprint" #
#                                                             #
# Ex: consoleprint("Hello GITHUB World")                      #
###############################################################

def consoleprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.3) #time is in seconds

print("Watch This..\n\n")
consoleprint("Hello GITHUB World..")