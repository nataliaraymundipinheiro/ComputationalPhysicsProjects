/**
 * @file latticeGasAutomata.h
 * @author Raymundi Pinheiro, Natalia (nraym2@illinois.edu)
 * @brief Implementation of the LatticeGasAutomata class
 * @version 1
 * @date January 2023
 */

#pragma once

#include "../../src/cellularAutomata.h"


/**
 * @brief LatticeGasAutomata Class: Creates a Cellular Automata
 *        for a Lattice Gas set of rules.
 * 
 *        The simulated gas particles will expand as a gas would
 *        expand inside a square structure.
 * 
 *        This inherits the functions and members of the parent
 *        class Cellular Automata.
 */
class LatticeGasAutomata: public CellularAutomata {
    public:

        /****************/
        /* Constructors */
        /****************/

        /**
         * @brief Construct a new Lattice Gas Automata object.
         *        Default constructor.
         *
         *        Write the final result to a TXT file to be
         *        read in Python.
         */
        LatticeGasAutomata();

        /**
         * @brief Construct a new Lattice Gas Automata object.
         *        Parametrized constructor.
         * 
         *        Write the final result to a TXT file to be
         *        read in Python.
         * 
         * @param size_ Size of the lattice.
         * @param sweeps_ Number of sweeps to do. Sweeps represent
         *        'steps' number of swaps between two sites.
         */
        LatticeGasAutomata(int size_, int sweeps_);


        /***********/
        /* Helpers */
        /***********/

        /**
         * @brief Start the state to a certain configuration.
         * 
         *        The lattice starts with the left side empty and
         *        the right side filled. Since 0 defines empty sites
         *        and 1 defines filled sites, this will fill out
         *        the left side with 0s and the right side with 1s.
         */
        void initialConfiguration();

        /**
         * @brief Make the 'steps' number of swaps.
         * 
         *        This will swap a random site with a random neighbor
         *        'steps' times.
         */
        void swaps();

    private:

        /*
         * Size of the lattice. It will be a 'size' x 'size' lattice
         * (always a square). Default value set to 100.
         */
        int size = 100;

        /*
         * Number of swaps we will make per sweep. Default value set to
         *'size' squared. Can be modified through the parametrized
         * constructor.
         */
        int steps = size * size;

        /*
         * Each sweep is 'size' x 'size' swaps. Deault value set to
         * 10000 (i.e., do 10000 repetitions of [100 * 100 =] 100000
         * steps).
         */
        int sweeps = 10000;
};