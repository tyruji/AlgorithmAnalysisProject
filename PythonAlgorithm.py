def disjointUnionOddCount( A, B ):
    n, m = len( A ), len( B )
    i, j = 0, 0
    c = 0
    
    while i < n and j < m:
        if A[ i ] < B[ j ]:         # A[ i ] nie występuje w B
            if A[ i ] & 1 == 1:     # oraz jest nieparzyste
                c += 1
            i += 1
            
        elif A[ i ] > B[ j ]:       # B[ j ] nie występuje w A
            if B[ j ] & 1 == 1:     # oraz jest nieparzyste
                c += 1
            j += 1
            
        else:                       # A[ i ] == B[ j ] pomiń
            i += 1
            j += 1 
                    # W przypadku gdy jedna tablica jest większa od drugiej
                    # sprawdź pozostałe elementy
    while i < n:
        if A[ i ] & 1 == 1:
            c += 1
        i += 1
            
    while j < m:
        if B[ j ] & 1 == 1:
            c += 1
        j += 1         
    
    return c

A=[1,2,3,5,8]
B=[0,1,3,4,8,9,10]

print( disjointUnionOddCount( A,B ) )