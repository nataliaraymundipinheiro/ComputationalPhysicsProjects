#######################
# Libraries and Files #
#######################

# Libraries
import numpy as np

# Files
from diracNotation.conversion import *
from diracNotation.prettyPrint import *


######################
# Function defintion #
######################


# Main function for hadamard.
def controlledNot(controlWire, notWire, fullInputState):
    # Initializes a dictionary which will be filled with state configurations.
    # The choice for a dictionary will be clearer later.
    dictionary = {}
    
    # For each element in our state,
    for element in fullInputState:
        
        # Do the hadamard for the line.
        # This will perform a hadamard operation for a certain line,
        # accounting the probability of that element. This already
        # does the distribution of the probability to the two new
        # possible states.
        probabilities = controlledNotForLine(controlWire, notWire, element)
        for probability in probabilities:            
    
            # Once we have performed the distribution, use a dictionary
            # to find out if we already have that configuration stored
            # in our dictionary. If yes, add the probability of this
            # configuration to the already stored probability. If not,
            # add a new entry that points to that value.
            
            key = probability[1]
            value = probability[0]
    
            if dictionary.get(probability[1]) == None:
                dictionary.update({key: value})
            
            else:
                oldValue = dictionary.get(key)
                dictionary.update({key: value + oldValue})
    
    
    # Transforming dictionary back to state:
    newState = []
    for key in dictionary:
        newState.append([dictionary.get(key), key])
    
    return newState


def controlledNotForLine(controlWire, notWire, inputState_line):
    configurations = controlledNotForConfiguration(controlWire, notWire, inputState_line[1])
    
    probabilities = []
    for element in configurations:
        probability = element[0] * inputState_line[0]
        configuration = element[1]
        
        probabilities.append([probability, configuration])
    
    return probabilities


def controlledNotForConfiguration(controlWire, notWire, inputState_line_configuration):
    # Example: '00101', controlWire at index 2, notWire at index 3
    before   = inputState_line_configuration[:notWire]        # '001'
    position = inputState_line_configuration[notWire]         # '0'
    after    = inputState_line_configuration[(notWire + 1):]  # '1'
    
    # Create the one configuration:
    configurations = []
    coefficient = 1
    
    configuration = ''
    if inputState_line_configuration[controlWire] == '1':
        if position == '0':
            configuration = before + '1' + after
            
        elif position == '1':
            configuration = before + '0' + after
    
    else:
        configuration = before + position + after

    configurations.append([coefficient, configuration])

    # Configurations look like [[1, '00111']]
    return configurations

















