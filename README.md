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
