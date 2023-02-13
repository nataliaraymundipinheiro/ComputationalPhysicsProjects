#######################
# Libraries and Files #
#######################

# Libraries
import numpy as np


######################
# Function defintion #
######################

# Take in a string of a binary number and turn it
# into a decimal number:
def binaryToInt(number):
    binary = int(number, 2)
    return binary
    

# Take a certain list or np.array representing a state
# and print it in a prettier, more readable way (with binary):
def prettyPrintBinary(state):
    # If state is empty:
    if (len(state) == 0):
        return '(  )'
    
    # Find out how many wires there are:
    numberOfWires = len(state[0][1])
    

    prettyPrint = '( '
    count = len(state)
    for element in state:
        count -= 1
        if (element[0] != 0.0 and count > 0):
            prettyPrint += str(element[0]) + '  |' + element[1] + '> + '
       
        if (count == 0):
            prettyPrint += str(element[0]) + '  |' + element[1] + '>'

    prettyPrint += ' )'
    
    return prettyPrint


# Take a certain list or np.array representing a state
# and print it in a prettier, more readable way (with integers):
def prettyPrintInteger(state):
    # If state is empty:
    if (len(state) == 0):
        print("State length is zero. Nothing to be done here.")
        return '(  )'
    
    
    prettyPrint = '( '
    count = len(state)
    for element in state:
        count -= 1
        if (element[0] != 0.0 and count > 0):
            prettyPrint += str(element[0]) + '  |' + \
                    str(binaryToInt(element[1])) + '> + '
                
        if (count == 0):
            prettyPrint += str(element[0]) + '  |' + \
                    str(binaryToInt(element[1])) + '>'

    prettyPrint += ' )'
    
    return prettyPrint


state = [(np.sqrt(0.1)*1.j,'101'),(np.sqrt(0.5), '000'),(-np.sqrt(0.4), '010')]
print(prettyPrintInteger(state))
