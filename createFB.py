import os, sys, requests
from Temporary.CreateACC.payloadsFB import Main
from Temporary.CreateACC.payloadsFB import MainV2
from rich.console import Console
from rich.panel import Panel

class Requdable:
    def __init__(self) -> None:
        pass
        
    def clear_terminalize(self):
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        
    def Banner(self):
        self.clear_terminalize()
        Console().print('''[grey50]\r
  _____             __      _______ 
 / ___/______ ___ _/ /____ / __/ _ ) [white]Author : [green]XyraaCode Dev
[red]/ /__/ __/ -_) _ `/ __/ -_) _// _  | [white]Status : [green]Premiun
\___/_/  \__/\_,_/\__/\__/_/ /____/ [white]Version : [green]2.0                                                            
\n''')
        return (True)
        
    def Running(self):
        self.Banner()
        Console().print('[grey50][[green]01[grey50]] Auto create FB')
        Console().print('[grey50][[green]02[grey50]] Create FB manual')
        querty = Console().input('\n[grey50][[green]#[grey50]] Choose : ')
        query = Console().input('\n[grey50][[green]#[grey50]] Berapa akun di buat : ')
        Console().print('\n[grey50][[green]#[grey50]] Result OK/[green]create_facebook_success.txt\n[grey50][[red]#[grey50]] Result CP/[red]create_facebook_invalid.txt')
        Console().print('\n[grey50][[green]#[grey50]] Gunakan [red]Ctrl + Z[grey50] Untuk Berhenti!\n')
        if querty =='1' or querty =='01':
            try:
                self.LoopingCreate(query)
            except (Exception, KeyboardInterrupt) as e: exit()
        elif querty =='2' or querty =='02':
            try:
                self.LoopingCreateV2(query)
            except (Exception, KeyboardInterrupt) as e: exit()
        else: exit()
        
    def LoopingCreate(self, query):
        try:
            for response in range(int(query)):
                main = Main()
                main.Create_Nama()
                main.Response_Nama()
                main.Create_Birthday()
                main.Response_Birthday()
                main.Create_Gender()
                main.Response_Gender()
                main.Create_Email()
                main.Response_Email()
                main.Create_Password()
                main.Response_Password()
                main.Next_Response()
                main.Next_Konfirmasi()
        except (Exception, requests.exceptions.ConnectionError) as e:
            self.LoopingCreate(query)
            
    def LoopingCreateV2(self, query):
        try:
            for response in range(int(query)):
                main = MainV2()
                main.Create_Nama()
                main.Response_Nama()
                main.Create_Birthday()
                main.Response_Birthday()
                main.Create_Gender()
                main.Response_Gender()
                main.Create_Email()
                main.Response_Email()
                main.Create_Password()
                main.Response_Password()
                main.Next_Response()
                main.Next_Konfirmasi()
        except (Exception, requests.exceptions.ConnectionError) as e:
            self.LoopingCreateV2(query)
            
