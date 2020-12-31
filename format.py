from pathlib import Path
import re

p = Path('/tmp')

math = p /'math.txt'
temp = p / 'ans.txt'
break_sentence = p / 'break.txt'
"""
create /temp/math.txt
then run this program,
In order to fill anki card format
$$ will replace to [$][/$]
\[ \]will replace to [$$][/$$]
"""
if math.exists():
    # with math.open() as f:
    #     text = f.read()
    #     s = '1\n'
    #     f.write(s)
    math.touch()
    s = math.read_text()
    # s = re.sub(r'\$\n*(.+?)\n\$', r'[$]\1[/$]', s)
    # s = re.sub(r'\$\n*(.+?)\n*\$', r'[$]\1[/$]', s)
    # s = re.sub(r'\$(.+?)\$', r'[$]\1[/$]', s)
    s = re.sub(r'\$(.*)\$', r'[$]\1[/$]', s)
    s = re.sub(r'\\\[', r'[$$]', s)
    s = re.sub(r'\\\]', r'[/$$]', s)
    math.write_text(s)

"""
create /tmp/break.txt
run this program,
,.; will be break to fit the latex sentence
"""

if break_sentence.exists():
    break_sentence.touch()
    s = break_sentence.read_text()
    s = re.sub('([^A|B|C|D])，',r'\1,\n',s)
    s = re.sub('([A|B|C|D]?)[，|,]', r'\1. ', s)
    s = s.replace(';', ';\n')
    s = s.replace('?', '?\n')
    s = s.replace('。', '.\n')
    # s = s.replace(': ', ':\n')


    # temp.write_text(s)
    break_sentence.write_text(s)
