import csv
import os

def combine_csv_files(file1_path, file2_path, output_file_path):
    """
    Combines two CSV files with the same header into a single output CSV file.

    Args:
        file1_path (str): Path to the first CSV file.
        file2_path (str): Path to the second CSV file.
        output_file_path (str): Path for the combined output CSV file.
    """
    try:
        rows_file1 = []
        header = []

        # --- Read the first file ---
        print(f"Reading from {file1_path}...")
        with open(file1_path, 'r', newline='', encoding='utf-8') as infile1:
            reader1 = csv.reader(infile1)
            header = next(reader1)  # Read the header
            rows_file1.extend(row for row in reader1) # Read data rows
        print(f"Read {len(rows_file1)} data rows from {file1_path}.")

        rows_file2 = []
        header_file2 = []

        # --- Read the second file ---
        print(f"Reading from {file2_path}...")
        with open(file2_path, 'r', newline='', encoding='utf-8') as infile2:
            reader2 = csv.reader(infile2)
            header_file2 = next(reader2) # Read the header of the second file
            # Validate if headers are the same
            if header != header_file2:
                print("Error: Headers of the two files do not match.")
                print(f"Header File 1: {header}")
                print(f"Header File 2: {header_file2}")
                return False
            rows_file2.extend(row for row in reader2) # Read data rows
        print(f"Read {len(rows_file2)} data rows from {file2_path}.")

        # --- Combine data ---
        combined_rows = rows_file1 + rows_file2
        print(f"Total data rows to write: {len(combined_rows)}.")

        # --- Write to the output file ---
        print(f"Writing combined data to {output_file_path}...")
        with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write the header
            writer.writerows(combined_rows) # Write all data rows
        
        print(f"Successfully combined '{file1_path}' and '{file2_path}' into '{output_file_path}'.")
        return True

    except FileNotFoundError:
        print("Error: One or both input files not found. Please check the file paths.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    print("--- CSV File Combiner ---")
    
    # Get file paths from user input
    file1 = input("Enter the path to the first CSV file: ").strip()
    file2 = input("Enter the path to the second CSV file: ").strip()
    output_file = input("Enter the path for the combined output CSV file: ").strip()

    # Basic validation for output file extension
    if not output_file.lower().endswith('.csv'):
        print("Warning: Output file does not have a .csv extension. Appending .csv")
        output_file += ".csv"
        
    # Ensure input files are not the same as the output file to prevent accidental overwrite during read
    if os.path.abspath(file1) == os.path.abspath(output_file) or \
       os.path.abspath(file2) == os.path.abspath(output_file):
        print("Error: Output file cannot be the same as an input file.")
    else:
        combine_csv_files(file1, file2, output_file)
