import csv
import os

def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist:", file_path)

    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def filter_data(data, threshold):
    # Filters rows where 'value' is greater than threshold
    return [row for row in data if int(row['value']) > threshold]

def write_csv(data, output_path):
    if not data:
        print("No data to write.")
        return

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    input_file = "data/input.csv"
    output_file = "data/output.csv"
    threshold = 50

    try:
        data = read_csv(input_file)
        filtered = filter_data(data, threshold)
        write_csv(filtered, output_file)
        print("Processing complete. Output written to", output_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
