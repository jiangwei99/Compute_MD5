import hashlib

import os


def find_file(path):
    file_list = []  # 新建一个空列表用于存放文件名
    file_dir = path  # 指定即将遍历的文件夹路径
    for files in os.walk(file_dir):  # 遍历指定文件夹及其下的所有子文件夹
        for file in files[2]:  # 遍历每个文件夹里的所有文件，（files[2]:母文件夹和子文件夹下的所有文件信息，files[1]:子文件夹信息，files[0]:母文件夹信息）
            if os.path.splitext(file)[1] == '.PDF' or os.path.splitext(file)[1] == '.pdf':  # 检查文件后缀名,逻辑判断用==
                # file_list.append(file)#筛选后的文件名为字符串，将得到的文件名放进去列表，方便以后调用
                file_list.append(file_dir + '\\' + file)  # 给文件名加入文件夹路径
    print(file_list)
    return file_list


if __name__ == '__main__':
    file_file = find_file('files')
    f = open("output.txt", 'w').close()
    for pdf_name in file_file:
        print(pdf_name)
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(pdf_name, "rb") as file:
            buf = file.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(BLOCKSIZE)
        result = hasher.hexdigest()
        print(result)

        with open("output.txt", "a") as f:
            f.write("文件名：")
            f.write(pdf_name)
            f.write("\n")
            f.write("MD5值：")
            f.write(result)  # 这句话自带文件关闭功能，不需要再写f.close()
            f.write("\n")

        # command = 'pdf2eps.bat 1 ' + pdf_name
        # print(command)
        # os.system(command)
        #

# BLOCKSIZE = 65536
# hasher = hashlib.md5()
# file_path = "D:\\Data\\OneDrive\\Write_Paper\\Jiang\\Save_Paper\\Submit\\Test-and-Decode A Partial Recovery Scheme for Verifiable Coded Computing.pdf"  # 输入文件地址
# with open(file_path, "rb") as file:
#     buf = file.read(BLOCKSIZE)
#     while len(buf) > 0:
#         hasher.update(buf)
#         buf = file.read(BLOCKSIZE)
# print(hasher.hexdigest())
