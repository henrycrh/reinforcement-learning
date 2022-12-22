from enum import Enum, auto
from goods.apple import AppleBase
from investments.apple_tree import AppleTreeBase


# For new items, add the Item Base to the end of either the
# Goods or Investments section depending on the new item.
# Also add a constant under either the Goods or Investments section
# assigned to auto() for item-to-index mappings
GOODS = []

CLASS_TO_INDEX
class Items(Enum):
    GOODS = [
        AppleBase()
    ]

    INVESTMENTS = [
        AppleTreeBase()
    ]

    ITEMS = GOODS + INVESTMENTS

    # Goods
    APPLE = 0
    ORANGE = auto()

    # Investments
    APPLE_TREE = auto()

