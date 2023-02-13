# Clear console code. Do not modify.
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass


#######################
# Libraries and Files #
#######################

# Libraries
import numpy as np

# Files
from diracNotation.conversion import *
from diracNotation.prettyPrint import *

from quantumComputerSimulator.hadamard import *
from quantumComputerSimulator.phase import *
from quantumComputerSimulator.controlledNot import *
from quantumComputerSimulator.quantumGatesII import *


######################
# Function defintion #
######################


def ignoreZeros(state):
    ignoreZeros = []
    
    # Clean up floating-point number errors.
    for entry in state:
        entry[0] = np.round(entry[0], 15)
        
        # Remove zeros.
        if entry[0] != 0.0:
            ignoreZeros.append(entry)
        
    return ignoreZeros


############
# NOT Gate #

def notGate(initialState):
    state = [[1, initialState]]

    # NOT gates use H -> P -> H.
    return ignoreZeros(hadamard(0, phase(0, np.pi, hadamard(0, state))))

# print(notGate('0'))
# print(notGate('1'))


############
# Rz Gate #

def rz(initialState, theta):

    # Rz gates use NOT -> P(-θ) -> NOT -> P(+θ).
    state = notGate(initialState)
    
    state = ignoreZeros(phase(0, - theta / 2, state))
    
    notGateOutput = notGate(state[0][1])
    state = [[state[0][0], notGateOutput[0][1]]]
    
    state = ignoreZeros(phase(0, theta / 2, state))
    
    return state

    
# print(rz('0', np.pi))
# print(rz('1', np.pi))


###################
# Control-Rz Gate #




