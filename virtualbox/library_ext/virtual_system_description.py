import time
import os

import virtualbox
from virtualbox import library
from virtualbox.library import VirtualSystemDescriptionType as DescType

"""
Add helper code to the default IVirtualSystemDescription class.
"""


class IVirtualSystemDescription(library.IVirtualSystemDescription):
    __doc__ = library.IVirtualSystemDescription.__doc__

    def set_final_value(self, description_type, value):
        "Set the value for the given description type"
        types, _, _, vbox_values, extra_config = self.get_description()

        # find offset to Name
        offset = 0
        for offset, t in enumerate(types):
            if t == description_type:
                break
        else:
            raise Exception("Failed to find name type")

        enabled = [True] * len(types)
        vbox_values = list(vbox_values)
        extra_config = list(extra_config)
        vbox_values[offset] = value 
        self.set_final_values(enabled, vbox_values, extra_config)

    def set_name(self, value):
        "Set the name of the appliance (name of machine when imported)."
        self.set_final_value(DescType.name, value)

    def set_cpu(self, value):
        "Set cpu value."
        self.set_final_value(DescType.cpu, value)

    def set_memory(self, value):
        "Set memory value."
        self.set_final_value(DescType.memory, value)

    def set_soundcard(self, value):
        "Set soundcard value."
        self.set_final_value(DescType.sound_card, value)

    def set_usb_controller(self, value):
        "Set usb controller value."
        self.set_final_value(DescType.usb_controller, value)

    def set_network_adapter(self, value):
        "Set network_adapter value."
        self.set_final_value(DescType.network_adapter, value)

    def set_cdrom(self, value):
        "Set cdrom value."
        self.set_final_value(DescType.cdrom, value)

    def set_hard_disk_controller_ide(self, value):
        "Set hard_disk_controller_ide value."
        self.set_final_value(DescType.hard_disk_controller_ide, value)

    def set_hard_disk_controller_sas(self, value):
        "Set hard_disk_controller_sas value."
        self.set_final_value(DescType.hard_disk_controller_sas, value)

    def set_hard_disk_controller_sata(self, value):
        "Set hard_disk_controller_sata value."
        self.set_final_value(DescType.hard_disk_controller_sata, value)

    def set_hard_disk_controller_scsi(self, value):
        "Set hard_disk_controller_scsi value."
        self.set_final_value(DescType.hard_disk_controller_scsi, value)

    def set_hard_disk_image(self, value):
        "Set hard_disk_image value."
        self.set_final_value(DescType.hard_disk_image, value)





