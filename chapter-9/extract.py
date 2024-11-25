# 代码 9-1 

from pypdf import PdfReader 
import time 

reader = PdfReader('example.pdf') 

page_len  = len(reader.pages)

for i in range(page_len):

    page = reader.pages[i] 
    
    text = page.extract_text() 
    with open(f"data/{i}.txt", "w", encoding="utf-8") as fw:
        fw.write(text)

    print(f"{i}/{page_len}")
    print(text) 
    