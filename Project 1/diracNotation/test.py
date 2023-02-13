#######################
# Libraries and Files #
#######################

# Libraries
import numpy as np

# Files
from diracNotation.prettyPrint import prettyPrintBinary, prettyPrintInteger
from diracNotation.conversion import stateToVector, vectorToState


# Test state:
state = [(np.sqrt(0.1) * 1.j, '101'),
         (np.sqrt(0.5),       '000'),
         (-np.sqrt(0.4),      '010')]


###############
# prettyPrint #
###############

# print(prettyPrintBinary(state))
# print(prettyPrintInteger(state))


##############
# conversion #
##############

vector = stateToVector(state)
# print(vector)
print(vectorToState(vector))