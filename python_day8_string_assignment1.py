from collections import Counter
import re

string = "To change the overall look of your document. To change the look available in the gallery"
words = re.findall(r'\b\w+\b', string.lower())
word_count = Counter(words)

print(word_count)


#output
Counter({'the': 3, 'to': 2, 'change': 2, 'look': 2, 'overall': 1,
'of': 1, 'your': 1, 'document': 1, 'available': 1, 'in': 1, 'gallery': 1})
