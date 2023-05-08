from post_processing import *
import pickle

case = 'case_111'
folder = './' + case + '/'

with open(folder+case+'.pkl', 'rb') as f:
    _ = pickle.load(f)
    wt = pickle.load(f)
    BEM = pickle.load(f)
	
f_blade, f_gravity, f_inertia, M_rot, P_harpy = rotor_moment(wt, BEM)