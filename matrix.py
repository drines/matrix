#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.28
# REVISED DATE:     2019.06.03
# PURPOSE:  Defines a class and methods for supporting Kalman Filters.
#
# NOTES:    TBD
#
#   Example call:
#      python ...
##

# library import statements
import math
from math import sqrt
import numbers

# matrix functions
def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

# matrix class definition
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # DONE - your code here
        if self.h == 1:
            det_sum = self.g[0][0]
        else:
            det_sum = self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]
        return det_sum

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # DONE - your code here
        trace_sum = 0
        for i in range(self.h):
            trace_sum += self.g[i][i]
        return trace_sum


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # DONE - your code here
        # For a 1 x 1 matrix:
        if self.h == 1:
            inv_matrix = [[ 1 / self.g[0][0] ]]
        else:
            # For a 2 x 2 matrix:
            if self.g[0][0] * self.g[1][1] == self.g[1][0] * self.g[0][1]:
                raise(ValueError, "This Matrix does not have an inverse.")
            else:
                inv_det = 1 / self.determinant()
                inv_matrix = [[inv_det * self.g[1][1], inv_det * -1 * self.g[0][1]],
                              [inv_det * -1 * self.g[1][0], inv_det * self.g[0][0]]]
        return inv_matrix


    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # DONE - your code here
        matrix_transpose = []
        # Loop through columns on outside loop
        for c in range(self.w):
            new_row = []
            # Loop through columns on inner loop
            for r in range(self.h):
                # Column values will be filled by what were each row before
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)    
        
        return matrix_transpose


    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # DONE - your code here
        #
        summed_matrix = []
        # loop through each row
        for r in range(self.h):
            # initialize a temporary list holder
            summed_row = []
            # loop through each column
            for c in range(self.w):
                summed_row.append(self.g[r][c] + other[r][c])
            summed_matrix.append(summed_row)
        return summed_matrix


    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            