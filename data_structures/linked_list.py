from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


@dataclass
class RandomNode:
    val: int = 0
    next: Optional["ListNode"] = None
    random: Optional["ListNode"] = None
