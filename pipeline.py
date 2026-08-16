import argparse

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Run the pipeline demo")
    parser.add_argument("--pg-user", default="root")
    parser.add_argument("--pg-pass", default="root")
    parser.add_argument("--pg-host", default="localhost")
    parser.add_argument("--pg-port", default=5432, type=int)
    parser.add_argument("--pg-db", default="ny_taxi")
    parser.add_argument("--target-table", default="yellow_taxi_data")
    parser.add_argument("--year", default=2020, type=int)
    parser.add_argument("--month", default=1, type=int)

    args = parser.parse_args()
    print("arguments", vars(args))
    print(f"Running pipeline for {args.year}-{args.month:02d}")

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df["year"] = args.year
    df["month"] = args.month
    print(df.head())

    df.to_parquet(f"output_day_{args.year}_{args.month:02d}.parquet")


if __name__ == "__main__":
    main()