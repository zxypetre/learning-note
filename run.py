'''
自动生成README.md文件并使文件中的每一行生成一个在当前文件夹中以.md结尾的文件的文件名。
'''

import os
import urllib.parse


files = os.listdir()
with open('README.md', 'w') as f:
    for filename in files:
        if filename.endswith('.md'):
            encoded_filename = urllib.parse.quote(filename)
            f.write('* [%s](%s/)\n' % (filename, encoded_filename))