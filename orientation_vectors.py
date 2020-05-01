import math
import numpy as np

def U_vector(u_k, o_k, i_k):
    
    term1 = M_vector(o_k, i_k) * math.sin(u_k)
    term2 = N_vector(o_k) * math.cos(u_k)
    Uvec = np.add(term1, term2)

    return Uvec

def N_vector(o_k):

    Nx = math.cos(o_k)
    Ny = math.sin(o_k)
    Nz = 0
    Nvec = np.array([Nx, Ny, Nz])

    return Nvec

def M_vector(o_k, i_k):
    
    Mx = -math.sin(o_k) * math.cos(i_k)
    My = math.cos(o_k) * math.cos(i_k)
    Mz = math.sin(i_k)
    Mvec = np.array([Mx, My, Mz])

    return Mvec