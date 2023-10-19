from strsimpy.jaro_winkler import JaroWinkler
# https://github.com/luozhouyang/python-string-similarity
jarowinkler = JaroWinkler()
print(jarowinkler.similarity('My string', 'My tsring'))# 0.9740740740740741
print(jarowinkler.similarity('My string', 'My ntrisg'))#0.8962962962962963

