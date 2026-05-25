import psutil
import shutil

class DiskCleanup:
    def __init__(self):
        self.min_disk_space = 10  # GB minimum
    
    def get_disk_usage(self):
        """Get current disk usage statistics"""
        partitions = psutil.disk_partitions()
        usage = {}
        for partition in partitions:
            try:
                usage[partition.device] = psutil.disk_usage(partition.mountpoint)
            except Exception as e:
                print(f"Error getting usage for {partition.device}: {e}")
        return usage
    
    def clean_system_files(self):
        """Clean system temporary files"""
        try:
            subprocess.run(['cleanmgr', '/sagerun:1'], check=True)
            return True
        except Exception as e:
            print(f"Error cleaning system files: {e}")
            return False
    
    def clean_downloads(self):
        """Clean downloads folder of old files"""
        downloads = os.path.expandvars('%USERPROFILE%\\Downloads')
        cutoff_date = datetime.now() - timedelta(days=30)
        
        cleaned_files = []
        for root, dirs, files in os.walk(downloads):
            for f in files:
                file_path = os.path.join(root, f)
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_time < cutoff_date:
                    try:
                        os.remove(file_path)
                        cleaned_files.append(file_path)
                    except Exception as e:
                        print(f"Error removing {file_path}: {e}")
        return cleaned_files