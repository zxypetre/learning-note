import os
files = os.listdir()
with open('README.md','w') as f:
    for file in files:
        if file.endswith('.md'):
            f.write('* ['+file+']('+file+'/)\n')