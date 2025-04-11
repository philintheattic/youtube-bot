txt = "This is a sample text based on a tutorial."
order = 3
ngrams = []

for i in range(len(txt)-order+1):
    ngrams.append(txt[i:i+order])

print(len(ngrams))
print(len(set(ngrams)))