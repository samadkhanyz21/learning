class Device:

    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print('Disconnected')


class Printer(Device):

    """Device is parent class and Printer is child class or
    better known as class inheritance"""
    def __init__(self, name, connected_by, capacity):
        """We can either copy and paste from Device
        or use a more efficient way by using a super
        class"""
        super().__init__(name, connected_by)
        # Max_capacity of printer
        self.capacity = capacity
        # Remaining capacity of printer
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print('Your printer is not connected!')
            return
        print(f"Printing {pages} pages")
        self.remaining_pages = pages


printer = Printer('Printer', 'USB', 500)
printer.print(29)
print(Printer)
