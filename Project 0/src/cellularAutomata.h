/**
 * @file cellularAutomata.h
 * @author Raymundi Pinheiro, Natalia (nraym2@illinois.edu)
 * @brief Implementation of the CellularAutomata class
 * @version 1
 * @date January 2023
 */

#pragma once

#include <fstream>  /* ofstream */
#include <iostream> /* cout, endl */
#include <string>   /* string */
#include <vector>   /* vector */

using namespace std;


/**
 * @brief CellularAutomata Class: Creates a general Cellular
 *        Automata. Does not set the rules; this will be defined
 *        by the child classes.
 * 
 *        This function only initializes a structure of given
 *        size will all 0s.
 */
class CellularAutomata {
    public:

        /****************/
        /* Constructors */
        /****************/

        /**
         * @brief Construct a new Cellular Automata object.
         *        Default constructor.
         */
        CellularAutomata();

        /**
         * @brief Construct a new Cellular Automata object.
         *        Parametrized constructor.
         * 
         * @param size_ Size of the structure.
         */
        CellularAutomata(int size_);


        /***********/
        /* Helpers */
        /***********/

        /**
         * @brief Resize the strucutre to the correct size.
         *        Initializes it to all 0s.
         * 
         * @param size_ Size of the structure.
         */
        void initialize(int size_);

        /**
         * @brief Print the structure.
         * 
         *        This function prints the structure as if it were a
         *        'size' x 'size' matrix.
         * 
         *        This is for the purpose of easily visualizing and
         *        debugging the code.
         */
        void print();

        
        /***********/
        /* Getters */
        /***********/
        
        /**
         * @brief Get the state object.
         * 
         * @return The state.
         */
        vector<vector<int>> getState();

    protected:

        /*
         * Size of the structure.
         * Default is set to 100.
         */
        int size = 100;

        /*
         * Represents the state of the cellular automata.
         */
        vector<vector<int>> state;
};