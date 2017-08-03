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
            if self.positive_dict.has_key(item):
                positive_num += 1
            if self.negative_dict.has_key(item):
                negative_num += 1
            print "result:", item, "下跌"
            print self.negative_dict.has_key("下跌")
            print self.negative_dict.has_key(item)
            if item.encode('utf-8') == "下跌":
                print "OKKK"
            #print self.negative_dict["下跌"]
            #print "item",item,positive_num, negative_num
        if positive_num > negative_num:
            return "看涨"
        if positive_num < negative_num:
            return "看跌"
        return "中性"

from flask import Flask,request  

app = Flask(__name__)
emotion_analysis = EmotionAnalysis()

@app.route('/', methods=['GET','POST'])
def process():
    query = request.args.get("query","").encode('utf-8')
    content = []
    for item in query.split("/"):
        content.append(item.strip())
    print "11"
    print "ret:", emotion_analysis.process(content)
    print "11"
    return emotion_analysis.process(content)

if __name__ == "__main__":
    app.run(debug=True,port=5004)
