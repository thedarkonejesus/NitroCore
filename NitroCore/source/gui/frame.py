"""Frame class for grouping widgets"""

import tkinter as tk
from typing import Optional


class Frame:
    """Frame container for grouping widgets"""
    
    def __init__(
        self,
        parent: tk.Widget,
        bg: Optional[str] = None,
        borderwidth: Optional[int] = None,
        relief: Optional[str] = None
    ):
        """Initialize frame"""
        self.frame = tk.Frame(
            parent,
            bg=bg,
            borderwidth=borderwidth,
            relief=relief
        )
        
        # Store properties
        self.bg = bg
    
    def pack(self, **kwargs) -> None:
        """Pack frame into parent"""
        self.frame.pack(**kwargs)
    
    def grid(self, row: int, column: int, **kwargs) -> None:
        """Grid frame into parent"""
        self.frame.grid(row=row, column=column, **kwargs)
    
    def set_background(self, color: str) -> None:
        """Set frame background color"""
        self.bg = color
        self.frame.config(bg=color)
    
    def add_widget(self, widget: tk.Widget) -> None:
        """Add widget to frame"""
        widget.pack(in_=self.frame)