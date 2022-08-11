# Some convenience function for creation of Latex expressions
#
# Semme J. Dijkstra 4/8/2022


from IPython.display import display, Math
from IPython.display import Latex as lt
from IPython.display import display, Math
import numpy as np



def display_matrix(matrix):
    data = ''
    for line in matrix:
        if not isinstance(line, np.ndarray):
            data += ' %.4f' % line + r' \\'
            continue
        if len( line) == 1:
            data += ' %.4f' % line + r' \\'
            continue
        for element in line[:-1]:
            data += ' %.4f&' % element
        data += ' %.4f' % line[-1]
        data += r'\\' + '\n'
    display(Math('\\begin{bmatrix} \n%s\end{bmatrix}' % data))
    
def latex_matrix(matrix):
    data = ''
    for line in matrix:
        if not isinstance(line, np.ndarray):
            data += ' %.4f' % line + r' \\'
            continue
        if len( line) == 1:
            data += ' %.4f' % line + r' \\'
            continue
        for element in line[:-1]:
            data += ' %.4f&' % element
        data += ' %.4f' % line[-1]
        data += r'\\' + '\n'
    return('\\begin{bmatrix} \n%s\end{bmatrix}' % data)

def display_tensor(tensor):
    if tensor.ndim <= 2:
        display_matrix(tensor)
    data = ''
    
#     for line in matrix:
#         if not isinstance(line, np.ndarray):
#             data += ' %.4f' % line + r' \\'
#             continue
            
#         if len( line) == 1:
#             data += ' %.4f' % line + r' \\'
#             continue
            
#         for element in line[:-1]:
#             data += ' %.4f&' % element
#         data += ' %.4f' % line[-1]
#         data += r'\\' + '\n'
#     display(Math('\\begin{bmatrix} \n%s\end{bmatrix}' % data))