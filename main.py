from scanner import PortScanner
from colorama import init, Fore, Style
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("Port Scanner", font="slant")
    print(f"{Fore.RED}{banner}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'='*75}{Style.RESET_ALL}")
    print(f"{Fore.RED}Geliştirici: [Muhammet Çakmak] | GitHub: https://github.com/muhammettcakmak{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'='*75}\n{Style.RESET_ALL}")

def get_user_input():
    while True:
        target_ip = input(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Hedef IP adresini girin: {Style.RESET_ALL}")
        if is_valid_ip(target_ip):
            break
        print(f"{Fore.RED}[!] Geçersiz IP adresi! Lütfen geçerli bir IP adresi girin (Örn: 192.168.1.1){Style.RESET_ALL}")
    
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

def is_valid_ip(ip):
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        return all(0 <= int(part) <= 255 for part in parts)
    except (AttributeError, TypeError, ValueError):
        return False

def main():
    init()
    try:
        print_banner()
        target_ip, start_port, end_port = get_user_input()
        scanner = PortScanner(target_ip, start_port, end_port)
        scanner.start_scan()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Program kullanıcı tarafından sonlandırıldı!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Bir hata oluştu: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()