"""
Hide the input cells in a notebook.

To use, place the following in your notebook:

from IPython.display import HTML
from toggle_input import toggle_input
HTML(toggle_input)
"""

from __future__ import absolute_import, division, print_function

from .toggle_input import *

from .version import __version__
