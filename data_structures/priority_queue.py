from dataclasses import dataclass, field
from typing import Any


# Reference: https://docs.python.org/3/library/heapq.html
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)
