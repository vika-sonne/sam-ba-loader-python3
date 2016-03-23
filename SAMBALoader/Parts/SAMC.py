#
#      Open Source SAM-BA Programmer
#     Copyright (C) Dean Camera, 2016.
#
#  dean [at] fourwalledcubicle [dot] com
#       www.fourwalledcubicle.com
#
#
# Released under a MIT license, see LICENCE.txt.

import Part
import CortexM0p


@Part.UntestedPart
class ATSAMC(CortexM0p.CortexM0p):
    """Part class for all SAM C series parts."""

    @staticmethod
    def identify(id_name, id_values):
        """Determines if the given chip identifiers positively identify a SAM C
           series device.

           Args:
              id_name   : Name of the chip identifier being tested.
              id_values : Chip identifier values extracted from the part.

           Returns:
               `True` if the given identifiers suggest the part is a SAM C
               series device.
        """
        return id_name == "DSU" and id_values.processor == 1 and id_values.family == 2 and id_values.series == 1
