"""Label class for displaying text"""

import tkinter as tk
from typing import Optional


class Label:
    """Label widget for displaying text"""
    
    def __init__(
        self,
        parent: tk.Widget,
        text: str,
        font: Optional[tuple] = None,
        fg: Optional[str] = None,
        bg: Optional[str] = None,
        anchor: Optional[str] = None
    ):
        """Initialize label"""
        self.label = tk.Label(
            parent,
            text=text,
            font=font,
            fg=fg,
            bg=bg,
            anchor=anchor
        )
        
        # Store properties
        self.text = text
    
    def pack(self, **kwargs) -> None:
        """Pack label into parent"""
        self.label.pack(**kwargs)
    
    def grid(self, row: int, column: int, **kwargs) -> None:
        """Grid label into parent"""
        self.label.grid(row=row, column=column, **kwargs)
    
    def set_text(self, text: str) -> None:
        """Set label text"""
        self.text = text
        self.label.config(text=text)
    
    def set_font(self, font: tuple) -> None:
        """Set label font"""
        self.label.config(font=font)
    
    def set_color(self, fg: str, bg: str) -> None:
        """Set label colors"""
        self.label.config(fg=fg, bg=bg)