# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from janome.tokenizer import Tokenizer
import CBOW
file = open('/Users/qiyixi/Downloads/Pycharm/corpus20150426.txt','r',encoding='sjis')
text = file.read()
#print(text[100])
t = Tokenizer()
#
def extract_words(test):
    tokens = t.tokenize(test)
    return [token.base_form for token in tokens
        if token.part_of_speech.split(',')[0] in['名詞','動詞','形容詞']]
#
#
#
#
sentences = text.split('。')
# #tokens = t.tokenize(sentences[2])
# #print(tokens)
# # for token in tokens:
# #     print(token)
# #word_list = [extract_words(sentences[2])]
#
word_list = [extract_words(sentence)for sentence in sentences]
#
# txt = open('./corpus.txt','w',encoding='sjis')
# for word_2 in word_list:
#     for word_1 in word_2:
#         txt.write(word_1)
#         txt.write(',')
# txt.close()
# print(word_list)



from gensim.models import word2vec
# file = open('./corpus.txt','r',encoding='sjis')
# word_list = file.read()
# my_list = word_list.split(',')
# print(my_list[:100])
model = word2vec.Word2Vec(word_list,min_count=2,sg=0)
ret = model.wv.most_similar(positive=['佐川'])
for item in ret :
    print(item[0],item[1])
model.save('./Word_CBOW.w2v')
# file.close()
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/