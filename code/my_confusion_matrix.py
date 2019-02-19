import numpy as np

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:34:31 2019

@author: jjnun
"""

class MyConfusionMatrix():
    
    def __init__(self,labels):
        n_labels = len(labels)
        # Start the matrix as zeros, square matrix of length equal to n of labels
        matrix = np.zeros((n_labels, n_labels))
        self.matrix = matrix
        # Create a dictionary to match label to column/row
        rowcol_dict = dict()
        for i in range(n_labels):
            # Key is the label, value is the column or row value
            rowcol_dict[labels[i]]=i
        self.rowcol_dict = rowcol_dict
        
        
    def getMatrix(self):
        return self.matrix
    
    def inputResults(self, y_true, y_pred):
        rowcol_dict = self.rowcol_dict
        
        n_y = len(y_true)
        for i in range(n_y):
            row = rowcol_dict[y_true[i]]
            col = rowcol_dict[y_pred[i]]
            self.matrix[row, col] += 1
        
        
        