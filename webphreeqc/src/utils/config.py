from pathlib import Path

phreeqc_path = Path.home() / 'phreeqc'  # phreeqc install location

phreeqc_executable = phreeqc_path / 'bin/phreeqc'
database_path = phreeqc_path / "share/doc/phreeqc/database"  # path to phreeqc database files

user_script_path = Path(__file__).parent.parent.parent / 'user_scripts'

initial_database = 'None'

database_options = [
    'None',
    'phreeqc.dat',
    'pitzer.dat',
    'minteq.v4.dat',
]

output_options = {
    'Terminal': 'terminal',
    'Output File': 'output',
    'Selected Output Block': 'selected_output',
}

# file path checks
if not phreeqc_executable.exists():
    raise FileNotFoundError(f"Phreeqc executable not found at {phreeqc_executable}")