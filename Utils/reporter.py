import re
from pathlib import Path

def reporter(report, scanner):
    with open(report, 'w') as file:
        iterate = 0
        for secret_found in scanner:
            iterate+=1
            if iterate >= 1:   
                print(secret_found)
                file.write(f"{secret_found}\n")
            else:
                print("No secrets were found")