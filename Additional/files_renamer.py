from pathlib import Path
import re


a = Path('/Users/user/Downloads/Комбинаторика Stepic')

pattern = r'ответы'
b = a.glob('*')
for item in b:
    text = re.search(pattern, str(item))
    if text:
        result = re.sub(pattern, 'Ответы', str(item))
        print(item)
        print(result)
