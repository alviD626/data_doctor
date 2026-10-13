import pandas as pd


def detect_missing_values(df: pd.DataFrame) -> dict:
    column_missing_values = df.isna().sum()
    total_missing_values = int(column_missing_values.sum())
    column_missing_percentage = df.isna().mean()*100
    missing_summary = {}
    for column in df.columns:
        missing_summary[column] = {
            "count": int(
                column_missing_values[column]
            ),
            "percentage": round(
                float(column_missing_percentage[column]),
                2
            )
        }
    row_wise_missing_values = int(df.isna().any(axis=1).sum())

    return {
        "total_missing": total_missing_values,
        "rows_with_missing": row_wise_missing_values,
        "columns": missing_summary
    }