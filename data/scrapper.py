import json
import os

files = os.listdir('datasets/')

input = []
for f in files:

    with open(f'datasets/{f}', 'r') as f:

        text = f.read()
    text = text.replace('\n','')
    words = text.split(' ')
    
    for i in range(0,len(words) + 100,256):

        if i == 0:
            temp = words[i:(i+1)*512]
        else:
            temp = words[i-100:(i+1)*256 - 100]
        
        input.append(' '.join(temp))
    

with open('datasets/train.json','w') as f:

    json.dump(input,f)    