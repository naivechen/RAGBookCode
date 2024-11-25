
def rule_based_chunking(text):
    chunks = []
    current_chunk = []
    for line in text.split("\n"):
        if line.strip(): # 如果行不为空
            current_chunk.append(line.strip())
        elif current_chunk: # 如果遇到空行且当前分块不为空，则将当前分块加入结果列表中
            chunks.append("\n".join(current_chunk))
            current_chunk = []
    if current_chunk: # 处理最后一个分块
        chunks.append("\n".join(current_chunk))
    return chunks

# 示例文本
text = """
这是第一个段落。

这是第二个段落，它有多行。
第二行。
第三行。

这是第三个段落。
"""
# 使用基于规则的文档分块方法对示例文本进行分块
chunks = rule_based_chunking(text)
# 打印分块结果
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")