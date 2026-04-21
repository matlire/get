import smbus

class MCP4725:
    def __init__ (self, dynamic_range: float, address=0x61, verbose = True) -> None:
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm      = 0x00
        self.pds     = 0x0

        self.dynamic_range = dynamic_range
        self.verbose       = verbose

        self.dac_depth = 12

    def deinit(self) -> None:
        self.bus.close()

    def set_number(self, number: int) -> None:
        if not (0 <= number <= 2**self.dac_depth - 1):
            print("Number can't be more then MCP4725 size (12 bits)")
        first_byte  = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)

        if self.verbose:
            print(f"Number: {number} sent by I2C data: [0x{(self.address << 1):02X}, 0x{second_byte:02x}]\n")

    def set_voltage(self, voltage: float) -> None:
        if (not (0.0 <= voltage <= self.dynamic_range)):
            print(f"Voltage is out of range: 0 - {self.dynamic_range}\nSetting 0.0V")
            return
        number = int(voltage / self.dynamic_range * 2**self.dac_depth)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = MCP4725(4.95)

        while True:
            try:
                voltage = float(input("Enter voltage: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("You entered Nan. Try again.\n")
    finally:
        dac.deinit()
