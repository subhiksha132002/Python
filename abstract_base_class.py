from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass

# Base class


class Stream(ABC):
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

    @abstractmethod
    def read(self):
        pass

# sub class


class DataStream(Stream):
    def read(self):
        print("data stream")

# sub class


class NetworkStream(Stream):
    def read(self):
        print("network stream")


class MemoryStream(Stream):
    def read(self):
        print("memory stream")


stream = MemoryStream()
stream.read()
