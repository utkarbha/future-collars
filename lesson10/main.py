class Device:
    DEVICE_TYPE = None
    DEVICE_BRAND = None

    def __init__(self, ram_size, serial_number, connection_types):
        self.connection_types = connection_types
        self.ram_size = ram_size
        self.serial_number = serial_number

    @property
    def information(self):
            return f"{self.DEVICE_TYPE}: SN-  {self.serial_number} {self.DEVICE_BRAND} {self.connection_types}"

class Smartphone(Device):
    DEVICE_TYPE = "Smartphone"

class Tablet(Device):
    DEVICE_TYPE = "Tablet"

class Laptop(Device):
    DEVICE_TYPE = "Laptop"

class SmartphoneSamsung(Smartphone):
    DEVICE_BRAND = "Samsung"



class SmartphoneLG(Smartphone):
    DEVICE_BRAND = "LG"


class IpadTablet(Tablet):
    DEVICE_BRAND = "Apple"

class ConnectionTypes:
    def __init__(self, bluetooth=False, wifi=False, nfc=False):
        self.bluetooth = bluetooth
        self.wifi = wifi
        self.nfc = nfc

    def __str__(self):
        base = ""
        if self.bluetooth:
            base += "Bluetooth: Yes; "

        if self.wifi:
            base += "Wifi: Yes; "

        if self.nfc:
            base += "NFC: Yes; "

        return f"{base}"
        # return f"Bluetooth : {self.bluetooth}, WiFi : {self.wifi}, NFC : {self.nfc}"




# smartphone1 = SmartphoneSamsung( 2048, "QWE-ASD-ZXC-ASD-QWE", ConnectionTypes(True, True, True))
# print(smartphone1.information)

smartphone2 = SmartphoneLG( 2048, "QWE-ASD-ZXC-ASD-QWE", ConnectionTypes(True, False, True))
print(smartphone2.information)

# smartphone3 = SmartphoneSamsung( 2048, "abdladbdaQWE-ASD-ZXC-ASD-QWE", ConnectionTypes(False, True))
# print(smartphone3.information)
#
# tablet1 = IpadTablet( 4064, "agsahaas-adasd", ConnectionTypes(wifi=True))
# print(tablet1.information)
#
# tablet2 = Tablet( 4064, "agsahaas-adasd", ["bluetooth", "nfc"])
# print(tablet2.information)


