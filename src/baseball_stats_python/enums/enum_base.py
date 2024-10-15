from enum import Enum


class EnumBase(Enum):
    def __str__(self):
        return self.value

    @classmethod
    def has_value(cls, value):
        """Check if the value is in the enum."""
        return str(value) in cls._value2member_map_

    @classmethod
    def join_all(cls):
        """Join all the values in the enum."""
        return '|'.join(cls._value2member_map_)
