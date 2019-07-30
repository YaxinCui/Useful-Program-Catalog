import os
from shutil import copyfile

# kaggle kernel需要连接网络

print("../input:", os.listdir("../input"))
# 列出Glove向量文件名

if not os.path.exists("./vector_cache"):
    os.mkdir("./vector_cache")

if not os.path.exists("./vector_cache/glove.6B.300d.txt"):
    if os.path.exists("../input/nlpword2vecembeddingspretrained"):
        copyfile("../input/nlpword2vecembeddingspretrained/glove.6B.300d.txt", "./vector_cache/glove.6B.300d.txt")
        copyfile("../input/nlpword2vecembeddingspretrained/glove.6B.50d.txt", "./vector_cache/glove.6B.50d.txt")
    else:
        copyfile("../input/glove.6B.300d.txt", "./vector_cache/glove.6B.300d.txt")
        copyfile("../input/glove.6B.50d.txt", "./vector_cache/glove.6B.50d.txt")
    # 把想要使用的Glove词向量转移到output/vector_cache文件夹中，将vector_cache文件夹作为缓存文件夹
print("./vector_cache:", os.listdir("./vector_cache"))
