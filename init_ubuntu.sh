#！/bin/sh

sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
 
sudo echo deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse > /etc/apt/sources.list
sudo echo deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse >> /etc/apt/sources.list
sudo echo deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse >> /etc/apt/sources.list
sudo echo deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse >> /etc/apt/sources.list

# 源码  
sudo echo deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse >> /etc/apt/sources.list
sudo echo deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse >> /etc/apt/sources.list
sudo echo deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse >> /etc/apt/sources.list
sudo echo deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse >> /etc/apt/sources.list

 
apt update
apt upgrade -y
# ————————————————
# 版权声明：本文为CSDN博主「liuyangbo121」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/liuyangbo121/article/details/82972724
