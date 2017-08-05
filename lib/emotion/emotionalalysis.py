#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: emotionalalysis[D.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 四  8/ 3 16:06:21 2017
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class EmotionAnalysis:
    def __init__(self):
        """init"""
        self.negative_dict_path = "data/finance_negative.dat"
        self.positive_dict_path = "data/finance_positive.dat"
        self.positive_dict = {}
        self.negative_dict = {}

    def load_data(self):
        """load_data"""
        for item in file(self.negative_dict_path).readlines():
            self.negative_dict[item.strip()] = 1
        for item in file(self.positive_dict_path).readlines():
            self.positive_dict[item.strip()] = 1

    def process(self, content):
        self.load_data()
        positive_num = 0
        negative_num = 0
        for item in content:
            print "item:", item
            if self.positive_dict.has_key(item.encode('utf-8')):
                positive_num += 1
            if self.negative_dict.has_key(item.encode('utf-8')):
                negative_num += 1 
        tot = positive_num + negative_num
        ret = ""
        if tot > 0:
            positive_ratio = positive_num * 1.0 / tot
            print positive_ratio
            if positive_ratio >= 0.6:
                ret = "利多"
            elif positive_ratio <= 0.4: 
                ret = "利空"
            else:
                ret = "中性"
        else:
            ret = "中性"
        return ret


from flask import Flask,request  
app = Flask(__name__)
emotion_analysis = EmotionAnalysis()

@app.route('/', methods=['GET','POST'])
def process():
    query = request.args.get("query","")
    content = []
    for item in query.split("/"):
        content.append(item.strip())
    return emotion_analysis.process(content)

if __name__ == "__main__":
    app.run(debug=True,port=5004)
