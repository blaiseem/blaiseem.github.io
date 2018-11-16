import os

for root, dirs, files in os.walk(r".\charts"):
    indexFileText = """{}\n<br>\n<br>\n\n""".format(root.split('\\')[-1].title())
    for file in files:
        if ('.html' in file) and ('index.html' not in file):
            needIndex = True
            indexFileText += """<a href="{}">{}</a>\n<br>\n""".format(file,file.replace('.html',''))
    if needIndex:
        fileHtml = open(root + '\\index.html','w')
        fileHtml.write(indexFileText)
        fileHtml.close()
        print(root + '\\index.html')