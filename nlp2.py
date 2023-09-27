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
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item]