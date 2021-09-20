import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

word_stats = {}
line = 0

for text in texts:
    for word in re.sub('([^A-z^\s])+', '', text).lower().split():
        if(word not in  word_stats):
            word_stats[word] = {'word_count': 1,'line_number': line}
        else:
            word_stats[word]['word_count'] = word_stats[word]['word_count']+1
    line += 1

print("word\tcount\tfirst line")
for i in word_stats:
    print(f"{i}\t{word_stats[i]['word_count']}\t{word_stats[i]['line_number']}")