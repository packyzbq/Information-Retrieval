from TokenLize import DocStream
from Dict_Build import Dict_Postlist

filename_1 = r'C:\Users\宝琦\Documents\EXP_Data\Modern info\shakespeare-merchant.trec.1'
filename_2 = r'C:\Users\宝琦\Documents\EXP_Data\Modern info\shakespeare-merchant.trec.2'
file_test = r'test.txt'

stream = DocStream()
test_dic = stream.getTokenStream(file_test)
for i in test_dic:
    print(i,':',test_dic.get(i))

dict_post = Dict_Postlist()
dict_post.spimi_build(test_dic)