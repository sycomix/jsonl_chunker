import json
import os

# Set the number of output files per input file
num_files_per_input = 10

# Get a list of all files in the current directory with a .jsonl extension
files = [f for f in os.listdir('.') if f.endswith('.jsonl')]

# Loop through each file
for file in files:
    # Open the input JSONL file
    with open(file, 'r') as input_file:
        # Read all lines from the input file and count the total number of lines
        lines = input_file.readlines()
        total_lines = len(lines)

    # Calculate the number of lines per output file
    lines_per_file = total_lines // num_files_per_input

    # Get the base file name and extension from the input file path
    file_name, file_extension = os.path.splitext(file)

    # Loop through each output file
    for i in range(num_files_per_input):
        # Calculate the start and end line numbers for the current output file
        start_line = i * lines_per_file
        end_line = start_line + lines_per_file

        # If this is the last output file, include any remaining lines
        if i == num_files_per_input - 1:
            end_line = total_lines

        # Construct the output file name
        output_file_name = f'{file_name}_{i + 1}{file_extension}'

        # Open the current output file
        with open(output_file_name, 'w') as output_file:
            # Write the lines to the current output file
            for line in lines[start_line:end_line]:
                # Parse the JSON object
                obj = json.loads(line)
                # Write the JSON object to the output file
                output_file.write(json.dumps(obj) + '\n')
