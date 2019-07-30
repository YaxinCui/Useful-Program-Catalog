import os
from shutil import copyfile

print("../input:", os.listdir("../input"))
# 列出Glove向量文件名

if not os.path.exists("../output"):
    os.mkdir("../output")

if not os.path.exists("../output/vector_cache"):
    os.mkdir("../output/vector_cache")

if not os.path.exists("../output/vector_cache/glove.6B.300d.txt"):
    copyfile("../input/glove.6B.300d.txt", "../output/vector_cache/glove.6B.300d.txt")
    # 把想要使用的Glove词向量转移到output/vector_cache文件夹中，将vector_cache文件夹作为缓存文件夹
print("../output:", os.listdir("../output"))
print("../output/vector_cache:", os.listdir("../output/vector_cache"))