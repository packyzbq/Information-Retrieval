import TokenLize
import Linklist

# 词典节点
class Dict_Node():
    def __init__(self,df,post_point,dict_point):
        self.df = df
        self.post_point = post_point
        self.dict_point = dict_point
    def __set_df__(self,df):
        self.df = df

# 词典-倒排表
# ps 链表的Node init的数据，为双层list
class Dict_Postlist():
    token_dict=[]
    post_list = Linklist()  # 倒排索引表
    dic_string=''           # 单一字符串字典

    # 添加到倒排表
    # para term  添加的词项
    #      docno 词项所在文档id
    def __addToPostList__(self,term,docno):
        return

    # spimi单步
    def __spimi_invert__(self,token_stream):
        return

    #TODO get set method


    # spimi算法
    def spimi_build(self,token_stream):
        return

    #gamma压缩
    def gamma(self,num):
        return

