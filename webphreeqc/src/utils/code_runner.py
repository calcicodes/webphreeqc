import os
import subprocess
from . import config

def run_code(user_id, code, database="phreeqc.dat"):
        
    # check for output file flag
    selected_output_file = config.user_script_path / f"{user_id}.selected_output"
    if "<<OUTPUT FILE>>" in code:
        code = code.replace("<<OUTPUT FILE>>", str(selected_output_file))
    
    # generate input file
    input_file = str(config.user_script_path / f"{user_id}.phreeqc")
    print(str(input_file))

    # write code to file
    with open(input_file, "w") as code_file:
        code_file.write(code)
    
    # generate output file path
    output_file = str(input_file + ".out")
    database_file = str(config.database_path / database)
    
    # run phreeqc
    result = subprocess.run([str(config.phreeqc_executable), input_file, output_file, database_file], capture_output=True, text=True)
    
    outlines = result.stderr.splitlines()
    outlines = '\n'.join(outlines[6:])
    
    # read output file
    with open(output_file, "r") as fout:
        output = fout.readlines()
        output = ''.join(output[4:])
    
    # cleanup
    os.remove(input_file)
    os.remove(output_file)
    
    # if produced, read selected output file
    if selected_output_file.exists():
        with open(str(selected_output_file), "r") as fout:
            selected_output = fout.read()
        os.remove(selected_output_file)
    else:
        selected_output = "No SELECTED_OUTPUT specified in input file. If you're expecting something here, check that you have set `-file <<OUTPUT FILE>>` correctly."
    
    return {'terminal': outlines, 'output': output, 'selected_output': selected_output}
