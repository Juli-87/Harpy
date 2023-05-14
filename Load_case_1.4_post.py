from post_processing import *
import pickle
import matplotlib.pyplot as plt

case = 'case_1.4'
folder = './' + case + '/'

with open(folder+case+'.pkl', 'rb') as f:
    _ = pickle.load(f)
    wt = pickle.load(f)
    BEM = pickle.load(f)
	
f_blade, f_gravity, f_inertia, M_rot, P_harpy = rotor_moment(wt, BEM)
lift = BEM.l
drag = BEM.d
alpha = BEM.alpha
phi = BEM.phi


fig1 = plt.figure()
ax1_1 = fig1.add_subplot(1,1,1)
ax1_1.plot(wt.z,lift[3,0,:])
ax1_1.plot(wt.z,lift[3,1,:])
ax1_1.plot(wt.z,lift[3,2,:])
ax1_1.set_xlabel("z [m]")
ax1_1.set_ylabel("Lift [N/m]")
ax1_1.grid()

fig2 = plt.figure()
ax2_1 = fig2.add_subplot(1,1,1)
ax2_1.plot(wt.z,drag[3,0,:])
ax2_1.plot(wt.z,drag[3,1,:])
ax2_1.plot(wt.z,drag[3,2,:])
ax2_1.set_xlabel("z [m]")
ax2_1.set_ylabel("Drag [N/m]")
ax2_1.grid()

fig3 = plt.figure()
ax3_1 = fig3.add_subplot(1,1,1)
ax3_1.plot(wt.z,alpha[3,0,:]*180/np.pi)
ax3_1.plot(wt.z,alpha[3,1,:]*180/np.pi)
ax3_1.plot(wt.z,alpha[3,2,:]*180/np.pi)
ax3_1.set_xlabel("z [m]")
ax3_1.set_ylabel("$\\alpha$ [°]")
ax3_1.grid()

fig4 = plt.figure()
ax4_1 = fig4.add_subplot(1,1,1)
ax4_1.plot(wt.z,phi[1,0,:]*180/np.pi)
ax4_1.plot(wt.z,phi[1,1,:]*180/np.pi)
ax4_1.plot(wt.z,phi[1,2,:]*180/np.pi)
ax4_1.set_xlabel("z [m]")
ax4_1.set_ylabel("$\\phi$ [°]")
ax4_1.grid()

fig5 = plt.figure()
ax5_1 = fig5.add_subplot(1,1,1)
ax5_1.plot(wt.z,phi[1,0,:]*180/np.pi)
ax5_1.set_xlabel("z [m]")
ax5_1.set_ylabel("$\\phi$ [°]")
ax5_1.grid()

A_rot = np.pi * wt.R**2
u0 = 8
rho = 1.225
P_avail = 0.5* rho * A_rot * u0**3
Cp = P_harpy/P_avail

print("Cp: "+str(np.mean(Cp[2:])))
print("Shaft My: "+str((M_rot[3,1])))