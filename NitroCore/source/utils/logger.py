"""Logging utilities for consistent logging across applications"""

import logging
import logging.handlers
import os
from pathlib import Path
from typing import Optional, Union


class Logger:
    """Logger class with configurable levels and handlers"""
    
    def __init__(self, name: str = 'app', level: int = logging.INFO):
        """Initialize logger with name and level"""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Prevent duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers()
    
    def _setup_handlers(self) -> None:
        """Setup console and file handlers"""
        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / 'app.log'
        
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=10*1024*1024, backupCount=5
        )
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
    
    def debug(self, msg: str) -> None:
        """Log debug message"""
        self.logger.debug(msg)
    
    def info(self, msg: str) -> None:
        """Log info message"""
        self.logger.info(msg)
    
    def warning(self, msg: str) -> None:
        """Log warning message"""
        self.logger.warning(msg)
    
    def error(self, msg: str) -> None:
        """Log error message"""
        self.logger.error(msg)
    
    def critical(self, msg: str) -> None:
        """Log critical message"""
        self.logger.critical(msg)
    
    @classmethod
    def get_logger(cls, name: str = 'app') -> 'Logger':
        """Get logger instance"""
        return cls(name)