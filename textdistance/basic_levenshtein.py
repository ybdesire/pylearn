import textdistance


d1 = textdistance.levenshtein('arrow', 'arowexy')
d2 = textdistance.levenshtein.normalized_similarity('arrow', 'arowexy')
d3 = textdistance.levenshtein.normalized_similarity('arrow', 'arow')
d4 = textdistance.levenshtein.normalized_similarity('arrow', 'arrow')

print(d1)#4
print(d2)#0.4285714285714286
print(d3)#0.8
print(d4)#1.0

# for normalized_similarity
# 1 is most similar
# 0 is most not similar