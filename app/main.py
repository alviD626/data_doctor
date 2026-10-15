from pprint import pprint
from loaders.csv_loader import load_csv
from profilers.basic_profile import get_basic_profile
from validators.missing_values import detect_missing_values
from validators.duplicates import get_duplicated


def main():
    df = load_csv(r"E:\python_projects\15_projects\datadoctor\sales.csv")
    profile = get_basic_profile(df)
    missing_report = detect_missing_values(df)
    duplicate_report = get_duplicated(df)

    print("\nDATASET PROFILE")
    pprint(profile)

    print("\nMISSING VALUE REPORT")
    pprint(missing_report)

    print("\nDUPLICATE REPORT")
    pprint(duplicate_report)

if __name__ == "__main__":
    main()