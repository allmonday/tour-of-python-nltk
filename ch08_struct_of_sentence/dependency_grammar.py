import nltk
groucho_dep_grammar = nltk.parse_dependency_grammar('''
    'shot'-> 'I'| 'elephant' | 'in'
    'elephant' -> 'an' | 'in'
    'in' -> 'pajamas'
    'pajamas' -> 'my'
''')

print groucho_dep_grammar

pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
print sent
trees = pdp.parse(sent)
for tree in trees:
    print tree

