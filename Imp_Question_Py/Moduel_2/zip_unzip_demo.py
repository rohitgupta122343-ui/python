
import zipfile as z

# Create zip
with z.ZipFile("archive.zip","w")as zipf:

    zipf.write("file1.txt")
    zipf.write("file2.txt")

# Create Extract
with z.ZipFile("archive.zip","r")as zipf:

    zipf.extractall("unzip")