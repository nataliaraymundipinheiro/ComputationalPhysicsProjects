#######################
# Libraries and Files #
#######################

# Libraries
import numpy as np

# Files
from diracNotation.prettyPrint import binaryToInt


######################
# Function defintion #
######################

# Take in a number and turn it into a binary:
def prettyBinary(number, numberOfWires):
    binary = bin(number)
    binary_str = str(binary)
    binary_str = binary_str.replace('0b', '')

    while len(binary_str) < numberOfWires:
        binary_str = '0' + binary_str
    
    # Return binary string.
    return binary_str


# Representations:
    # Example: (√0.1 * 00) + (0 * 01) + (0 * 10) + (√0.9 * 11)
    # State: list of tuples
        # [(√0.1, '00'), (0, '01'), (0, '10'), (√0.9, '11')]
    # Vector: np.ndarray of ints
        # [√0.1, 0, 0, √0.9]

# Turns state into vector form
def stateToVector(state):
    if (len(state) == 0):
        return  []
    
    vector = []
    numberOfWires = len(state[0][1])

    unordered = []
    for element in state:
        unordered.append((element[0], binaryToInt(element[1])))
    
    unordered = sorted(unordered, key=lambda x: x[1])

    count = 0
    for element in unordered:
        while (count != element[1]):
            vector.append(0.0)
            count += 1
            
        vector.append(element[0])
        count += 1
    
    while (count < (2 ** numberOfWires)):
        vector.append(0.0)
        count += 1
    
    return vector
    

# Turns vector into state form
def vectorToState(vector):
    state = []
    numberOfWires = np.log(len(vector)) / np.log(2)
    
    count = 0
    for element in vector:
        amplitude = element
        binary = prettyBinary(count, numberOfWires)
        
        if (amplitude != 0.0):
            pair = (amplitude, binary) # tuple
            state.append(pair)
        
        count += 1
        
    return state
    