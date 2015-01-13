# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 01:44:26 2014

@author: joe
"""

import numpy as np

class Individual:
    """Attributes:
        genome - 3D array (chromosome,locus,dimension)
        g_shape - 1D array (c,L,d), where c is (haploid) chromosome number,
                    L is number of loci per chromosome, and d is the number
                    of dimensions in the phenotype space.
        phenotype - position vector"""

    def __init__(self,genome=None,g_shape=None):
        self.G_shape = g_shape
        self.G = genome
        if self.G == None:
            if self.G_shape == None:
                self.phenotype = None
            else:
                self.G = self.make_genome()
        self.phenotype = self.set_phenotype()
                
    def make_genome(self):
        return np.random.normal(0,1,self.G_shape)
        
    def set_phenotype(self):
        if self.G == None:
            return None
        return sum(np.sum(self.G, axis=1))
        
    def distance(self,other):
        v = self.phenotype - other.phenotype
        return np.sqrt(sum(v*v))
        
    def asex(self):
        return Individual(self.G,self.G_shape)
        
    def sex(self,other):
        whichCopy = np.random.binomial(1,0.5,self.G_shape[0])
        newG = []
        for i in range(self.G_shape[0]):
            if whichCopy[i] == 0:
                newG.append(self.G[i])
            else:
                newG.append(other.G[i])
        newG = np.array(newG)
        return Individual(newG,newG.shape)
        
    def fitness(self,other):
        d = self.distance(other)
        w = np.exp(-(d**2)/2)
        return w
        
    def mutation(self,mu,dfem):
        ml = np.random.binomial(1,mu,self.G_shape)
        vals = dfem(np.sum(ml))
        self.G.put(ml.nonzero(),vals)
        return
    
    def __repr__(self):
        return str(self.phenotype)
        
        
        