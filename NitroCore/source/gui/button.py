"""Button class for creating buttons"""

import tkinter as tk
from typing import Callable, Optional, Any


class Button:
    """Button widget with click handler support"""
    
    def __init__(
        self,
        parent: tk.Widget,
        text: str,
        command: Optional[Callable] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        bg: Optional[str] = None,
        fg: Optional[str] = None,
        font: Optional[tuple] = None
    ):
        """Initialize button"""
        self.button = tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            height=height,
            bg=bg,
            fg=fg,
            font=font
        )
        
        # Store properties
        self.text = text
        self.command = command
        self.enabled = True
    
    def pack(self, **kwargs) -> None:
        """Pack button into parent"""
        self.button.pack(**kwargs)
    
    def grid(self, row: int, column: int, **kwargs) -> None:
        """Grid button into parent"""
        self.button.grid(row=row, column=column, **kwargs)
    
    def set_command(self, command: Callable) -> None:
        """Set button command"""
        self.command = command
        self.button.config(command=command)
    
    def enable(self) -> None:
        """Enable button"""
        self.enabled = True
        self.button.config(state='normal')
    
    def disable(self) -> None:
        """Disable button"""
        self.enabled = False
        self.button.config(state='disabled')
    
    def set_text(self, text: str) -> None:
        """Set button text"""
        self.text = text
        self.button.config(text=text)