from loaders.csv_loader import load_csv
from profilers.basic_profile import get_basic_profile


def main():
    df = load_csv(r"E:\python_projects\15_projects\datadoctor\sales.csv")
    profile = get_basic_profile(df)
    print(profile)

if __name__ == "__main__":
    main()