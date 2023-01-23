/**
 * @file cellularAutomata.cpp
 * @author Raymundi Pinheiro, Natalia (nraym2@illinois.edu)
 * @brief Implementation of the CellularAutomata functions
 * @version 1
 * @date January 2023
 */

#include "cellularAutomata.h"


/****************/
/* Constructors */
/****************/

CellularAutomata::CellularAutomata() {
    // Initializes state with 'size' rows and 'size' columns.
    initialize(size);
}

CellularAutomata::CellularAutomata(int size_) {
    // Update default value to size_.
    size = size_;

    // Initializes state with 'size' rows and 'size' columns.
    initialize(size);
}


/***********/
/* Helpers */
/***********/

void CellularAutomata::initialize(int size_) {
    // Update default value to size_.
    size = size_;
    
    // Creates 'size' number of rows:
    state.resize(size);

    // Update size of each row to size.
    for (size_t row = 0; row < state.size(); row++) {
        // Creates 'size' number of columns:
        state[row].resize(size);
        // Fill the rows will 0s.
        fill(state[row].begin(), state[row].end(), 0);
    }
}

void CellularAutomata::print() {
    cout << endl;
    for (size_t row = 0; row < state.size(); row++) {
        for (size_t col = 0; col < state[row].size(); col++) {
            cout << state[row][col] << ' ';
        }
        cout << endl;
    }
    cout << endl;
}


/***********/
/* Getters */
/***********/

vector<vector<int>> CellularAutomata::getState() {
    return state;
}