import os
import subprocess
import psutil

class PerformanceTuner:
    def __init__(self):
        # GUID templates for performance profiles
        self.high_perf_guid = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
        # Ultimate Performance GUID (Hidden by default on many machines, but unlocked below)
        self.ultimate_perf_guid = "e9a42b02-d5df-448d-aa00-03f14749eb61"

    def set_process_priority(self):
        """
        Safely adjusts execution priority levels for critical interface components 
        in-memory without killing the process or risking a system black-screen.
        """
        target_processes = ['explorer.exe', 'dwm.exe']
        adjusted_count = 0
        
        # Iterate through actively running system processes
        for proc in psutil.process_iter(['name', 'pid']):
            try:
                if proc.info['name'] and proc.info['name'].lower() in target_processes:
                    p = psutil.Process(proc.info['pid'])
                    # Set to ABOVE_NORMAL_PRIORITY_CLASS instead of HIGH to prevent 
                    # mouse/keyboard hardware input starvation loops.
                    p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
                    adjusted_count += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
                
        return f"Process Tuning: Adjusted {adjusted_count} system components to High Responsiveness"

    def optimize_power_plan(self):
        """
        Unlocks and activates the highest performing power configuration schema 
        available on the host architecture.
        """
        try:
            # 1. Attempt to unlock the 'Ultimate Performance' scheme overlay if it's hidden
            subprocess.run(
                ["powercfg", "-duplicatescheme", self.ultimate_perf_guid],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.get_terminal_size  # Avoid console popups on newer Pythons or use creationflags directly
            ) if os.name == 'nt' else None
            
            # Use specific flag to hide window on Windows
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            # 2. Try to activate Ultimate Performance
            result = subprocess.run(
                ["powercfg", "/s", self.ultimate_perf_guid],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                startupinfo=startupinfo,
                check=True
            )
            return "Power Plan: Switched to Ultimate Performance"
            
        except subprocess.CalledProcessError:
            # Fallback to standard High Performance if Ultimate is restricted by hardware policy
            try:
                subprocess.run(
                    ["powercfg", "/s", self.high_perf_guid],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    startupinfo=startupinfo,
                    check=True
                )
                return "Power Plan: Switched to High Performance (Standard)"
            except Exception as e:
                return f"Power Plan Error: System rejected profile schema changes: {str(e)}"
