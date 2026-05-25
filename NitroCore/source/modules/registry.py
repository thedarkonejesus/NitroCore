import winreg
import os

class RegistryOptimizer:
    def __init__(self):
        self.optimization_rules = {
            'disable_hibernation': self._disable_hibernation,
            'disable_pagefile': self._disable_pagefile,
            'optimize_performance': self._optimize_performance
        }
    
    def _disable_hibernation(self):
        """Disable hibernation to free up disk space"""
        try:
            subprocess.run(['powercfg', '/hibernate', 'off'], check=True)
            return True
        except Exception as e:
            print(f"Error disabling hibernation: {e}")
            return False
    
    def _optimize_performance(self):
        """Apply Windows performance optimizations"""
        perf_settings = {
            'VisualFX': 2,  # Adjust visual effects
            'Priority': 5   # Set process priority
        }
        
        for key, value in perf_settings.items():
            try:
                self._set_registry_value(key, value)
            except Exception as e:
                print(f"Error setting {key}: {e}")
        return True
    
    def apply_all(self):
        """Apply all registry optimizations"""
        results = {}
        for name, func in self.optimization_rules.items():
            results[name] = func()
        return results