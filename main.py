from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    data = extract_data("data/sales.csv")
    print("Extracted Data:")
    print(data)

    cleaned_data = transform_data(data)
    print("\nTransformed Data:")
    print(cleaned_data)

    cleaned_data.to_csv("output/cleaned_sales.csv", index=False)

    load_data(cleaned_data)
    print("\nETL Pipeline Completed Successfully.")

if __name__ == "__main__":
    main()
