import random

# txt = "There is a sample text based on a theremin that is theirs."

# get some input text from a file
with open("text.txt" ,"r", encoding="utf-8") as f:
    txt = f.read().strip().replace("\n", "")

order = 3
ngrams = {}

for i in range(len(txt)-order):
    # substring the text into ngrams
    ngram = txt[i:i+order]

    # if ngram doesn't exist, create it and initalize an array
    if ngram not in ngrams:
        ngrams[ngram] = []

    # if ngram exists append the follow-up character to the array associated with that ngram
    ngrams[ngram].append(txt[i+order])

        
def markovIt(iterations):
    # start with the first ngram of the input string
    # currentGram = txt[0:order]

    # start with random ngram
    currentGram = random.choice(list(ngrams))

    # initialize result string that we can append characters to
    result = currentGram

    # main loop
    for _ in range(iterations):

        # load up array of possible characters of current ngram
        try:
            possibilities = ngrams[currentGram]
        except KeyError:
            print(f"KeyError detected. Stopped the chain on step: {_}")
            break

        # choose a random letter from that array
        next = random.choice(possibilities)

        # add that letter to the result string
        result += next

        # take the new result into consideration and use the latest ngram from that string for the next iteration
        currentGram = result[-order:]

    return result

#example usage:
print(markovIt(500))
