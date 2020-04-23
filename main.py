class TimeoutExceeded(Exception):
    pass

class Waiter:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def is_up(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((host, port))
            sock.close()
            return True

        except socket.error:
            return False

    def wait(self, timeout, interval=5):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_up():
                return
            
            time.sleep(interval)
            
        raise TimeoutExceeded()
