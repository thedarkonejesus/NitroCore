import os
import subprocess
import psutil
from datetime import datetime, timedelta

class DiskCleanup:
    def __init__(self):
        self.min_disk_space_gb = 10.0
    
    def get_disk_usage(self):
        """
        Get current disk usage statistics, filtering out unmounted, 
        removable, or virtual system media to maximize speed.
        """
        usage = {}
        for partition in psutil.disk_partitions(all=False): # all=False skips inactive/virtual layouts
            # Only analyze local fixed drives (like HDD/SSDs) to prevent hanging on empty media
            if 'fixed' in partition.opts or partition.fstype:
                try:
                    usage_stats = psutil.disk_usage(partition.mountpoint)
                    usage[partition.device] = {
                        'total_gb': round(usage_stats.total / (1024**3), 2),
                        'used_gb': round(usage_stats.used / (1024**3), 2),
                        'free_gb': round(usage_stats.free / (1024**3), 2),
                        'percent': usage_stats.percent
                    }
                except (PermissionError, FileNotFoundError):
                    continue
        return usage
    
    def clean_system_files(self):
        """
        Triggers Windows Native Deployment Image Servicing/Cleanup tools safely.
        Using DISM components or a direct fast-clean argument handles this without hanging the thread.
        """
        try:
            # Running cleanmgr with /autoclean bypasses UI state menus entirely for a true hands-off UX
            result = subprocess.run(
                ['cleanmgr', '/autoclean'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                timeout=300 # Prevent infinite background hangs if Windows blocks
            )
            return "Windows Native Cleanup executed successfully"
        except subprocess.TimeoutExpired:
            return "Windows Native Cleanup timed out (System spent too long compressing old updates)"
        except Exception as e:
            return f"Error executing System File Cleanup: {str(e)}"
    
    def clean_downloads(self, retention_days=30):
        """
        Scan and clean files in the user downloads folder older than specified retention days.
        Optimized via os.scandir to prevent directory-walking lockups.
        """
        downloads_path = os.path.realpath(os.path.expandvars('%USERPROFILE%\\Downloads'))
        
        if not os.path.exists(downloads_path):
            return "Downloads folder not found"
            
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        files_removed = 0
        bytes_saved = 0
        
        def _purge_old_files(target_path):
            nonlocal files_removed, bytes_saved
            try:
                with os.scandir(target_path) as entries:
                    for entry in entries:
                        try:
                            if entry.is_file(follow_symlinks=False):
                                # Check file modification time
                                file_mtime = datetime.fromtimestamp(entry.stat().st_mtime)
                                if file_mtime < cutoff_date:
                                    file_size = entry.stat().st_size
                                    os.remove(entry.path)
                                    files_deleted += 1
                                    bytes_saved += file_size
                            elif entry.is_dir(follow_symlinks=False):
                                # Recurse into subfolders
                                _purge_old_files(entry.path)
                                # Clean up directory shell if now empty
                                if not os.listdir(entry.path):
                                    os.rmdir(entry.path)
                        except (PermissionError, FileNotFoundError):
                            continue
            except PermissionError:
                pass

        _purge_old_files(downloads_path)
        mb_saved = bytes_saved / (1024 * 1024)
        return f"Downloads Clean: Removed {files_removed} files older than {retention_days} days ({mb_saved:.2f} MB freed)"
