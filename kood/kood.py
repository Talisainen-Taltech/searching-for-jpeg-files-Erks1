import os

files = os.listdir(r"C:\Users\erkil\OneDrive\Desktop\Kood\Skriptimiskeeled\random_files")

for file in files:
    with open(fr"C:\Users\erkil\OneDrive\Desktop\Kood\Skriptimiskeeled\random_files\{file}", "r", encoding="latin-1") as f:
        text = f.readlines()
        if "ÿØÿÛ" in text:
            print(file)
