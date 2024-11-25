# 代码 9-2

"""
1. 去除一些空格，回车符等等；
2. 去除长度每行小于5的字符串；
3. 按照行对文档内容进行分块处理；
"""

stop_word = ['\uf06c']
page_len = 15
for i in range(page_len):
    fw = open(f"chunk/{i}.txt", "w", encoding="utf-8")
    with open(f"data/{i}.txt", "r", encoding="utf-8") as fr:
        readlines = fr.readlines()
        for line in readlines:
            line = line.strip().split()
            print(line)
            # 写入文件
            tmp = ""
            for item in line:
                if item not in stop_word:
                    tmp = tmp + item  + " "
            tmp = tmp.strip()
            if len(tmp)>5:
                fw.write(tmp+"\n")
    
    fw.close()