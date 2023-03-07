with open('openai_key.txt', 'w') as f:
    f.writelines("aoba")
    f = f.read()
    print(f[f.find('=')+1:])