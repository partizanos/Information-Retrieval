si = fmax * (ti - tmin) / (tmax - tmin)


# the most frequent term t ī in a document d j always has tf īj = 1

def maxFreq = lambda ( )

tf = lambda  term, document : freq(
    term, document) / maxFreq( document)

'''
The inverse document frequency idf i is a measure of the general 
importance of the term t i in the whole corpus.
'''
import numpy as np
idf = lambda term, all_documents : np.log2( 
    len( all_documents) / 
)


w = lambda (term, document) = tf(term, document) * idf(term, document)