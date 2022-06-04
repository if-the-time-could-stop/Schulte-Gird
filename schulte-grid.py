#coding:utf-8
#Developed by Tony Choi (蔡梓溢）
#Published under the Unlicense

import os
import math
import time
import random

try:
    while True:
        if os.name=="nt":
            os.system("CLS")
        else:
            os.system("clear")
        print("舒尔特方格训练程序\nTony Choi（蔡梓溢）\nv0.0.0.0-beta\n•您必须先同意我们的软件许可协议，然后才能使用此软件•")
        print("[0]开始训练\n[1]查看软件许可协议\n[2]开发人员名单\n[3]退出程序\n请输入选项前的序号以选择。按[Enter]结束输入。")
        s=input("请输入>")
        try:
            n=int(s)
        except:
            print("输入错误，请检查后重新输入")
            continue
        if n<0 or n>3:
            print("输入错误，请检查后重新输入")
            continue
        if n==0:
            print("有关舒尔特方格的标准版本，请参阅https://baike.baidu.com/item/%E8%88%92%E5%B0%94%E7%89%B9%E6%96%B9%E6%A0%BC/5372437\n（本软件所有开发者与百度公司没有任何联系，百度公司对于本软件对其网站连接的引用并不知情）")
            while True:
                print("请输入方格行数")
                l=input("请输入>")
                print("请输入方格列数")
                c=input("请输入>")
                print("请输入随机数种子")
                s=input("请输入>")
                try:
                    line=int(l)
                    col=int(c)
                    seed=int(s)
                except:
                    print("输入错误，请检查后重新输入")
                    continue
                det=[]
                for i in range(line):
                    tmp=[]
                    for j in range(col):
                        tmp.append(0)
                    det.append(tmp)
                sou=list(range(1,line*col+1))
                k=1
                for i in range(line):
                    for j in range(col):
                        random.seed(seed)
                        num=random.randint(0,line*col-k)
                        det[i][j]=sou[num]
                        del sou[num]
                        k+=1
                lg=math.ceil(math.log10(line*col))
                for i in range(line):
                    for j in range(col):
                        det[i][j]="{0!s:>0{1}}".format(det[i][j],lg)
                for i in range(line):
                    print("|",end="")
                    for j in range(col):
                        print(det[i][j],end="|")
                    print()
                st=time.time()
                print("计时开始")
                input("当完成后，请按下[Enter]以结束计时")
                et=time.time()
                print("你所用的时间是{0:.2f}s".format(et-st))
                input("按下[Enter]以返回主界面")
                break
        elif n==1:
            print("本软件使用The Unlicense许可证作为我们的软件许可协议。协议全文如下：\nThis is free and unencumbered software released into the public domain. \nAnyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means. In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law. \nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. For more information, please refer to <http://unlicense.org/>\n（本许可协议摘自https://unlicense.org/，协议原作者依据「CC0协议 1.0通用」在法律许可的最大范围内放弃了本协议内容的版权。协议原作者对于本软件对其协议的引用并不知情。）")
            input("按下[Enter]返回主界面")
        elif n==2:
            print("制作人员名单\n开发者：Tony Choi（蔡梓溢）\n鸣谢：苏昱文、qpython3h\n使用的第三方开源库：os、math、time、random（四者皆为python自带）\n使用Python以保证代码简洁和修改自由\n感谢https://unlicense.org/对The Unlicense协议版权的无偿放弃及其对自由软件事业的伟大贡献。")
            input("按下[Enter]返回主界面")
        else:
            break
except:
    print("出现了未知错误。若此问题重复出现，请联系开发者。\n按下[Enter]以退出……")
    input()