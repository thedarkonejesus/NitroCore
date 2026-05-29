import win32service
import win32serviceutil
import pywintypes

class ServiceManager:
    def __init__(self):
        # Services typically targeted for a gaming/performance profile
        self.services_to_optimize = [
            'wuauserv',      # Windows Update
            'BITS',          # Background Intelligent Transfer Service
            'WSearch'        # Windows Search Indexer
        ]
        
    def optimize_all_services(self):
        """
        Main runner block to stop target services and set their startup type to manual.
        Returns a formatted multi-line summary string for the UI log.
        """
        results = []
        
        # Open a connection to the Service Control Manager (SCM) with full access privileges
        try:
            scm_handle = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)
        except pywintypes.error as e:
            return f"Services Optimization Error: Access Denied (Requires Administrator privileges)"

        for service_name in self.services_to_optimize:
            # 1. Stop the active running state
            stop_res = self._stop_service_safely(scm_handle, service_name)
            
            # 2. Reconfigure startup type to MANUAL (SERVICE_DEMAND_START = 3)
            # This ensures they don't instantly boot up on the next Windows restart
            config_res = self._set_service_startup_safely(scm_handle, service_name, win32service.SERVICE_DEMAND_START)
            
            results.append(f"{service_name}: {stop_res} | Config: {config_res}")
            
        # Clean up the main master SCM handle
        win32service.CloseServiceHandle(scm_handle)
        return "\n".join(results)

    def _stop_service_safely(self, scm_handle, service_name):
        """Safely queries a service state and stops it if running, handling state boundaries."""
        try:
            # Open handle to the specific service
            svc_handle = win32service.OpenService(scm_handle, service_name, win32service.SERVICE_QUERY_STATUS | win32service.SERVICE_STOP)
            
            # Query status to check if it's already stopped
            status = win32service.QueryServiceStatus(svc_handle)
            if status[1] == win32service.SERVICE_STOPPED:
                win32service.CloseServiceHandle(svc_handle)
                return "Already Stopped"
                
            # Send the stop control code
            win32service.ControlService(svc_handle, win32service.SERVICE_CONTROL_STOP)
            win32service.CloseServiceHandle(svc_handle)
            return "Stopped Successfully"
            
        except pywintypes.error as e:
            # Code 1060 means the service doesn't exist on this version of Windows
            if e.winerror == 1060:
                return "Not Found on System"
            return f"Stop Failed ({e.strerror})"

    def _set_service_startup_safely(self, scm_handle, service_name, startup_type):
        """Correctly opens a service handle and reconfigures its Windows boot state."""
        try:
            # Open handle with configuration modification permissions
            svc_handle = win32service.OpenService(scm_handle, service_name, win32service.SERVICE_CHANGE_CONFIG)
            
            # Execute the native Win32 configuration adjustment
            win32service.ChangeServiceConfig(
                svc_handle,
                win32service.SERVICE_NO_CHANGE, # Category type
                startup_type,                   # New startup type (Manual)
                win32service.SERVICE_NO_CHANGE, # Error control
                None, None, 0, None, None, None, None
            )
            
            win32service.CloseServiceHandle(svc_handle)
            return "Startup Set to Manual"
            
        except pywintypes.error as e:
            if e.winerror == 1060:
                return "Not Found"
            return f"Config Failed ({e.strerror})"
