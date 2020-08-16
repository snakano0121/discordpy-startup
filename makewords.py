# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:47:59 2020

@author: User
"""

import re
from janome.tokenizer import Tokenizer

#感情ファイルの辞書を作成する
def analyzeWord(message):
    def read_pn_di():
        dic_pn = {}
    
        f = open(r"words.txt","r",encoding="utf-8")
        lines = f.readlines() # 1行を文字列として読み込む(改行文字も含まれる)
        
        for line in lines:
            #フォーマット
            #見出し語:読み(ひらがな):品詞:感情極性実数値
            columns = line.split(':')
            dic_pn[columns[0]] = float(columns[3])
        f.close
    
        return dic_pn
    
    dic_pn = read_pn_di()
    
    #セパレータを「。」とする。
    seperator = "。"
    message_origin = message
    mixi_diary_origin = re.sub("[｜ 　「」\n]", "", message_origin) # | と全角半角スペース、「」と改行の削除
    #
    
    mixi_diary_list = mixi_diary_origin.split(seperator)  # セパレーターを使って文章をリストに分割する
    mixi_diary_list = [x+seperator for x in mixi_diary_list]  # 文章の最後に。を追加
    #
    ##この時点でデータの準備が終わりです
    ##ここから形態素分析に入ります
    t = Tokenizer()
    
    mixi_diary_words = []  #形態素分析したあとに出てきた語句を格納するリスト(この例では、名詞、形容詞のみの語句を取っています)
    
    semantic_value = 0
    semantic_count = 0
    for sentence in mixi_diary_list:
        tokens = t.tokenize(sentence)
        words = []
        for token in tokens:
            # 品詞を取り出し
            partOfSpeech = token.part_of_speech.split(',')[0]
            #感情分析(感情極性実数値より)
            if( partOfSpeech in ['動詞','名詞', '形容詞', '副詞']):
                if(token.surface in dic_pn):
                    data = token.surface + ":" + str(dic_pn[token.surface])
                    semantic_value = dic_pn[token.surface] + semantic_value
                    semantic_count = semantic_count + 1
                else:
                    semantic_count = semantic_count + 1
            
            words.append(token.surface)
        
        if len(words) > 0:
            mixi_diary_words.extend(words)

    return [semantic_value,semantic_value / semantic_count]