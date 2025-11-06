import pandas as pd, json

def validate_json_column(file_path, column_name):
    df = pd.read_csv(file_path)
    for idx, val in enumerate(df[column_name]):
        try:
            json.loads(val)
        except Exception as e:
            print(f"❌ Invalid JSON in row {idx+1}: {e}")
            return
    print("✅ All JSON arrays valid.")

if __name__ == "__main__":
    file = "output/irb_protocols_transformed.csv"
    validate_json_column(file, "personnel::hrn")
