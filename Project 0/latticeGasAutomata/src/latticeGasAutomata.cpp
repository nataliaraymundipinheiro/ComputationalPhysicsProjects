/**
 * @file latticeGasAutomata.cpp
 * @author Raymundi Pinheiro, Natalia (nraym2@illinois.edu)
 * @brief Implementation of the LatticeGasAutomata functions
 * @version 1
 * @date January 2023
 */

#include "latticeGasAutomata.h"

#include <random> /* for std::random_device, std::mt19937, std::uniform_int_distribution */


/****************/
/* Constructors */
/****************/

LatticeGasAutomata::LatticeGasAutomata(): CellularAutomata() {
    // Open the results.txt file to write on it.
    ofstream results("latticeGasAutomata/results.txt");
    
    // Add size and sweeps to results.txt.
    results << size << '\n' << sweeps << '\n';

    // Start the state to the required configuration.
    initialConfiguration();

    // Write initial state to file.
    for (size_t row = 0; row < state.size(); row++) {
        for (size_t col = 0; col < state[row].size(); col++) {
            results << state[row][col] << ' ';
        }
        results << '\n';
    }
    results << '\n';

    // Now, make 'steps' number of swaps for 'sweeps' number of
    // 'sweeps'.
    for (size_t sweep = 0; sweep < sweeps; sweep++) {
        swaps();

        // After making the required number of swaps,
        // write the state to the file.
        for (size_t row = 0; row < state.size(); row++) {
            for (size_t col = 0; col < state[row].size(); col++) {
                results << state[row][col] << ' ';
            }
            results << '\n';
        }
        results << '\n';
    }

    // Close the results.txt file.
    results.close();
}

LatticeGasAutomata::LatticeGasAutomata(int size_, int sweeps_): CellularAutomata(size_) {
    // Update default values.
    size = size_;
    sweeps = sweeps_;

    // Open the results.txt file to write on it.
    ofstream results("latticeGasAutomata/results.txt");
    
    // Start the state to the required configuration.
    initialConfiguration();

    // Write initial state to file.
    for (size_t row = 0; row < state.size(); row++) {
        for (size_t col = 0; col < state[row].size(); col++) {
            results << state[row][col] << ' ';
        }
        results << '\n';
    }
    results << '\n';

    // Now, make 'steps' number of swaps for 'sweeps' number of
    // 'sweeps'.
    for (size_t sweep = 0; sweep < sweeps; sweep++) {
        swaps();

        // After making the required number of swaps,
        // write the state to the file.
        for (size_t row = 0; row < state.size(); row++) {
            for (size_t col = 0; col < state[row].size(); col++) {
                results << state[row][col] << ' ';
            }
            results << '\n';
        }
        results << '\n';
    }

    // Close the results.txt file.
    results.close();
}


/***********/
/* Helpers */
/***********/

void LatticeGasAutomata::initialConfiguration() {
    // Middle index of the matrix:
    size_t middle = state.size() / 2;

    // Fill right half of structure with 1s.
    for (size_t row = 0; row < state.size(); row++) {
        fill(state[row].begin() + middle, state[row].end(), 1);
    }
}

void LatticeGasAutomata::swaps() {
    // Seed the random number generator named 'mt' with 'random_device'.
    random_device rd;
    mt19937 mt(rd());
    
    // Get random numbers for an interval of 0 to 'size - 1'
    uniform_int_distribution<> dist1(0, size - 1);
    
    // Get random numbers for an interval of 1 to 4 (neighbors).
    // This is used to choose a random neighbor.
    uniform_int_distribution<> dist2(1, 4);

    // Number of swaps:
    for (int step = 0; step < steps; step++) {
        // Get random site:
        int row = dist1(mt);
        int col = dist1(mt);
        int value = state[row][col];

        // Get random neighbor:
        // * 1 = up
        // * 2 = right
        // * 3 = down
        // * 4 = left
        int neighbor = dist2(mt);
        int row_neighbor;
        int col_neighbor;
        int value_neighbor;

        if (neighbor == 1) {
            // Account for boundaries:
            if (row - 1 >= 0) {
                row_neighbor = row - 1;
                col_neighbor = col;
                value_neighbor = state[row_neighbor][col_neighbor];

                // Swap values:
                state[row][col] = value_neighbor;
                state[row_neighbor][col_neighbor] = value;
            }
        }
        
        else if (neighbor == 2) {
            // Account for boundaries:
            if (col + 1 < state.size()) {
                row_neighbor = row;
                col_neighbor = col + 1;
                value_neighbor = state[row_neighbor][col_neighbor];

                // Swap values:
                state[row][col] = value_neighbor;
                state[row_neighbor][col_neighbor] = value;
            }
        }
        
        else if (neighbor == 3) {
            // Account for boundaries:
            if (row + 1 < state.size()) {
                row_neighbor = row + 1;
                col_neighbor = col;
                value_neighbor = state[row_neighbor][col_neighbor];

                // Swap values:
                state[row][col] = value_neighbor;
                state[row_neighbor][col_neighbor] = value;
            }
        }
        
        else if (neighbor == 4) {
            // Account for boundaries:
            if (col - 1 >= 0) {
                row_neighbor = row;
                col_neighbor = col - 1;
                value_neighbor = state[row_neighbor][col_neighbor];

                // Swap values:
                state[row][col] = value_neighbor;
                state[row_neighbor][col_neighbor] = value;
            }
        }
        
        // Enters here if it arrives at a problem.
        else {
            cout << "\033[1;31m";
            cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
            cout <<  "There was a problem setting up with the swaps. Stop.";
            cout << "\033[0m\n";
            return;
        }
    }
}