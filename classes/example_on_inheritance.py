class InvalidOperationError(Exception):
    pass

# Base class


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

# sub class


class DataStream(Stream):
    def read(self):
        print("data stream")

# sub class


class NetworkStream(Stream):
    def read(self):
        print("network stream")


data = DataStream()
data.read()
network = NetworkStream()
network.read()


# There is no muti level  inheritance here
# simple  inheritance - base class and 2 sub classes
# Multiple inheritance - no common method so even if we use it,no problem we will face in future
