import win32service
import win32serviceutil

class ServiceManager:
    def __init__(self):
        self.services_to_optimize = [
            'wuauserv',      # Windows Update
            'BITS',          # Background Intelligent Transfer
            'WSearch'        # Windows Search
        ]
    
    def stop_services(self):
        """Stop unnecessary services"""
        stopped = []
        for service in self.services_to_optimize:
            try:
                win32serviceutil.StopService(service)
                stopped.append(service)
            except Exception as e:
                print(f"Error stopping {service}: {e}")
        return stopped
    
    def set_service_startup(self, service, startup_type):
        """Set service startup type"""
        try:
            win32service.ChangeServiceConfig(
                service,
                win32service.SERVICE_NO_CHANGE,
                startup_type,
                win32service.SERVICE_NO_CHANGE,
                None,
                None,
                0,
                None,
                None,
                None,
                None
            )
            return True
        except Exception as e:
            print(f"Error changing startup for {service}: {e}")
            return False