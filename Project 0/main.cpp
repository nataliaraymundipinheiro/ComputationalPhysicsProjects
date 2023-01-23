#include "src/cellularAutomata.h"
#include "latticeGasAutomata/src/latticeGasAutomata.h"
#include "sandAutomata/src/sandAutomata.h"

#include <assert.h> /* assert */
#include <iostream> /* cout, endl */

using namespace std;


void latticeGasAutomata() {
    // Regular values:
    LatticeGasAutomata regular = LatticeGasAutomata();
}

void sandAutomata() {
    int size  = 25;
    int k     = 4;
    int steps = 10000;

    SandAutomata sand(size, k, steps);
    for (int i = 0; i < sand.getPiecesOfSandOverTime().size(); i++) {
        cout << sand.getPiecesOfSandOverTime()[i] << ' ';
    }
}

int main() {

    // Lattice Gas Automata:
    latticeGasAutomata();

    // Sand Automata:
    sandAutomata();
    

    cout << "\033[1;32m\n\nDone.\033[0m\n";
    return 0;
}