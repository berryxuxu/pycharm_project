"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = []
    for i in line:
        if i != 0:
            new_line.append(i)

    while len(new_line)<len(line):
        new_line.append(0)

    #print '/n'
    #print 'newline', new_line
    newnew_line = [ ]
    #print 'newnew_line' ,newnew_line
    ii = 0
    while ii < len(line):
        try:
            if new_line[ii] == new_line[ii+1] and new_line[ii] !=0 :
                newnew_line.append(2 * new_line[ii])
                ii += 2
            else:
                newnew_line.append(new_line[ii])
                ii += 1
        except:
            newnew_line.append(new_line[ii])
            ii += 1

    #print 'newnew_line' ,newnew_line

    for i in new_line:
        if i == 0:
            new_line.remove(i)

    while len(newnew_line)<len(line):
        newnew_line.append(0)

    return newnew_line