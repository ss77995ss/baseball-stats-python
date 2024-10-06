from enum import Enum


class EnumBase(Enum):
    def __str__(self):
        return self.value

    @classmethod
    def has_value(cls, value):
        return str(value) in cls._value2member_map_

    @classmethod
    def get_all(cls):
        return '|'.join(cls._value2member_map_)
