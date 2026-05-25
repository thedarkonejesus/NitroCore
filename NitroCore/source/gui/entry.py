"""Entry class for text input fields"""

import tkinter as tk
from typing import Optional, Callable


class Entry:
    """Entry widget for text input"""
    
    def __init__(
        self,
        parent: tk.Widget,
        placeholder: Optional[str] = None,
        width: Optional[int] = None,
        font: Optional[tuple] = None,
        show: Optional[str] = None
    ):
        """Initialize entry"""
        self.entry = tk.Entry(parent, width=width, font=font, show=show)
        self.placeholder = placeholder
        
        # Add placeholder if provided
        if placeholder:
            self.set_placeholder(placeholder)
        
        # Store properties
        self.value = ""
        self.on_change_callbacks = []
    
    def pack(self, **kwargs) -> None:
        """Pack entry into parent"""
        self.entry.pack(**kwargs)
    
    def grid(self, row: int, column: int, **kwargs) -> None:
        """Grid entry into parent"""
        self.entry.grid(row=row, column=column, **kwargs)
    
    def set_placeholder(self, placeholder: str) -> None:
        """Set placeholder text"""
        self.placeholder = placeholder
        self.entry.insert(0, placeholder)
        self.entry.config(fg='gray')
        
        def clear_placeholder(event):
            if self.entry.get() == placeholder:
                self.entry.delete(0, tk.END)
                self.entry.config(fg='black')
        
        def restore_placeholder(event):
            if not self.entry.get():
                self.entry.insert(0, placeholder)
                self.entry.config(fg='gray')
        
        self.entry.bind("<FocusIn>", clear_placeholder)
        self.entry.bind("<FocusOut>", restore_placeholder)
    
    def get_value(self) -> str:
        """Get entry value"""
        return self.entry.get()
    
    def set_value(self, value: str) -> None:
        """Set entry value"""
        self.value = value
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
    
    def add_change_callback(self, callback: Callable[[str], None]) -> None:
        """Add callback for value change"""
        self.on_change_callbacks.append(callback)
    
    def _trigger_change(self) -> None:
        """Trigger change callbacks"""
        value = self.get_value()
        for callback in self.on_change_callbacks:
            callback(value)
    
    def _bind_events(self) -> None:
        """Bind events to track changes"""
        self.entry.bind("<KeyRelease>", lambda _: self._trigger_change())