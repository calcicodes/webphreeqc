from pathlib import Path

phreeqc_path = Path.home() / 'phreeqc'  # phreeqc install location

phreeqc_executable = phreeqc_path / 'bin/phreeqc'
database_path = phreeqc_path / "share/doc/phreeqc/database"

user_script_path = Path(__file__).parent.parent.parent / 'user_scripts'

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