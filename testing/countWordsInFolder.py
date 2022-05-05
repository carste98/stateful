import os
import sys
import re

# Code from:
# https://github.com/gandreadis/markdown-word-count
def count_words_in_markdown(markdown):
    text = markdown

    # Comments
    text = re.sub(r'<!--(.*?)-->', '', text, flags=re.MULTILINE)
    # Tabs to spaces
    text = text.replace('\t', '    ')
    # More than 1 space to 4 spaces
    text = re.sub(r'[ ]{2,}', '    ', text)
    # Footnotes
    text = re.sub(r'^\[[^]]*\][^(].*', '', text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r'^( {4,}[^-*]).*', '', text, flags=re.MULTILINE)
    # Custom header IDs
    text = re.sub(r'{#.*}', '', text)
    # Replace newlines with spaces for uniform handling
    text = text.replace('\n', ' ')
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    # Remove HTML tags
    text = re.sub(r'</?[^>]*>', '', text)
    # Remove special characters
    text = re.sub(r'[#*`~\-–^=<>+|/:]', '', text)
    # Remove footnote references
    text = re.sub(r'\[[0-9]*\]', '', text)
    # Remove enumerations
    text = re.sub(r'[0-9#]*\.', '', text)

    return len(text.split())



# Script based on code
# https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
def get_wordcount(start_path):
    validTextEndings = ['.txt', '.rst', '.md']
    count = 0
    for paths, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(paths, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                filename, file_extension = os.path.splitext(fp)
                if file_extension in validTextEndings:
                    if file_extension == ".md":
                        f = open(fp, "r", encoding='utf-8')
                        count += count_words_in_markdown(f.read())
                    else:
                        f = open(fp, "r")
                        for line in f:
                            count += len(line.split())
    return count


for i in range(1, len(sys.argv)):
    name = sys.argv[i].split("/")
    if name[len(name)-1] != "":
        print('folder name:', name[len(name)-1], '-', get_wordcount(sys.argv[i]), 'words')
    else:
        print('folder name:', name[len(name)-2], '-', get_wordcount(sys.argv[i]), 'words')


