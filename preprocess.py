import numpy as np

def load_data():
    with open('shakespeare.txt', mode='r', encoding='utf-8') as f:
        data = f.read()
    return data

raw_data = load_data()
print("Length of raw data: {}".format(len(raw_data)))

def remove_junk(raw_data):
    START = """THE SONNETS

by William Shakespeare"""
    STOP = "End of Project Gutenberg's Shakespeare's Sonnets, by William Shakespeare"
    
    assert START in raw_data, "START not found in given data"
    assert STOP in raw_data, "STOP not found in given data"
    
    data = raw_data.split(START, 1)[1]
    data = data.split(STOP, 1)[0]
    return data

cleaned_data = remove_junk(raw_data)
print("Length of data after removing the header and the footer: {}".format(len(cleaned_data)))


def clean(data):
    temp = data.split('\n')
    # A simple 'hack' to remove the roman numerals and empty lines from the data
    temp = [t.strip() for t in temp if len(t) > 10]
    # Rejoining the cleaned parts
    data = '\n'.join(temp)
    return data

data = clean(cleaned_data)
# Keeping a common case, for faster tranining, and lesser vocabulary size
data = data.lower()

# Further reduce the vocabulary size by removing a few punctuations 
exclude_chars = ['!', "'", '(', ')', ',', '-', '.', ':', ';', '?']
for c in exclude_chars:
    data = data.replace(c, '')

print("Length of data after cleaning: {}".format(len(data)))

distinct_chars = sorted(list(set(data)))
print("Number of unique characters/Vocabulary size: {}".format(len(distinct_chars)))

# Saving the processed data:
with open('shakespeare_cleaned.txt', mode='w', encoding='utf-8') as f:
    f.write(data)
    
