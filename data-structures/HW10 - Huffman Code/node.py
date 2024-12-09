#!/usr/bin/env python3

from typing import Optional

class Node:
    def __init__(
            self, 
            key: str, 
            value: int = 0, 
            left: Optional['Node'] = None, 
            right: Optional['Node'] = None
            ) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    def __eq__(self, other: 'Node') -> bool:
        return self.value == other.value

    def __gt__(self, other: 'Node') -> bool:
        return self.value > other.value
        
    def __ge__(self, other: 'Node') -> bool:
        return self.value >= other.value
    
    def __lt__(self, other: 'Node') -> bool:
        return self.value < other.value
    
    def __le__(self, other: 'Node') -> bool:
        return self.value <= other.value
    
