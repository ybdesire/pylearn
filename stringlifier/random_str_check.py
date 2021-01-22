from stringlifier.api import Stringlifier

stringlifier=Stringlifier()
s7= "asdfasasdfbwer.werasdfasgefe.vatgdgasfddsa.hwhefasdfa.hello.yes.aaaaaaaaaa"
s, tokens = stringlifier(s7, return_tokens=True)
print(s)
#['<RANDOM_STRING>.werasdfasgefe.<RANDOM_STRING>.<RANDOM_STRING>.hello.yes.<RANDOM_STRING>']
print(tokens)
# [[('asdfasasdfbwer', 0, 14, '<RANDOM_STRING>'), ('vatgdgasfddsa', 29, 42, '<RANDOM_STRING>'), ('hwhefasdfa', 43, 53, '<RANDOM_STRING>'), ('aaaaaaaaaa', 64, 73, '<RANDOM_STRING>')]]
