""" pyodv

.. module:: pyodv
    :synopsis: Python package for reading ODV (Ocean Data Variables) files

.. moduleauthor:: Rory Meyer <rory.meyer@vliz.be>

"""

from .base import MyModel
from .__version__ import __version__
import logging

__all__ = ['MyModel', '__version__']

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
