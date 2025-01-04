import socket
import threading
from queue import Queue
import time
from colorama import Fore, Style, init
import sys
import ssl

class PortScanner:
    def __init__(self, target, start_port, end_port):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.queue = Queue()
        self.open_ports = []
        self.scanned_ports = 0
        self.total_ports = end_port - start_port + 1
        self.lock = threading.Lock()
        init()

    def update_progress(self):
        try:
            percentage = round((self.scanned_ports / self.total_ports) * 100, 2)
            bar_length = 30
            filled_length = int(bar_length * self.scanned_ports // self.total_ports)
            bar = '#' * filled_length + '-' * (bar_length - filled_length)
            
            sys.stdout.write(f'\r{Fore.RED}[{bar}] %{percentage:.2f}{Style.RESET_ALL}')
            sys.stdout.flush()
        except:
            pass

    def get_service_info(self, port):
        try:
            service = socket.getservbyport(port)
            
            if port in [80, 443]:
                try:
                    if port == 443:
                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE
                        sock = context.wrap_socket(socket.socket())
                    else:
                        sock = socket.socket()
                    
                    sock.settimeout(2)
                    sock.connect((self.target, port))
                    
                    request = f"GET / HTTP/1.1\r\nHost: {self.target}\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
                    if port == 443:
                        sock.write(request.encode())
                    else:
                        sock.send(request.encode())
                    
                    response = sock.recv(1024).decode('utf-8', errors='ignore')
                    sock.close()
                    
                    for line in response.split('\n'):
                        if 'Server:' in line:
                            server = line.split('Server:')[1].strip()
                            return f"{'HTTPS' if port == 443 else 'HTTP'} ({server})"
                    return service.upper()
                except:
                    return service.upper()
            
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((self.target, port))
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            
            if banner:
                return f"{service.upper()} ({banner.split()[0]})"
            return service.upper()
        except:
            return f"PORT {port}"

    def port_scan(self, port):
        try:
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                with self.lock:
                    service_info = self.get_service_info(port)
                    self.open_ports.append((port, service_info))
            sock.close()
        except:
            pass
        finally:
            with self.lock:
                self.scanned_ports += 1
                self.update_progress()

    def worker(self):
        while not self.queue.empty():
            self.port_scan(self.queue.get())

    def start_scan(self):
        print(f"\n{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] Port Scanner v1.0")
        print(f"\n{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Hedef: {self.target} [{self.start_port}-{self.end_port}]{Style.RESET_ALL}\n")
        
        sys.stdout.write(f'{Fore.RED}[{"#"*30}] %0.00{Style.RESET_ALL}')
        sys.stdout.flush()
        
        start_time = time.time()
        
        for port in range(self.start_port, self.end_port + 1):
            self.queue.put(port)
        
        threads = []
        for _ in range(100):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        duration = time.time() - start_time
        
        print(f"\n\n{Fore.RED}PORT     STATE    SERVICE")
        print(f"{Fore.WHITE}{'-'*40}{Style.RESET_ALL}")
        
        if self.open_ports:
            for port, service_info in sorted(self.open_ports):
                port_str = str(port).ljust(8)
                print(f"{Fore.WHITE}{port_str} {Fore.RED}open     {Fore.WHITE}{service_info}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] Açık port bulunamadı{Style.RESET_ALL}")
        
        print(f"\n{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Tarama {duration:.2f} saniyede tamamlandı{Style.RESET_ALL}") 