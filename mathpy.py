import scipy as sp
import sympy as sy
from sympy import init_session
import spb
import numpy as np
import pint
import matplotlib
import os

os.environ["XDG_SESSION_TYPE"] = "xcb"
import matplotlib.pyplot as plt

# use qt backend
# matplotlib.use("Qt5Agg")
u = pint.UnitRegistry()
init_session(use_latex="mathjax")

import io
from PIL import Image as PILImage
from sympy import Basic

ip = get_ipython()

from sympy import Basic
from IPython.display import Image, display
import io

ip = get_ipython()

def sympy_display(expr):
    buf = io.BytesIO()
    sy.preview(expr, output='png', viewer='BytesIO', outputbuffer=buf, dvioptions=['-D', '400', '-fg', 'rgb 1.0 1.0 1.0', '-bg', 'Transparent'])
    return buf.getvalue()

ip.display_formatter.formatters['image/png'].for_type(Basic, sympy_display)

def sy_symbols():
    global x,y,z,a,b,c,t,d,i,j,k,n,hA,hB,hH

    x,y,z,a,b,c,t,d = sy.symbols("x,y,z,a,b,c,t,d")
    i,j,k,n = sy.symbols("i,j,k,n", integer=True)
    hA= sy.Symbol('\hat A', commutative = False)
    hB= sy.Symbol('\hat B', commutative = False)
    hH= sy.Symbol('\hat H', commutative = False)

def start():
    print(
        """
    MathPy:
        Reminder:
        - sp: scipy
        - sy: sympy
        - np: numpy
        - ureg: pint.UnitRegistry

        Solve:
        - Analytical: syp.solve(expr_that_is_zero,variable_to_solve_for)
        - Numerical: sip.optimize.fsolve(expr_that_is_zero,initial_guess)

        Get Help:
        - help(np.function): Get help for the function
        - np.lookfor('keyword'): Search for keyword in numpy documentation

        General:
        - _: Last output
        - __: Second to last output
        - __x__: x-th output
        - %history: Show history
        - %reset: Reset the namespace
        - %who: Show all variables in the namespace
        - sci(number): Scientific notation of number

        Extras:
        - load_quantum: Loads quantum mechanis functions
            - Sympy quantum as sypqm
            - QUtip as qtp
        - print_self: Prints this file
        - sy_symbols: Defines many sympy variables
       """
    )
start()

# Define some neat formatings
def sci(number):
    return "{:.2e}".format(number)


def load_quantum():
    global qtp
    global sypqm
    global sypqm_pauli

    import qutip as qtp
    import sympy.physics.quantum as sypqm
    import sympy.physics.paulialgebra as sypqm_pauli


    print("Quantum Mechanics functions loaded")


def print_self():
    import os

    filepath = "/mnt/SSHD/Speicher/02_Code/Random/utils/mathpy.py"
    with open(filepath, "r") as file:
        print(file.read())
