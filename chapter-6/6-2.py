
def sliding_window(text, window_size):
    chunks = []
    for i in range(0, len(text), window_size):
        chunk = text[i:i+window_size]
        chunks.append(chunk)
    return chunks
# 示例文本
text = "这是一个示例文本，用于演示滑动窗口的分块算法。"
# 设置窗口大小为 10
window_size = 10
# 使用滑动窗口进行分块
chunks = sliding_window(text, window_size)
# 打印分块结果
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")