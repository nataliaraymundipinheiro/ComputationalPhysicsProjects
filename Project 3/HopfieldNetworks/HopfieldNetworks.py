"""
Part 1: Hopfield Networks
"""

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import HopfieldNetworks.MakeImage


# =============================================================================
# Initialize the arrays states, biases, and weights.
# =============================================================================

def Initialize(n):
    print("Initializing states, biases, and weights...")
    # Create states
    states = np.random.choice([-1,1], size=(n,n), replace=True)

    # Create biases
    biases = np.random.uniform(low=-1.0, high=1.0, size=(n,n))
    
    # Create weights
    weights_notsymmetric = np.random.uniform(low=-1.0, high=1.0, size=(n**2,n**2))
    weights_symmetric = (weights_notsymmetric + weights_notsymmetric.T) / 2
    weights_symmetric_zerodiagonal = weights_symmetric - np.diag(np.diag(weights_symmetric))
    weights = weights_symmetric_zerodiagonal
    
    print("  Done")
    return states, biases, weights



# =============================================================================
# Update the state of a neuron.
# Choose a random neuron and updates it according to the following update rule:
# * Ignore the neuron's current state;
# * Compute the "total weight" Ti coming into it;
# * If this "total weight" Ti is bigger than the bias for the original neuron,
#   the new state is 1, otherwise it is -1.
# =============================================================================

def UpdateState(states, biases, weights):
    n = len(states)
    
    # print("Initial State:")
    # print(states)
    
    # Choose a random row and column (choosing a random state)
    row = np.random.randint(low=0, high=n, dtype=int)
    col = np.random.randint(low=0, high=n, dtype=int)
    
    # Consider each weight row a "state output", and each column in that row a
    # "state input"
    weights_row = weights[row * n + col]
    states_row = states.reshape(weights_row.shape)

    # Compute the "total weight" Ti coming into it
    Ti = sum(states_row * weights_row)
    
    # If this "total weight" Ti is bigger than the bias for the original
    # neuron, the new state is 1, otherwise it is -1
    if Ti > biases[row,col]:
        states[row,col] = 1
    else:
        states[row,col] = -1
    
    return states
    # print("Final States:")
    # print(states)



# =============================================================================
# Check if network has converged.
# This function goes to every node and finds if this node wants to flip.
# =============================================================================

def CheckConvergence(states, biases, weights):
    n = len(states)
    
    # Perform the sums for each state
    states_temp = states.reshape(n**2,1)
    sums = weights @ states_temp
    
    # Check if any 
    for row in range(n):
        for col in range(n):
            # Compute the "total weight" Ti coming into it
            Ti = sums[row * n + col]

            # If this "total weight" Ti is bigger than the bias for the
            # original neuron and the state is -1, we still haven't converged
            if Ti > biases[row,col] and states[row,col] == -1:
                return False
            # If this "total weight" Ti is smaller than the bias for the
            # original neuron and the state is 1, we still haven't converged
            if Ti < biases[row,col] and states[row,col] == 1:
                return False

    # If we pass everything, return True
    return True

# =============================================================================
# Compute the energy of the corresponding state.
# =============================================================================

def GetEnergy(states, biases, weights):
    n = len(states)
    
    # Reshape arrays for matrix multiplication
    states_temp = states.reshape(n**2,1)
    biases_temp = biases.reshape(1,n**2)
    
    # Apply it to the formula
    E = - 0.5 * states_temp.T @ weights @ states_temp + \
        biases_temp @ states_temp
    
    return E
  
  
# =============================================================================
# Plot a graph of the behavior of energy throughout several state updates.
# =============================================================================

# Analyzes the energy of one state
def AnalyzingEnergy(states, biases, weights):
    current_time = str(dt.datetime.now().strftime('%H:%M:%S'))
    print("Starting to analyze state... (" + current_time + ')')
    
    initial_energy = GetEnergy(states, biases, weights)

    energies = np.array([initial_energy])
    
    steps = 0
    
    while not CheckConvergence(states, biases, weights):
        steps += 1
        
        states = UpdateState(states, biases, weights)

        energy = GetEnergy(states, biases, weights)
        energies = np.append(energies, energy)
    
    print("  State has been analyzed and has converged.")
    return energies, steps

# Analyzes the energy of ten state
def Analyzing10Energies(n):
    # Initialize 10 different states with biases and weights
    data_arr = []
    for d in range(10):
        data_arr.append(Initialize(n))
    
    energies_arr = []
    steps_arr = []
    
    for data in data_arr:
        energies, steps = AnalyzingEnergy(data[0], data[1], data[2])

        energies_arr.append(energies)
        steps_arr.append(steps)
    
    fig, ax = plt.subplots(1, figsize=(10,10))
    ax.set_title("Analysis of State Convergence over Number of Steps Using " +\
                 str(n**2) + " Neurons")
    ax.set_xlabel("Steps")
    ax.set_ylabel("Energy")
    ax.set_xlim(0, max(steps_arr))
    ax.axhline(y=0, linestyle='dashed', color='black')
    
    for d in range(10):    
        label = 'State ' + str(d)
        x = range(steps_arr[d] + 1)
        y = energies_arr[d]
        ax.plot(x, y, label=label)
    
    ax.legend()

    folder = 'Part 1 - Hopfield Networks/Results/'
    filename = 'Analysis of Energy Convergence over Number of Steps'
    fig.savefig(folder + filename, dpi=200)



# =============================================================================
# Turn a binary string into an image.
# =============================================================================

def TurnIntoImage(string_image):
    # Number of pixels
    n = int(np.sqrt(len(string_image)))
    # Save image of size n x n
    image = np.zeros((n, n))

    # Make the conversion between string to 2D-array of pixels
    image_temp = np.fromiter(string_image, (np.compat.unicode, 1))
    image_temp = image_temp.astype(int)
    
    # Replace zeros with -1.
    image_temp[image_temp == 0] = -1

    # Reshape to image size
    image = image_temp.reshape((n, n))

    # fig, ax = plt.subplots(1)
    # ax.matshow(image)
    
    return image



# =============================================================================
# Train the computer to learn a set of images so it can reproduce them later
# on. It takes in a 1D-array of strings (10x10 images) and returns the weights
# of the trained images along with the images.
# =============================================================================

# def Memorizing(string_images):
#     # Number of memories
#     m = len(string_images)
#     n = int(np.sqrt(len(string_images[0])))
    
#     # Create an images array which is going to store string_images in a 2D
#     # numpy array
#     flattened_images = np.zeros((m,n**2))
#     images = np.zeros((m,n,n))
    
#     # Make the conversion between 1D-string array to 2D-array
#     for i in range(len(string_images)):
#         images[i] = TurnIntoImage(string_images[i])
#         flattened_images[i] = images[i].flatten()

#     # Calculate the weights (check if this is correct)
#     weights = 1 / m * flattened_images.T @ flattened_images
    
#     return weights, images, flattened_images
    

def Memorizing(images):
    # Number of memories
    m = int(len(images))
    # Size of image
    n = int(len(images[0]))
    
    # Create an images array which is going to store string_images in a 2D
    # numpy array
    flattened_images = np.zeros((m,n**2))
    
    # Flatten each image
    for i in range(len(images)):
        flattened_images[i] = images[i].flatten()

    # Calculate the weights (check if this is correct)
    weights = 1 / m * flattened_images.T @ flattened_images
    
    return weights, flattened_images


# =============================================================================
# It takes in a 1D-array of strings (10x10 images to train the weights) and
# returns a restored image.
# =============================================================================

def Restore(to_memorize, to_recover):
    # Make to_memorize is a numpy array
    to_memorize = np.array(to_memorize)
    
    # Create an images array which is going to store string_images in a 2D
    # numpy array
    weights, images, flattened_images = Memorizing(to_memorize)
    original_image = TurnIntoImage(to_recover)
    
    # Create random biases (check this!)
    n = int(np.sqrt(len(to_recover)))
    biases = np.random.uniform(low=-1.0, high=1.0, \
                               size=(n,n))
    
    intermediate_image = original_image.copy()
    temp = original_image.copy()
    
    steps = 0
    while not CheckConvergence(temp, biases, weights):
        steps += 1
        # This is an estimated value: it might be wrong
        if steps == 200:
            intermediate_image = temp.copy()
            
        temp = UpdateState(temp, biases, weights)
        
    final_image = temp.copy()
    
    
    # Plotting and saving
    # fig, ax = plt.subplots(1, 3, figsize=((15,5)))
    
    # # Original
    # ax[0].set_title('Original Image')
    # ax[0].matshow(original_image)

    # # Intermediate
    # ax[1].set_title('Intermediate Image')
    # ax[1].matshow(intermediate_image)

    # # Final
    # ax[2].set_title('Final Image')
    # ax[2].matshow(final_image)
    
    # return final_image, fig
    return final_image


# =============================================================================
# 
# =============================================================================

# def HammingDistance(to_memorize, to_recover, p, k):
#     # Flips the bits in place
#     n = int(np.sqrt(len(to_recover)))
#     to_flip = np.random.choice(np.arange(0, n**2), size=k, replace=False)
#     for index in to_flip:
#         to_recover = to_recover[:index] + ('1' if to_recover[index] == '0' \
#                                             else '0') + to_recover[index+1:]
    
#     # Turn it into an image and flatten it
#     to_recover_image = TurnIntoImage(to_recover)
#     to_recover_flattened = to_recover_image.flatten()

#     # Restore the final_image
#     # final_image, fig = Restore(to_memorize, to_recover)
#     final_image = Restore(to_memorize, to_recover)
#     final_image_flattened = final_image.flatten()

#     # Calculate Hamming distance
#     hamming_distance = to_recover_flattened @ final_image_flattened

#     return hamming_distance

def HammingDistance(p, k):
    # Add p images to the network
    memories = []
    for p2 in range(0,p):
        memories.append(np.random.choice([-1,1], size=(10,10)))
    memories = np.array(memories)
    
    # Choose one of the p images
    index_range = np.arange(0,p,step=1)
    image = weights[np.random.choice(index_range)]
    image_flattened = image.flatten()
    
    # Corrupt k bits on that image
    n = image_flattened.shape[0]
    to_flip = np.random.choice(np.arange(0, n), size=k, replace=False)
    for index in to_flip:
        image_flattened[index] = 1 if (image_flattened[index] < 0) else -1

    image = image_flattened.reshape((int(np.sqrt(n)), int(np.sqrt(n))))
    final_image = Restore(weights, image)
    final_image_flattened = final_image.flatten()
    hamming_distance = image_flattened @ final_image_flattened
    
    return hamming_distance
    

# =============================================================================
# Testing
# =============================================================================


# *****************************************************************************
# Hopfield Network's Evolution: Energy vs. Iteration

# Analyzing10Energies(10)



# *****************************************************************************
# Original, Intermediate, and Final Images of Smiley Face

# to_memorize = np.array(['0000000000000100010000000000000000000000000010000000000000000001110000001000100001000001111000000001'])
# to_recover = '0000011111000101111100000111110000011111000011111111111111111111111111111111111111111111111111111111'
# final_image, fig = Restore(to_memorize, to_recover)
# fig.suptitle('Smiley Face with Corrupted 1/4th of the Image', fontsize=16)
# folder = 'Part 1 - Hopfield Networks/Results/'
# name = 'Original, Intermediate, and Final Image Using Hopfield Networks - Smiley Face'
# fig.savefig(folder + name, dpi=200)

# to_memorize = np.array(['0000000000000100010000000000000000000000000010000000000000000001110000001000100001000001111000000001',\
#                         '0001111000000111100000001100000000110000001111111000001100100000110000000011000000001100000000110000'])
# to_recover = '0000011111000101111100000111110000011111000011111111111111111111111111111111111111111111111111111111'
# final_image, fig = Restore(to_memorize, to_recover)
# fig.suptitle('Smiley Face with Corrupted 1/4th of the Image with both Images in Weights', fontsize=16)
# folder = 'Part 1 - Hopfield Networks/Results/'
# name = 'Original, Intermediate, and Final Image Using Hopfield Networks - Smiley Face with 2 Inputs'
# fig.savefig(folder + name, dpi=200)

# to_recover = '0001111000000111100000001100000000000000000000000000000000000000000000000000000000000000000000000000'
# final_image, fig = Restore(to_memorize, to_recover)
# fig.suptitle('Tree with Corrupted Part with both Images in Weights', fontsize=16)
# folder = 'Part 1 - Hopfield Networks/Results/'
# name = 'Original, Intermediate, and Final Image Using Hopfield Networks - Tree with 2 Inputs'
# fig.savefig(folder + name, dpi=200)



# *****************************************************************************
# Hamming Distance

hamming_distances = np.empty((60, 100))

for k in range(0,60):
   for p in range(1,100):
       hamming_distances[k,p] = HammingDistance(p,k)
       
plt.matshow(hamming_distances)
plt.colorbar()
plt.show()