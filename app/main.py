from pprint import pprint
from loaders.csv_loader import load_csv
from profilers.basic_profile import get_basic_profile
from validators.missing_values import detect_missing_values


def main():
    df = load_csv(r"E:\python_projects\15_projects\datadoctor\sales.csv")
    profile = get_basic_profile(df)
    missing_report = detect_missing_values(df)

    print("\nDATASET PROFILE")
    pprint(profile)

    print("\nMISSING VALUE REPORT")
    pprint(missing_report)

if __name__ == "__main__":
    main()