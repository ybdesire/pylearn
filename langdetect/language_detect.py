from langdetect import detect

lang = detect("Ein, zwei, drei, vier")
print(lang)

lang = detect("这里是一些中文")
print(lang)

lang = detect("English is a language.")
print(lang)

'''
de
zh-cn
en
'''



