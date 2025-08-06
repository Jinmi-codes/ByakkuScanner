import re
import zipfile
from pathlib import Path

#Key masker. Replaces part of found keys with asterisks while reporting.
def mask(secret):
       
    return secret[:4] +'*' * (len(secret)-8) + secret[-4:]

#main scanner function
def scanner(path,patterns,report,zip):
    secret_found = False
    path = Path(path)
    if path.exists():
      # yields a generator. 
        for file in path.rglob("*"):
            if file.is_file():
                try: 
                    with open(file, 'r', encoding='utf-8') as current:
                        line_count = 0
                        for line in current:
                            line_count +=1
                            line = line.strip()
                            for object in patterns.regex_patterns:
                                if re.search(patterns.regex_patterns[object], line):  
                                    secret_found = True  
                                    yield f"[!] Secret was found! \n Path: {file} \n Type: {object} \n Secret: {mask(line)} \n Line: {line_count} \n \n"
                except (UnicodeDecodeError, PermissionError):
                    continue
                           

        
        if secret_found == False:
            print(f"No secret was found in specified location: {path}")
        elif secret_found:
            print( f"All secrets found were saved to specified location: {report}")
        
        if zip != None:
            print("Zipping files will be implemented later.")
    else:
        yield f"Specified path: {path} does not exist."                  
                          
                                
