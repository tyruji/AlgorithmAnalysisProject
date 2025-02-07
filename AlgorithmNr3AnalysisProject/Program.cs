/*

    Input:
        array A of n elements containing natural numbers, sorted ascending
        array B of m elements containing natural numbers, sorted ascending

    Output:
        Odd number count from a disjoint union operation on arrays A and B. 

    Disjoint union - append only the numbers not present in both arrays, e.g.
    for: A={1,2,3,5,8}, B={0,1,3,4,8,9,10} disjoint union returns: {0,2,4,5,9,10}

*/


Console.WriteLine( disjointUnionOddCount( [1, 2, 3, 5, 8], [0, 1, 3, 4, 8, 9, 10] ) );




int disjointUnionOddCount( int[] A, int[] B )
{
    return countOddFromAinB( A, B ) + countOddFromAinB( B, A );
}

int countOddFromAinB( int[] A, int[] B )
{
    int result = 0;
    for( int i = 0; i < A.Length; ++i )
    {
        if( ( A[ i ] & 1 ) == 0 ) continue;

        if( binarySearch( A[ i ], B ) != -1 ) continue;
        ++result;
    }
    return result;
}

int binarySearch( int num, int[] arr )
{
    int left = 0, right = arr.Length - 1;

    while( left <= right )
    {
        int center = ( left + right ) / 2;

        if( arr[ center ] == num ) return center;

        if( arr[ center ] < num ) left = center + 1;
        else right = center - 1;
    }

    return -1;
}

/*

    time complexity: O( n*log(m) + m*log(n) ) 

*/