import os
import subprocess
from pathlib import Path

database_path = Path("../phreeqc-3.8.6-17100/database")
user_script_path = Path("user_scripts")

available_databases = [
    'phreeqc.dat',
    'pitzer.dat',
    'minteqv4.dat',
]

def run_code(user_id, code, database="phreeqc.dat"):
    
    # generate input file
    input_file = str(user_script_path / f"{user_id}.phreeqc")
    
    # write code to file
    with open(input_file, "w") as code_file:
        code_file.write(code)
    
    # generate output file path
    output_file = str(input_file + ".out")
    database_file = str(database_path / database)
    
    # run phreeqc
    result = subprocess.run(['phreeqc', input_file, output_file, database_file], capture_output=True, text=True)
    
    outlines = result.stderr
    
    # read output file
    with open(output_file, "r") as fout:
        output = fout.readlines()
        output = ''.join(output[4:])
    
    print(input_file)
    print(output_file)
    
    # cleanup
    os.remove(input_file)
    os.remove(output_file)
    
    out = (
        outlines + 
        '\n\n\n################ PHREEQC OUTPUT STARTS ################\n\n\n' + 
        output
    )
    
    return {'terminal': outlines, 'output': output}
