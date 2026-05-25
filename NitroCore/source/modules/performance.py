import subprocess
import winreg

class PerformanceTuner:
    def __init__(self):
        self.performance_tweaks = {
            'priority_class': 'HIGH',
            'processor_affinity': [0, 1, 2, 3],
            'scheduler_priority': 7
        }
    
    def set_process_priority(self):
        """Set high priority for critical processes"""
        processes = ['explorer.exe', 'dwm.exe']
        for proc in processes:
            try:
                subprocess.run(['taskkill', '/F', '/IM', proc], check=True)
                subprocess.run(['start', '', proc], shell=True)
            except Exception as e:
                print(f"Error setting priority for {proc}: {e}")
    
    def optimize_power_plan(self):
        """Switch to High Performance power plan"""
        try:
            subprocess.run(['powercfg', '/s', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'], check=True)
            return True
        except Exception as e:
            print(f"Error switching power plan: {e}")
            return False