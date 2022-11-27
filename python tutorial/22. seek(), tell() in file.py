from io import SEEK_CUR


f= open("yash.txt")
print(f.tell())
print(f.readline())
print(f.seek(10))
print(f.readline())
f.close()