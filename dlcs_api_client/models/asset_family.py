from enum import IntEnum


class AssetFamily(IntEnum):
    VALUE_70 = 70
    VALUE_73 = 73
    VALUE_84 = 84

    def __str__(self) -> str:
        return str(self.value)
