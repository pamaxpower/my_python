import os

dir = 'sort'
k = 'video'
new_dir = os.path.join(os.getcwd(), dir, k)
print(new_dir)
print(os.path.join(dir))