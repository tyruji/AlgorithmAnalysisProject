from mpl_toolkits import mplot3d
import numpy as np
import time
import math
from random import sample
import matplotlib.pyplot as plt
from PythonAlgorithm import disjointUnionOddCount

def plot_func( n, m ):
    A = sorted( sample( range( 0, 9999 ), n ) )
    B = sorted( sample( range( 0, 9999 ), m ) )
    
    start_time = time.time()
    disjointUnionOddCount( A, B )
    return time.time() - start_time

def get_func_time( n, m, repeat ):
    
    time = 0
    for i in range( repeat ):
        time += plot_func( n, m )
        
    return time / repeat

def conjectured_time_complexity( n, m ):
    return ( n + m ) / ( 25 * 10000000 / 30 )      # scaled to real data's peaks
    #return ( n * math.log( m ) + m * math.log( n ) ) / ( 10000000 * 16 / 20 ) STARA FUNKCJA

fig = plt.figure()
ax = plt.axes( projection='3d' )



max_data_size = 1500
data_size_step=100
#time_data = [ [ plot_func( x, y ) for x in range( max_data_size ) ] for y in range( max_data_size ) ]

xs = [ i for i in range( 1, max_data_size, data_size_step ) for _ in range( 1, max_data_size, data_size_step  ) ]
ys = list( range( 1, max_data_size, data_size_step  ) ) * int( max_data_size / data_size_step )



    # Change this to show from real function times
    # and the predicted time complexity function
show_func_graph = False



if show_func_graph:
    measurement_repeat = 350
    zs = [ get_func_time( x, y, measurement_repeat ) for x, y in zip( xs, ys ) ]
else:
    zs = [ conjectured_time_complexity( x, y ) for x, y in zip( xs, ys ) ]


ax.plot( xs, ys, zs, '-' )

ax.set_xlabel( "n" )
ax.set_ylabel( "m" )
ax.set_zlabel( "czas" )

    # Set rotation to view at a convincing angle
ax.view_init( 15, -130, 0 )

plt.show()
#disjointUnionOddCount()

'''
    Zrób tak:
        wykres 3d jeden
        zrob przykladowo wykresy 2d dla wybranch wartosci m, z zaleznoscia od n
        
        i odpowiednio zrob wykresy funkcji przewidzianej zlozonosci
        
        i porownaj je ze soba
'''