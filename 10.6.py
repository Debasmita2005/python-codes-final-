# Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.

def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as fout:
        line1 = f1.readlines()
        line2 = f2.readlines()

        max_len = max(len(line1), len(line2))

        for i in range(max_len):
            if i < len(line1):
                fout.write(line1[i])
            if i < len(line2):
                fout.write(line2[i])

    print(f"Merged content written to {output_file}")

merge_files('file1.txt', 'file2.txt', 'merged_output.txt')
