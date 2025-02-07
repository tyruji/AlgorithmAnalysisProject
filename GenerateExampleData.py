from random import sample, randint
from PythonAlgorithm import disjointUnionOddCount

repeat=1
min_len=2
max_len=5
max_value=10

for i in range( repeat ):
    #A = sorted( sample( range( max_value ), randint( min_len, max_len ) ) )
    #B = sorted( sample( range( max_value ), randint( min_len, max_len ) ) )
    
    A = [ 4, 5, 6 ]
    B = [ 1, 2, 6, 8, 9 ]
    
    print( "-------------. ", i, " .-------------" )
    print( "" )
    print( "A: ", A, " n: ", len( A ) )
    print( "B: ", B, " m: ", len( B ) )
    print( "c: ", disjointUnionOddCount( A, B ) )

