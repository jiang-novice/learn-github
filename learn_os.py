import os

path = "/home/jasonjiang/jason.jiang_test/"
all_dir = os.listdir(path)

for file in all_dir:
    all_file = os.path.join(path,file)
    filepath, file_ext = os.path.splitext(all_file)
    filename = os.path.basename(all_file)
    flie_dir = os.path.dirname(all_file)
    print(flie_dir)

path_ = "/home/jasonjiang/jason.jiang_test/001.png"
if not os.path.exists(path_):
    print("this path is not exist") 