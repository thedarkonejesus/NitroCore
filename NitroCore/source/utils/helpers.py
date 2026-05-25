"""Helper functions for common operations"""

import re
import hashlib
import uuid
import functools
import time
from typing import Callable, Any, Optional, TypeVar
from pathlib import Path


# Type variables for decorators
T = TypeVar('T')


def is_valid_ip(ip: str) -> bool:
    """Check if string is valid IP address"""
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(ip_pattern, ip):
        return False
        
    parts = ip.split('.')
    return all(0 <= int(part) <= 255 for part in parts)


def is_valid_email(email: str) -> bool:
    """Check if string is valid email address"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))


def sanitize_input(input_str: str) -> str:
    """Sanitize input string for security"""
    # Remove potentially dangerous characters
    sanitized = re.sub(r'[^\w\s\-\.]', '', input_str)
    return sanitized.strip()


def hash_password(password: str, algorithm: str = 'sha256') -> str:
    """Hash password using specified algorithm"""
    hash_func = getattr(hashlib, algorithm)
    return hash_func(password.encode()).hexdigest()


def generate_uuid() -> str:
    """Generate UUID string"""
    return str(uuid.uuid4())


def retry_on_failure(max_retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry function on failure"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay)
            
            raise last_exception
        return wrapper
    return decorator


def memoize(func: Callable) -> Callable:
    """Decorator to memoize function results"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            return cache[key]
            
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper


def validate_path(path: str) -> bool:
    """Validate file/directory path"""
    try:
        p = Path(path)
        return p.exists() and (p.is_file() or p.is_dir())
    except Exception:
        return False


def ensure_directory_exists(path: str) -> None:
    """Ensure directory exists, create if needed"""
    Path(path).mkdir(parents=True, exist_ok=True)