import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

word_stats = {}
line = 0

def word_statistics(word_stats):
    if(word not in word_stats):
        word_stats[word] = {'word_count': 1,'line_number': line}
    else:
        word_stats[word]['word_count'] = word_stats[word]['word_count']+1

def print_stats(word_stats):
    print("word\tcount\tfirst line")
    for i in word_stats:
        print(f"{i}\t{word_stats[i]['word_count']}\t{word_stats[i]['line_number']}")

for text in texts:
   word_list = re.sub('([^A-z^\s])+', '', text).lower().split()
    for word in word_list:
        word_statistics(word_stats)
    line += 1
print_stats(word_stats)
