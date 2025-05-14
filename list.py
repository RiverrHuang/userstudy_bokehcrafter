import os

root = 'videos/ours'
txt = ''
for name in sorted(os.listdir(root)):
    if '.mp4' not in name:
        continue
    txt += name[:-4] + ','
print(txt)

print(list(range(18, 42)))