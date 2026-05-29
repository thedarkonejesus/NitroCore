"""
Application lifecycle guardrails, handling single-instance enforcement 
and emergency OS handle cleanups.
"""

import sys
import atexit
from typing import Optional

# Platform-specific check to ensure safety if tested cross-platform
IS_WINDOWS = sys.platform == "win32"

if IS_WINDOWS:
    import win32event
    import win32api
    import winerror

class LifecycleManager:
    """Manages system-level single instance constraints and process teardowns."""
    
    _mutex: Optional[object] = None

    @classmethod
    def enforce_single_instance(cls) -> None:
        """
        Guarantees only one instance of the optimizer runs at a time.
        Prevents simultaneous write race conditions on system registries.
        """
        if not IS_WINDOWS:
            return

        # Unique global named identifier for the kernel mutex object
        cls._mutex = win32event.CreateMutex(None, False, "Global\\NitroCore_SingleInstance_Mutex")
        
        # If the mutex handle already exists, another instance is running
        if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
            cls._mutex = None
            print("[Lifecycle] NitroCore is already running. Exiting current process.")
            sys.exit(0)

    @staticmethod
    def register_emergency_cleanup(cleanup_callback: callable) -> None:
        """
        Registers an emergency handler to safely release low-level 
        system pointers if the app shuts down unexpectedly.
        """
        atexit.register(cleanup_callback)
