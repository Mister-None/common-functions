import sys, re, pandas as pd, subprocess
from colorama import Fore, init

init(autoreset=True)

class CommonFunctions:
    @staticmethod
    def list_of_functions(*args):
        print(Fore.RED + 'Enter number of function!')
        for id, i in enumerate(args):
            if i:
                print(f"{Fore.LIGHTYELLOW_EX}{id} {Fore.LIGHTGREEN_EX}==> {Fore.LIGHTBLUE_EX}{i}")
        sys.exit(1)

    def list_of_functions_v(*args):
        for id, i in enumerate(args):
            if i:
                print(f"{Fore.LIGHTYELLOW_EX}{id} {Fore.LIGHTGREEN_EX}==> {Fore.LIGHTBLUE_EX}{i}")

    @staticmethod
    def text_normalizer(raw_text):
        raw = str(raw_text).lower().strip()
        raw = re.sub(r"""[,.()"'|!?/«»_:;”=’`~\n]""", ' ', raw)
        raw = re.sub(' +', ' ', raw)
        if raw == 'nan':
            return None
        else:
            return raw

    @staticmethod
    def xlsx(mode, **columns):
        df = pd.DataFrame(columns)
        df.to_excel(mode+'.xlsx', index=False)


    @staticmethod
    def temp_clipboard(mode, **lists):
        list_values = list(lists.values())
        with open(mode, 'w') as f:
            for row in zip(*list_values):
                line = '\t'.join(str(item) for item in row)
                f.write(line + '\n')
        input('Paste >>> ')
        subprocess.run(f"cat {mode} | wl-copy && rm {mode}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)            

    @staticmethod
    def connect_vpn(server):
        subprocess.run("mullvad disconnect --wait", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(f"mullvad relay set location {server}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run("mullvad connect --wait", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
