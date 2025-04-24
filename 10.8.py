# Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.

def remove(input_file, output_file):
    articles = {'a', 'an', 'the'}

    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            words = line.split()
            filtered_words = [word for word in words if word.lower() not in articles]
            fout.write(' '.join(filtered_words) + '\n')

    print(f"Filtered content written to {output_file}")

remove('input.txt', 'output.txt')
