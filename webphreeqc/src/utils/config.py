from pathlib import Path

phreeqc_executable = Path.home() / Path('phreeqc/bin/phreeqc')
database_path = Path("../phreeqc-3.8.6-17100/database")
user_script_path = Path("user_scripts")

initial_database = 'phreeqc.dat'

database_options = [
    'phreeqc.dat',
    'pitzer.dat',
    'minteq.v4.dat',
]

# file path checks
if not phreeqc_executable.exists():
    raise FileNotFoundError(f"Phreeqc executable not found at {phreeqc_executable}")
if not (database_path / initial_database).exists():
    raise FileNotFoundError(f"Initial database file not found at {database_path / initial_database}")