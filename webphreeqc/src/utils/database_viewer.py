from . import config

def load_database(database):
    database_file = config.database_path / database
    
    if not database_file.exists():
        return f"Database file {database} does not exist."
    
    with open(str(database_file), "r", encoding='latin-1') as f:
        return f.read()
