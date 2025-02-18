#
#   This file is part of do-mpc
#
#   do-mpc: An environment for the easy, modular and efficient implementation of
#        robust nonlinear model predictive control
#
#   Copyright (c) 2014-2019 Sergio Lucia, Alexandru Tatulea-Codrean
#                        TU Dortmund. All rights reserved
#
#   do-mpc is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as
#   published by the Free Software Foundation, either version 3
#   of the License, or (at your option) any later version.
#
#   do-mpc is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with do-mpc.  If not, see <http://www.gnu.org/licenses/>.

"""
Various auxiliary tools for do-mpc.
"""


import pickle

from ._indexedproperty import IndexedProperty
from ._structure import Structure
from ._casstructure import *
# from ._dae2odeconversion import *
from ._timer import Timer


def save_pickle(filename, data):
    filename = filename.replace('.pkl','')
    with open(filename + '.pkl', 'wb') as f:
        pickle.dump(data, f)

def load_pickle(path_to_file):
    with open(path_to_file, 'rb') as f:
        data = pickle.load(f)
    return data


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Print a progress bar to the console.

    :param iteration: Current iteration
    :type iteration: int
    :param total: Total iterations
    :type total: int
    :param prefix: Prefix string
    :type prefix: str
    :param suffix: Suffix string
    :type suffix: str
    :param decimals: Positive number of decimals in percent complete
    :type decimals: int
    :param length: Character length of bar
    :type length: int
    :param fill: Bar fill character
    :type fill: str
    :param printEnd: End character (e.g. "\r")
    :type printEnd: str

    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
