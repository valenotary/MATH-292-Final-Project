# imports
import gym
import numpy as np

# activation functions
def sigmoid(x):
    return 1/(1+np.exp(-x))

def steepsigmoid(x):
    return (1/1+np.exp(-4.9*x))

class Node:

    def __init__(self, nType='input', val=0.0):
        self.ID = 0 # TODO
        self.nType=nType
        self.val=0.0
        self.adjNodes=[] # just a list of nodes that point INTO the current node

    def __hash__(self): # TODO
        pass

    def __eq__(self, other):
        pass

class Connection:
    pass

class Genome:
    gIN = 1 # globalInnovationNumber

    def __init__(self, inputs=1, outputs=1):
        pass

    # should be an exact copy (only necessary when copying the champions)
    @staticmethod
    def copyGenome(genome):
        pass

    # returns a NEW genome that is a crossover of two parent genomes
    @staticmethod
    def crossover(g1, g2):
        pass

    # calculates how 'related' two genomes are
    @staticmethod
    def delta(g1, g2, c1=1.0, c2=1.0, c3=1.0):
        pass

class NEAT: # this actually simulates our genome in the gym environment
    # list hyperparameters here

    # generational simulation hyperparameters
    maxGenerations=50 # maximum number of generationl simulations
    populationLimit=150 # population number per generation
    championThresholdCount=5

    # delta function hyperparameters
    deltaThreshold=1.0
    c1=c2=c3=1.0

    # some more hyperparameters... blah blah blah

    def __init__(self, envName=None):
        if (envName!=None): # create a genome with the proper input and output parameters
            pass
        else:
            print('No environment defined; empty NEAT class')

    def simulate():
        pass
