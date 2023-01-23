/**
 * @file sandAutomata.cpp
 * @author Raymundi Pinheiro, Natalia (nraym2@illinois.edu)
 * @brief Implementation of the SandAutomata functions
 * @version 1
 * @date January 2023
 */

#include "sandAutomata.h"

#include <random> /* for std::random_device, std::mt19937, std::uniform_int_distribution */


// Keep track of how many steps we have taken.
static int countSteps = 0;
static bool doVideo = false;


/****************/
/* Constructors */
/****************/

SandAutomata::SandAutomata(int size_, int k_, int steps_): CellularAutomata(size_) {
    // Update default values.
    size = size_;
    k = k_;
    steps = steps_;

    // Seed the random number generator named 'mt' with 'random_device'.
    random_device rd;
    mt19937 mt(rd());
    // Get random numbers for an interval of 0 to 'size - 1' to choose
    // coordinates to drop sand granule.
    uniform_int_distribution<> dist(0, size - 1);

    for (int step = 0; step < steps; step++) {
        int row = dist(mt);
        int col = dist(mt);

        // Use this avalanche to make a video:
        if (step == snapshot) {
            doVideo = true;
        }

        dropGranule(row, col);

        doVideo = false;
    }

    writePiecesOfSandOverTime();
    writeSizeOfAvalancheOverTime();
    writeSnapshot();
    writeVideo();
}


/***********/
/* Helpers */
/***********/

void SandAutomata::dropGranule(int row, int col) {
    if (doVideo) {
        // Push back initial state.
        video.push_back(state);
    }

    // Add new piece of sand at that spot.
    state[row][col] += 1;
    
    // Average of pieces of sand:
    piecesOfSand++;

    // If that column has height bigger than 'k',
    // start avalanche.
    if (state[row][col] > k)    { avalanche(row, col); }

    countSteps++;
    if (countSteps % windowAveraging == 0) {
        piecesOfSandOverTime.push_back(piecesOfSand);
        
        sizeOfAvalancheOverTime.push_back(sizeOfAvalanche);
        sizeOfAvalanche = 0;
    }

    if (countSteps == snapshot) {
        snapshotState = state;
    }
}

void SandAutomata::avalanche(int row, int col) {
    // @todo Make this function more random.

    // Decrease size of column.
    state[row][col] -= 4;
    // One more column collapses:
    sizeOfAvalanche++;

    bool up     = row - 1 >= 0;
    bool down   = row + 1 < state.size();
    bool left   = col - 1 >= 0;
    bool right  = col + 1 < state.size();

    // If these columns exist, increase their size by one.
    if (up)     { state[row - 1][col] += 1; }
    else        { piecesOfSand--; }

    if (down)   { state[row + 1][col] += 1; }
    else        { piecesOfSand--; }

    if (left)   { state[row][col - 1] += 1; }
    else        { piecesOfSand--; }

    if (right)  { state[row][col + 1] += 1; }
    else        { piecesOfSand--; }

    video.push_back(state);

    // If these columns exist and their size is larger than
    // 'k', create an avalanche.
    if (up && state[row - 1][col] > k)      { avalanche(row - 1, col); }
    if (down && state[row + 1][col] > k)    { avalanche(row + 1, col); }
    if (left && state[row][col - 1] > k)    { avalanche(row, col - 1); }
    if (right && state[row][col + 1] > k)   { avalanche(row, col + 1); }

}


/******************/
/* Write to Files */
/******************/

void SandAutomata::writePiecesOfSandOverTime() {
    ofstream file("sandAutomata/piecesOfSandOverTime.txt");

    for (int number : piecesOfSandOverTime) {
        file << number << ' ';
    }

    file.close();
}

void SandAutomata::writeSizeOfAvalancheOverTime() {
    ofstream file("sandAutomata/sizeOfAvalancheOverTime.txt");

    for (int number : sizeOfAvalancheOverTime) {
        file << number << ' ';
    }

    file.close();
}

void SandAutomata::writeSnapshot() {
    ofstream file("sandAutomata/snapshot.txt");

    for (int row = 0; row < snapshotState.size(); row++) {
        for (int col = 0; col < snapshotState[row].size(); col++) {
            file << snapshotState[row][col] << ' ';
        }
        file << '\n';
    }

    file.close();
}

void SandAutomata::writeVideo() {
    ofstream file("sandAutomata/video.txt");

    for (vector<vector<int>> currentState : video) {
        for (int row = 0; row < currentState.size(); row++) {
            for (int col = 0; col < currentState[row].size(); col++) {
                file << currentState[row][col] << ' ';
            }
            file << '\n';
        }
        file << '\n';
    }

    file.close();
}


/***********/
/* Getters */
/***********/

vector<int> SandAutomata::getPiecesOfSandOverTime() {
    return piecesOfSandOverTime;
}


