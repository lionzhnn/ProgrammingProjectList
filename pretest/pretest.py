# -*- coding: utf-8 -*-
import sys,tkFileDialog,os
from Tkinter import*
#逆转字符串——输入一个字符串，将其逆转并输出
def reverseString(s):
    return s[::-1]
#拉丁猪文字游戏——这是一个英语语言游戏。基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”）。
def latinWordGame(s):
    for index,item in enumerate(s):
        if item not in ['a','e','i','o','u']:
            break
    return s[:index]+s[index+1:]+'-'+s[index]+'ay'
#统计元音字母——输入一个字符串，统计处其中元音字母的数量
def countVowel(s):
    counting={'a':0,'e':0,'i':0,'o':0,'u':0};
    for index,item in enumerate(s):
        if item in ['a','e','i','o','u']:
            counting[item] +=1
    return counting
#判断是否为回文
def isplalindrome(s):
    reverse=s[::-1]
    return reverse==s and len(s)
#统计字符串中的单词数目
def countWord(s):
    counting=s.split(' ')
    return len(counting)
#文本编辑器——记事本类型的应用，可以打开、编辑、保存文本文档。可以增加单词高亮和其它的一些特性。

if __name__=="__main__":
    result=countWord("We trained a large, deep convolutional neural network.")
    print(result)
