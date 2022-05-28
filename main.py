# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    f = open ('C:\Users\Tunika\Documents\Python Scripts\Reading-Text-Files\story.txt','r')
    c = f.read()
    f.close()
    return c
read_file_content("story.txt")

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    sample_file = open('C:\Users\Tunika\Documents\Python Scripts\Reading-Text-Files\story.txt','r')
    file_contents = sample_file.read()

    contents_as_list = file_contents.split()
    occurence_count = collections.Counter(contents_as_list)

    print(occurence_count)
    #return {"as": 10, "would": 20}
count_words()

