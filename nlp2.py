import numpy as np
from gensim import corpora, models
from gensim.utils import simple_preprocess


text1 = ["My name is Mitusha Pawar.", 
   "I am from Sanjivani College of Engineering.", 
   "Mitusha is from Ahmednagar. "]


tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)


print("\n-----------------------------------------")
print("-------------------TFIDF----------------------")
text = ["My name is Mitusha Pawar.", 
   "I am from Sanjivani College of Engineering.", 
   "I am from Information Technology Department. "]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

# Output: 
#    The dictionary has: 13 tokens

# {'Mitusha': 0, 'My': 1, 'Pawar.': 2, 'is': 3, 'name': 4, 'College': 5, 'Engineering.': 6, 'I': 7, 'Sanjivani': 8, 'am': 9, 'from': 10, 'of': 11, 'Ahmednagar.': 12}
# Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)], [(0, 1), (3, 1), (10, 1), (12, 1)]]

# -----------------------------------------
# -------------------TFIDF----------------------
# Dictionary : 
# [['is', 1], ['mitusha', 1], ['my', 1], ['name', 1], ['pawar', 1]]
# [['am', 1], ['college', 1], ['engineering', 1], ['from', 1], ['of', 1], ['sanjivani', 1]]
# [['am', 1], ['from', 1], ['department', 1], ['information', 1], ['technology', 1]]
# TF-IDF Vector:
# [['is', 0.45], ['mitusha', 0.45], ['my', 0.45], ['name', 0.45], ['pawar', 0.45]]
# [['am', 0.24], ['college', 0.47], ['engineering', 0.47], ['from', 0.24], ['of', 0.47], ['sanjivani', 0.47]]
# [['am', 0.27], ['from', 0.27], ['department', 0.53], ['information', 0.53], ['technology', 0.53]]