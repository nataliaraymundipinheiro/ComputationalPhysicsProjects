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
import matplotlib.pyplot as plt

# Files
from diracNotation.conversion import *
from diracNotation.prettyPrint import *
from quantumComputerSimulator.hadamard import hadamard
from quantumComputerSimulator.phase import phase
from quantumComputerSimulator.controlledNot import controlledNot


######################
# Function defintion #
######################



def readInput(filename):
    # Reads all lines from file.
    lines = open(filename).readlines()

    # Find number of wires.
    numberOfWires = int(lines[0])
    
    initialState = []
    if lines[1][0] == 'INITSTATE':
        # Get the initial state:
        initialState = initialStateFormatter(numberOfWires, lines[1].split())
    else:
        initialState = [[1, str(bin(0)[2:].zfill(numberOfWires))]]
        
    # Create an array to save all gate operations.
    gateOperations = []
    for line in lines[2:]:
        gateOperations.append(line.split())
        
    return numberOfWires, initialState, gateOperations


def initialStateFormatter(numberOfWires, initialState):
    if initialState[1] == 'FILE':    # INITSTATE FILE myFile.txt
        # Reads all lines from file.
        inputFile = open(initialState[2]).readlines()
        lines = []
        for line in inputFile:
            lines.append(line.split())
            
        # Lines looks like: probability = [real, imaginary]
        
        state = []
        index = 0
        for probability in lines:
            amplitude = float(probability[0]) + float(probability[1])*1.j
            
            if amplitude != 0:
                configuration = bin(index)[2:].zfill(numberOfWires)
                
                state.append([amplitude, configuration])

            index += 1
        
        return state

    elif initialState[1] == 'BASIS': # INITSTATE BASIS |001>
        configuration = ''
        for i in range(1, len(initialState[2]) - 1):
            configuration += initialState[2][i]

        return [[1, configuration]] # Returns '001'


def performGateOperations(numberOfWires, initialState, gateOperations):
    state = initialState.copy()
    
    for gateOperation in gateOperations:
        if gateOperation[0] == 'H':
            state = hadamard(int(gateOperation[1]), state)
        elif gateOperation[0] == 'P':
            state = phase(int(gateOperation[1]), float(gateOperation[2]), state)
        elif gateOperation[0] == 'CNOT':
            state = controlledNot(int(gateOperation[1]), int(gateOperation[2]), state)
    
    removeZeros = []
    for entry in state:
        if entry[0] != 0:
            removeZeros.append(entry)
    state = removeZeros
    
    
    # Consider MEASURE:
    measure = state.copy()
    if gateOperations[-1][0] == 'MEASURE':
        measureProbabilities = []
        measureConfigurations = []
        
        for entry in measure:
            entry[0] = abs(entry[0]) ** 2
            measureProbabilities.append(entry[0])
            measureConfigurations.append(entry[1])
            
        return np.random.choice(measureConfigurations, p=measureProbabilities)
                    
    
    return state




###########
# Testing #
###########

file = 'rand.circuit'
numberOfWires, initialState, gateOperations = readInput(file)
output = performGateOperations(numberOfWires, initialState, gateOperations)
print(output)


file = 'measure.circuit'
numberOfWires, initialState, gateOperations = readInput(file)

outputs = {}
for i in range(0, 1000):
    output = performGateOperations(numberOfWires, initialState, gateOperations)
    # print(output)
    # plt.hist(output)
    
    if outputs.get(output) == None:
        outputs.update({output: 1})
    else:
        oldVal = outputs.get(output)
        outputs.update({output: 1 + oldVal})
        
plt.title("MEASURE Circuit Output vs. Count")
plt.xlabel("MEASURE Circuit Output")
plt.ylabel("Count")

keys = []
vals = []
for key in sorted(outputs):
    keys.append(key)
    vals.append(outputs.get(key))
print(outputs, '\n')
print(keys, vals)

plt.bar(keys, vals)


file = 'input.circuit'
numberOfWires, initialState, gateOperations = readInput(file)
output = performGateOperations(numberOfWires, initialState, gateOperations)
print(output)
