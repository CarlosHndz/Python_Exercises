def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has approximately " + str(num_words) + " words.")

print("Enter the name of a file to calculate the approximate number of words in the file.")
filename = input("\nFile name: ")
count_words(filename)