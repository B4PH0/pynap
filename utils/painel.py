import colorama
import datetime

def painel():
    color = {
        'red': colorama.Fore.RED,
        'reset': colorama.Fore.RESET
    }
    now = datetime.date.today()
    date = {
        'time': now.ctime()
    }
    hora = datetime.time
    print(f'Starting pynap 1.0.0 ({date["time"]})...')
