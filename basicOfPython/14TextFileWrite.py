#read the text file, reverse the file content and write back in the same file

with open ('text.txt', 'r') as reader:
    content =reader.readlines()
    print(content) #['ab\n', 'cd\n', 'ef\n', 'gh\n', 'ij\n']
    rev=reversed(content) #['ij\n', 'gh\n', 'ef\n', 'cd\n', 'ab\n']
    with open ('text.txt','w') as writer:
        for line in rev:
            writer.write(line)
