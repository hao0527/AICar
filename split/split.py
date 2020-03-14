import os
import numpy as np
import time
from sys import argv
from sklearn.model_selection import train_test_split
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # 这里主要实现从命令行取得需要读取的文件  默认读取文件为normal.txt
    parser.add_argument('-f', '--file', type=str, default='normal.txt',
                        help='txt file')

    # 解析命令行获取的参数
    args, unparsed = parser.parse_known_args()
    # 获取文件名及格式
    filename = args.file.split("\\")[-1]

    fp1 = open(filename, 'r+')
    str2 = fp1.read()

    str1 = ""
    str3 = ""
    str4 = ""
    num = 0
    for i in str2:
        if i == ' ':                # 找到空格
            num += 1                # 数量+1
            str3 += str1 + i

            if str1 == "5A":        # 找到固定数据
                if num < 11:        # 数据不够 继续统计
                    pass
                elif num == 11:     # 找到一组数据
                    str3 += "\r"    # 插入换行
                    str4 += str3    # 保存获得的字符串
                    num = 0         # 清空统计
                    str3 = ""
                else:               # 固定数据出现丢失 导致一组数据过多 丢弃
                    num = 0         # 清空统计
                    str3 = ""

            str1 = ""  # 清空
        else:
            str1 += i
    fp1.close()

    fp2 = open("split_" + filename, 'w+')
    fp2.write(str4)
    fp2.close()

