#create a script to filter the others from the filtered csvs
import csv

#input the filtered csvs
def csv_to_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = []
        for i in reader:
            data.append(i)
    return(data)

filtered_ts_filepath = "C23-52/L2/L2_filtered_median_range.csv"
filtered_ANCOMBC_filepath = "C23-52/L2/L2_filtered_ANCOMBC.csv"

filtered_ts = csv_to_data(filtered_ts_filepath)

# print(filtered_ts)

#define the find other function
def remove_rows_starting_with_other(input_file_pa, output_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                if not row[0].startswith("Other"):
                    writer.writerow(row)

# Example usage:
input_file = filtered_ANCOMBC_filepath
output_file = 'C23-52/L2/wo-other_filtered_ANCOMBC.csv'

remove_rows_starting_with_other(input_file, output_file)

