import nltk
groucho_grammar = nltk.parse_cfg("""
    s -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | 'my'
    N -> 'elephant' | 'pajamas'
    V -> 'shot'
    P -> 'in'                        
    """ 
)
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
    print tree

'''    
outputs:
(s
      (NP I)
        (VP
                    (V shot)
                        (NP (Det an) (N elephant) (PP (P in) (NP (Det my) (N
                            pajamas)))))
    )
(s
          (NP I)
            (VP
                    (VP (V shot) (NP (Det an) (N elephant)))
                        (PP (P in) (NP (Det my) (N pajamas))))
        )
'''

''' comment:
I shot an elephant in my pajamas. 

A better construction of the sentence would be: I was wearing pajamas when I
shot the elephant. (if that's what he meant to say.) 

But Groucho played with the words. First you think that Groucho was
wearing pajamas when he shot the elephant. Then you realize, as he
continues, that it was the elephant that was wearing the pajamas when
Groucho says "how he got in my pajamas, I'll never know." "'"
 '''
