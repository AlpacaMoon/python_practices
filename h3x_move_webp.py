import os

dir_main = "D:/Images/H3x"
dir_HT = dir_main + "/HT"
dir_webp = dir_main + "/webps"

os.chdir(dir_HT)
print(os.getcwd())

for each in os.listdir():
    if each.endswith('webp'):
        os.rename(dir_HT + "/" + each, dir_webp + "/" + each)



os.chdir(dir_webp)
with open(dir_main + "/webp_list.txt", "w") as f:
    for each in os.listdir():
        if each.find("master1200") != -1:
            f.write("https://www.pixiv.net/en/artworks/" + each[:each.find('_')] + "\n")