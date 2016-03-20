#
#      Open Source SAM-BA Programmer
#     Copyright (C) Dean Camera, 2016.
#
#  dean [at] fourwalledcubicle [dot] com
#       www.fourwalledcubicle.com
#
#
# Released under a MIT license, see LICENCE.txt.

import abc


class Transport(object):
    """Base class for SAM-BA transports. Derived instances should override all
       methods listed here.
    """

    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def read(self, length=None):
        """Reads a given number of bytes from the transport.

            Args:
                length : Number of bytes to read. If `None`, a full line will be
                         read until a terminator is reached.

            Returns:
                Byte array of the received data.
        """
        pass


    @abc.abstractmethod
    def write(self, data):
        """Writes a given number of bytes to the transport.

            Args:
                data : Bytes to write.
        """
        pass
