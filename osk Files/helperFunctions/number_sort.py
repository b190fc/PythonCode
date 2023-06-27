# Define the input and output file names
input_file_name = "D:/henry/Code/pythonextra/file_list.txt"
output_file_name = "sorted_output.txt"

# Read the contents of the input file into a list
with open(input_file_name, 'r') as input_file:
    contents = [int(x) for x in input_file.read().split()]

# Sort the list
sorted_list = sorted(contents)

# Write the sorted list to the output file
with open(output_file_name, 'w') as output_file:
    for num in sorted_list:
        output_file.write(str(num) + "\n")
