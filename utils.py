from colorama import Fore, Style
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("Port Scanner", font="slant")
    print(f"{Fore.RED}{banner}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'='*75}{Style.RESET_ALL}")
    print(f"{Fore.RED}Geliştirici: [Muhammet Çakmak] | GitHub: https://github.com/muhammettcakmak{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'='*75}\n{Style.RESET_ALL}")

def validate_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

def get_user_input():
    while True:
        target_ip = input(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Hedef IP adresini girin: {Style.RESET_ALL}")
        if validate_ip(target_ip):
            break
        print(f"{Fore.RED}[!] Geçersiz IP adresi! Lütfen tekrar deneyin.{Style.RESET_ALL}")
    
    while True:
        try:
            start_port = int(input(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Başlangıç portunu girin (1-65535): {Style.RESET_ALL}"))
            if 1 <= start_port <= 65535:
                break
            print(f"{Fore.RED}[!] Port numarası 1-65535 arasında olmalıdır!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}[!] Lütfen geçerli bir sayı girin!{Style.RESET_ALL}")
    
    while True:
        try:
            end_port = int(input(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Bitiş portunu girin (1-65535): {Style.RESET_ALL}"))
            if start_port <= end_port <= 65535:
                break
            print(f"{Fore.RED}[!] Bitiş portu başlangıç portundan büyük ve 65535'ten küçük olmalıdır!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}[!] Lütfen geçerli bir sayı girin!{Style.RESET_ALL}")
    
    return target_ip, start_port, end_port 