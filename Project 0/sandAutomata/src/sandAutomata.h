/**
 * @file sandAutomata.h
 * @author Raymundi Pinheiro, Natalia (nraym2@illinois.edu)
 * @brief Implementation of the SandAutomata class
 * @version 1
 * @date January 2023
 */

#pragma once

#include "../../src/cellularAutomata.h"


/**
 * @brief SandGasAutomata Class: Creates a Cellular Automata
 *        for a Sand distribution set of rules.
 * 
 *        The simulated sand grains will drop  and form
 *        columns, thus spreading out, in the same manner
 *        that a table full of sand will work.
 * 
 *        This inherits the functions and members of the
 *        parent class Cellular Automata.
 */
class SandAutomata: public CellularAutomata {
    public:

        /****************/
        /* Constructors */
        /****************/

        /**
         * @brief Construct a new Sand Automata object.
         *        Parametrized constructor.
         * 
         * @param size_ Size of table.
         * @param k_ Max size of column.
         * @param steps_ Total number of steps to take.
         */
        SandAutomata(int size_, int k_, int steps_);
        

        /***********/
        /* Helpers */
        /***********/

        /**
         * @brief Drops grain of sand on the table.
         *        Checks if avalanche will happen.
         * 
         * @param row Row to drop grain of sand.
         * @param col Col to drop grain of sand.
         */
        void dropGranule(int row, int col);

        /**
         * @brief Sorts out the avalanche created by
         *        drop of grain of sand.
         * 
         * @param row Row to start avalanche.
         * @param col Col to start avalanche.
         */
        void avalanche(int row, int col);


        /******************/
        /* Write to Files */
        /******************/

        /**
         * @brief Writes the data from piecesOfSandOverTime
         *        to a TXT file.
         */
        void writePiecesOfSandOverTime();

        /**
         * @brief Writes the data from sizeOfAvalancheOverTime
         *        to a TXT file.
         */
        void writeSizeOfAvalancheOverTime();

        /**
         * @brief Writes the data from snapshotState
         *        to a TXT file.
         */
        void writeSnapshot();

        /**
         * @brief Writes the data from video
         *        to a TXT file.
         */
        void writeVideo();


        /***********/
        /* Getters */
        /***********/

        /**
         * @brief Get the Pieces Of Sand Over Time object.
         * 
         * @return piecesOf
         */
        vector<int> getPiecesOfSandOverTime();

    private:

        /*
         * Size of the table. It will be a 'size' x 'size' table
         * (always a square). Default value set to 25.
         */
        int size = 25;

        /*
         * Column size. The columns cannot be larger than this value.
         * Default max column value set to 4.
         */
        int k = 4;

        /*
         * Number of steps taken in order to make a window average.
         * Default value set to 100.
         */
        int windowAveraging = 100;

        /*
         * Number of pieces of sand in the table.
         */
        int piecesOfSand = 0;

        /*
         * Number of sand granules over time.
         */
        vector<int> piecesOfSandOverTime;

        /*
         * Number of columns that collapsed.
         */
        int sizeOfAvalanche = 0;

        /*
         * How many columns collapse over time.
         */
        vector<int> sizeOfAvalancheOverTime;

        /*
         * Number of steps to pass in order to take snapshot
         * of sand in equilibrium. Default value set to 2000.
         */
        int snapshot = 2000;

        /*
         * Snapshot state.
         */
        vector<vector<int>> snapshotState;

        /*
         * Vector containing all states to plot.
         */
        vector<vector<vector<int>>> video;

        /*
         * Number of total steps to take.
         */
        int steps = 10000;
};