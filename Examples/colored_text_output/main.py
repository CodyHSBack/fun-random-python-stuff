class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Examples: \n")

print(f"{bcolors.HEADER}HEADER{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}OKBLUE{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}OKCYAN{bcolors.ENDC}")
print(f"{bcolors.WARNING}Warning{bcolors.ENDC}")
print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}")
print(f"{bcolors.ENDC}END{bcolors.ENDC}")
print(f"{bcolors.BOLD}BOLD{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}UNDERLINE{bcolors.ENDC}")

