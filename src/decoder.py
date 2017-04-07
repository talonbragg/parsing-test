# coding=utf-8
from abc import ABCMeta, abstractmethod

class BaseDecoder:
    """Abstract base class for building decoders."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def decode(self, message: str) -> dict:
        """
        Decodes a message.
        """
        pass


# YOUR CLASS GOES HERE
#         V


class MetarDecoder(BaseDecoder):
    """Your decoder object goes here."""

    def decode(self, message: str) -> dict:
        """Your method documentation goes here."""

        # Your code here!
        pass
