import ast

s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
d = ast.literal_eval(s)
print( type(d) )
print( d['muffin'] )


