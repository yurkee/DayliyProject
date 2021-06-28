# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/21 18:42
"""
import os
import shutil

os.remove('data_write.txt')

# print(os.getcwd())
# dirpath = r'd:\dirdemo\subdir'
# if not os.path.exists(dirpath):
#     # os.mkdir(dirpath)
#     os.makedirs(dirpath)
# else:
#     # os.rmdir(dirpath)
#     shutil.rmtree(dirpath)

# filenames = os.listdir(os.getcwd())
# for fname in filenames:
#     print(fname)

# for files in os.walk(os.getcwd()):
#     print(files)

#序列解包
# for dirpath, subdirs, files in os.walk(os.getcwd()):
#     for name in subdirs:
#         print('mulu', os.path.join(dirpath, name))
#     for name in files:
#         print('wenjian', os.path.join(dirpath, name))