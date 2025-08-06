import argparse
from pathlib import Path
import time


#Custom made tools
from Utils import scanner
from Utils import reporter
import patterns
startTime = time.time()
#arg initialization
parser = argparse.ArgumentParser(description="A CLI tool that recursively scans through a folder or shared drive for secrets.")
parser.add_argument("--target", '--t', required=True, help="Type what path needs to be scanned recursively.")
parser.add_argument("--report", '--r', required=True, help="Specify where scan results should be saved.")
parser.add_argument("--zip", '--z', required=False ,help="Specify if files found with secrets should be zipped.")
args = parser.parse_args()

#parsed args
target = Path(args.target)
report = Path(args.report) 

#zip not yet implemented 
zip_path = args.zip

pattern = patterns
print(f"ByakuScanner is starting!....\n \n")

#main process
try:
    reporter.reporter(report, scanner.scanner(target,pattern,report,zip_path))
except Exception as e:
    print(f"The following error occured: {e}")
    
endTime = time.time()
runtime = endTime - startTime

print(f"The program took {runtime} seconds to run!")
#optional zip feature
