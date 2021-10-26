from gensim.models import word2vec
file = open('./cor.txt','r','sjis')
word_list = file.read()
my_list = word_list.split(',')
print(my_list[0])