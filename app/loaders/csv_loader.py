from pathlib import Path

import pandas as pd

def load_csv(file_path:str) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"file not found: {file_path}"
        )
    if path.suffix.lower() != ".csv":
        raise ValueError(
            "Only csv files are currently are supported."
        )
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        raise ValueError(
            "The CSV file is empty"
        )
    except pd.errors.ParserError:
        raise ValueError(
            "The CSV file could not be parsed"
        )
    return df