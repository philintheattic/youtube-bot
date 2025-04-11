txt = "This is a sample text based on a tutorial."
order = 3
ngrams = []

for i in range(len(txt)):
    ngrams.append(txt[i:i+order])

print(ngrams)