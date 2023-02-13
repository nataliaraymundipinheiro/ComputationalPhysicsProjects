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


# Main function for phase.
def phase(wire, theta, fullInputState):
    # Initializes a dictionary which will be filled with state configurations.
    # The choice for a dictionary will be clearer later.
    dictionary = {}
    
    # For each element in our state,
    for element in fullInputState:
        
        # Do the phase for the line.
        # This will perform a phase operation for a certain line,
        # accounting the probability of that element. This already
        # does the distribution of the probability to the two new
        # possible states.
        probabilities = phaseForLine(wire, theta, element)
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


def phaseForLine(wire, theta, inputState_line):
    configurations = phaseForConfiguration(wire, theta, inputState_line[1])
    
    probabilities = []
    for element in configurations:
        probability = element[0] * inputState_line[0]
        configuration = element[1]
        
        probabilities.append([probability, configuration])
    
    return probabilities


def phaseForConfiguration(wire, theta, inputState_line_configuration):
    # Example: '00101', wire at index 2
    before   = inputState_line_configuration[:wire]        # '00'
    position = inputState_line_configuration[wire]         # '1'
    after    = inputState_line_configuration[(wire + 1):]  # '01'
    
    # Create the two configurations:
    configurations = []
    coefficient = np.exp(theta * 1.j)
    if position == '0':
        configuration = before + '0' + after
        configurations.append([1, configuration])
        
    elif position == '1':
        configuration = before + '1' + after
        configurations.append([coefficient, configuration])

    # Configurations look like [[exp(theta j), '00101']]
    return configurations
