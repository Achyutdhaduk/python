
"""
->game atli parameter pass kari saki
-> *args ni jagyaye *achyut api saku"""

def sumofnumber(*args):
    print(args)
    return sum(args)

print(sumofnumber(1,2,3,4,5))
print(sumofnumber(1,2,3,4,5,6,7,8,9))
print(sumofnumber(1,2,3,4,5,1,1,1,1,1,1,1,1,1,))

"""
def sumofnumber(*achyut):
    return sum(achyut)
    """


"""
def sumofnumber(*achyut):
    print(achyut)
    for i in achyut:
    print(i)
    return sum(achyut)
    """
