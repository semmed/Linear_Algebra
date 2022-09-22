import matplotlib.pyplot as plt
import numpy as np

# 1. Add the `plot_title = ''` argument to the function declaration of `plottransform()`
def plottransform(B, Bt, plot_title = ''):
    # Don't change this, just checking whether the arguments are usable
    if not isinstance(B, (np.ndarray)):
        print('B must be a numpy array')
        return
    if not isinstance(Bt, (np.ndarray)):
        print('Bt must be a numpy array')
        return

    if not (B.shape[0] == 2) or B.shape[1] < 2 or not len(B.shape)==2:
        print('Matrix shape '+str(B.shape)+' does not match expected polygon shape (2 x >=2)')
        return
    if not (Bt.shape[0] == 2) or Bt.shape[1] < 2 or not len(Bt.shape)==2:
        print('Matrix shape '+str(Bt.shape)+' does not match expected polygon shape (2 x >=2)')
        return
    
    # Make sure that the plot is isometric along the axes
    plt.axis('equal')
    
    # 2. Update the code so that it will plot the title using `plt.title()`
    plt.title(plot_title)
    
    # Plot the untransformed shape
    plt.fill(B[0,:],B[1,:],'C0', ec='k',zorder=0)
    
    # Plot the lines connecting the non-transformed and transformed vertices
    for i in range(B.shape[1]):
        plt.plot([B[0,i], Bt[0,i]],[B[1,i],Bt[1,i]],'k--',zorder=1)

    # Plot the transformed shape with transparency so that the original shape and/or lines can be seen if they are covered
    plt.fill(Bt[0,:],Bt[1,:],'C1', ec='k', alpha=.8,zorder=2)

    return 
    