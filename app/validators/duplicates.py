import pandas as pd

def get_duplicated(df:pd.DataFrame) -> dict:
    dup_mask = df.duplicated()
    dup_row_count = int(dup_mask.sum())
    dup_row_percentage = (dup_row_count/len(df)*100 if len(df) > 0 else 0)
    duplicated_indexes = (
        df.index[dup_mask].tolist()
    )
    duplicate_rows = (
        df[dup_mask].to_dict(orient="records")
    )

    return{
        "duplicate_count":dup_row_count,
        "duplicate_percentage" : round(
            dup_row_percentage, 2
        ),
        "duplicated_indexes" : duplicated_indexes,
        "duplicate_rows" : duplicate_rows
    }