# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:56:12 2021

@author: Aapo Kössi
"""

#import the libraries we use
import numpy as np
import matplotlib.pyplot as plt
import argparse

#initialize and configure the command line argument parser
parser = argparse.ArgumentParser(description = 'draw 3d curve with curvature kappa and torsion tau')
parser.add_argument('kappa', type = str, help = 'type an equation for the curvature in python/numpy syntax:'\
                    ' (exponent as a**b, square root as np.sqrt(), etc.). As the variable use s_, arc length!')
parser.add_argument('--tau', type = str, help = 'optionally type an equation for the torsion in python/numpy syntax.'\
                    ' Similarly to kappa, use s_ as the variable!',
                    default = '0')
parser.add_argument('--limits', nargs = '+', type = float, help = 'optionally set both limits of s to use for the curve, defaults to +-20',
                    default = (-20.0,20.0))
parser.add_argument('--equal_scaling', action = 'store_true', help = 'specify this flag if you want the plot to be scaled equally for all axis.')

#parse given arguments and define some variables for easier access
args = parser.parse_args()
str_curvature = args.kappa
str_torsion = args.tau
lims = args.limits

#assert that the user has not given more or less than 2 limits for our arc length parameter
assert len(lims) == 2

#this function parses the user-given string function into a python function
#note: when evaluating the user input, only python builtins and the numpy package are available
def make_user_function(string):
    def func(param):
        string_with_param = string.replace('s_',str(param))
        func_at_param = eval(string_with_param, {'np': np})
        return func_at_param
    return func


#try defining given curvature and torsion functions and evaluate one test call at s_ = 0
try:
    curvature = make_user_function(args.kappa)
    curvature(0.0)
except:
    print('something went wrong when defining the curvature, check your input arguments')
    raise SystemExit
try:
    torsion = make_user_function(args.tau)
    torsion(0.0)
except:
    print('something went wrong when defining the torsion, check your input arguments')
    raise SystemExit

#defining our "infinitesimal" ds, s, 0 in R^3 and our initial Frenet frame
#note: you can try playing around with changing the value of ds and trade
#computation power for more accuracy or vice versa.
ds = 0.01
s = np.arange(lims[0],lims[1], ds)
zero_vec = np.array([0.0,0.0,0.0])
starting_point = zero_vec.copy()
starting_e1 = np.array([1.0,0.0,0.0])
starting_e2 = np.array([0.0,1.0,0.0])
starting_e3 = np.array([0.0,0.0,1.0])

#safe normalization function
def div_by_norm(vector):
    norm = get_norm(vector)
    if norm != 0.0:
        normal_vec = vector / norm
    else: normal_vec = zero_vec
    return normal_vec
    
#function for standard euclidean norm of a vector
def get_norm(vector):
    return np.linalg.norm(vector)

def numerically_differentiate_frame(basis, kappa, tau):
    '''
    numerically approximate the change in the frenet frame with given current
    e1(s), e2(s), e3(s) as basis and kappa(s), tau(s) as kappa, tau

    RETURNS: list of e1(s+ds), e2(s+ds), e3(s+ds)
    '''
    e1, e2, e3 = basis
    
    #rotate current e1 according to curvature, normalization is required here
    #as we are working with finite differences
    de1 = kappa * e2
    new_e1 = div_by_norm(e1 + de1*ds)
    
    #rotate our current e2 according to frenet equation,
    #then project the result to be orthogonal to e1(s+ds)
    #and finally normalize the result
    de2 = -kappa * e1 + tau * e3
    raw_e2 = e2 + de2*ds
    ortho_e2 = raw_e2 - np.dot(raw_e2,new_e1)*new_e1
    new_e2 = div_by_norm(ortho_e2)
    
    #e3 = e1 cross e2
    new_e3 = np.cross(new_e1, new_e2)
    return [new_e1, new_e2, new_e3]

#define intial values for loop
u = [starting_point]
e1 = starting_e1
e2 = starting_e2
e3 = starting_e3

#move u ds by a ds length vector in direction e1 and
#calculate next position of our Frenet frame
for s_value in s:
    u.append(u[-1] + e1*ds)
    basis = [e1, e2, e3]
    kappa = curvature(s_value)
    tau = torsion(s_value)
    e1, e2, e3 = numerically_differentiate_frame(basis, kappa, tau)        

#define our plot
fig = plt.figure()
ax = plt.axes(projection = '3d')

#combine accumulated u into a single matrix
u = np.stack(u)

#if equal scaling of axes required, calculate largest diff in one coordinate,
#calculate middle points of all coordinates along curve and
#set limits accordingly
if args.equal_scaling:
    umax = np.amax(u)
    umin = -np.amax(-u)
    interval = umax - umin
    half_interval = interval/2.0
    umeans = (np.amax(u,axis=0) - np.amax(-u,axis=0)) / 2.0
    ax.set_xlim(umeans[0] - half_interval,umeans[0] + half_interval)
    ax.set_ylim(umeans[1] - half_interval,umeans[1] + half_interval)
    ax.set_zlim(umeans[2] - half_interval,umeans[2] + half_interval)

#transform u into pyplot friendly format
u = np.transpose(u).tolist()

#draw plot and show
ax.plot(*u)
plt.show()


