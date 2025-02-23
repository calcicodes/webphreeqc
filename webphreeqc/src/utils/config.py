from pathlib import Path

database_path = Path("../phreeqc-3.8.6-17100/database")
user_script_path = Path("user_scripts")

initial_database = 'phreeqc.dat'

database_options = [
    'phreeqc.dat',
    'pitzer.dat',
    'minteq.v4.dat',
]