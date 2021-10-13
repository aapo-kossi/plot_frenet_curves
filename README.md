# plot_frenet_curves
Python script that draws 3d curves with user-defined curvature and torsion. Easy to use from a command terminal with the help of python argparser.

## Built with
* [python 3.8.8](https://www.python.org/)
* [numpy 1.19.2](https://numpy.org/)
* [matplotlib 3.3.1](https://matplotlib.org/)

## Installation
1. Make sure you have [python 3.X](https://www.python.org/downloads/) installed
2. Download the code from this repository from the "download ZIP" button in the top right part of the repository front page  
    1. Unzip the download into your desired folder
2. **Optional**: Create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html) to run the script in isolation from other projects
    1. Open a command terminal (for UNIX-based systems this guide assumes bash as the terminal, not csh or fish!)
    2. run the command `python -m venv [c:/path/to/your/desired/folder]`  
    3. activate the new environment by running `source [path to venv specified before]/activate`  
        1. Note: for Windows you need to run `activate.bat` if using a command terminal or `activate.ps1` for powershell
4. Install Numpy and Matplotlib
    1. This is done easiest using pip, the package installer included with python starting from version 3.4  
    2. run the command `pip install numpy` in a command terminal, if using a venv make sure you have activated it
    3. run the command `pip install matplotlib`    
 5. You're ready to go! view the help message for the plotting script  
 by navigating to the script location in your command terminal using `cd [c:/path/to/target]`  
 and running `python plot_from_k_and_t.py --help`

## Usage
To run the program using command line terminal (for example bash for UNIX-based systems,  
such as MacOS of LINUX or the command prompt for Windows) you must first navigate  
to the script location with the command `cd [path to script folder]`, and run the script  
with the command `python plot_from_k_and_t.py [arguments]`, where you define the plotted curve  
with arguments as follows:  

The first argument is required as it defines the curvature of the curve *u(s)* at point *s*.  
This argument must be specified immediately after the name of the script, before any optional arguments.  
The curvature can be written using python multiplication (\*), division (/), exponent (\*\*) and  
sum (+ or -). As the parameter for curvature and torsion, always use `s_`,  
which will also be the resulting curve length. An example using only the required argument is  
`python plot_from_k_and_t.py (1+s_)**-1-1/10*(0.1+(15-s_)**2)**-0.5`,  
for which the resulting plot resembles a cresting wave. Note that you cannot use whitespace inside your arguments,  
as argparse interprets it as a delimiter between different arguments. You can also note that even though  
the curvature explodes near *s = -1*, the script successfully plots a curve. This behaviour allows more freedom  
to the user, but care must be taken as the resulting curves cannot be accurate in cases where kappa or tau are  
badly defined. Moreover, in contrast to the true Frenet frame this script can calculate paths  
with 0 and negative curvatures successfully, but the resulting plots cannot be guaranteed to represent  
anything meaningful (do they really?).  
**If the user desires to approximate an actual Frenet frame, they need to ensure that the curvature satisfies kappa > 0.**  
Additionally you can use [mathematical functions defined by numpy](https://numpy.org/doc/stable/reference/routines.math.html)  
by typing `np.[function]([input expressions])`, for example `np.sin(10*s_)`.  
The most important optional argument is `--tau`, torsion of the curve at point *s*. When specifying  
optional arguments, the syntax is `--[name of argument] [argument value]`, for example `--tau 5*s_`.  
If unspecified, the script will plot a curve with 0 torsion in R^3 space.  
With the limits argument you can specify the interval *c: (a,b) -> R^3*  
with the syntax `--limits [a] [b]`.  
You can also ensure the curve is not distorted by different scales on the x, y and z axes  
by specifying the argument `--equal_scaling`.

## Examples
input:
`python plot_from_k_and_t.py 1 --tau 0.25 --equal_scaling`  
output:  
![helix1](https://user-images.githubusercontent.com/81294037/137204561-6ed2f864-a7ef-423b-8775-287aba4b8b86.png)  
input:
`python plot_from_k_and_t.py s_`  
output:  
![eulerspiral1](https://user-images.githubusercontent.com/81294037/137204859-c1063cc9-07a3-4453-9317-bc238e9e5860.png)  
input:
`python plot_from_k_and_t.py 10*np.sin(np.exp(s_)/5) --tau abs(s_) --limits -5 5`  
output:  
![weirdcurve](https://user-images.githubusercontent.com/81294037/137205925-c884ceac-78af-4c3e-b14e-ce77f490f9ea.png)
