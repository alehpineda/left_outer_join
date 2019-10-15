import itertools

def left_outer_join(file_a, col_a, file_b, col_b):
    '''
    file_a and file_b are file path strings
    col_a and col_b are non-negative integers

    Prints out a left_outer_join of two CSV files, with
    the specified 0-index columns as the join keys. For
    simplicity, assume that a match only happens 0 or 1
    times, and that the lines within each file have the
    same number of columns.  Output the correct number of 
    NULLs if there is no match in file_b.

    Example:

    file_a "/mnt/data/file_a.csv":
    a,1,q
    b,3,7
    c,2,t

    file_b "/mnt/data/file_b.csv":
    a,d,g,2
    j,p,4,1

    left_outer_join(file_a, 1, file_b, 3) -->
    a,1,q,j,p,4,1
    b,3,7,NULL,NULL,NULL,NULL
    c,2,t,a,d,g,2

    left_outer_join(file_a, 0, file_b, 0) -->
    a,1,q,a,d,g,2
    b,3,7,NULL,NULL,NULL,NULL
    c,2,t,NULL,NULL,NULL,NULL
    '''
    file_a = []
    with open('file_a.txt') as f:
        for line in f:
            file_a.append(''.join(line.split()).split(','))

    file_b = []
    with open('file_b.txt') as f:
        for line in f:
            file_b.append(''.join(line.split()).split(','))
    
    for row_a in file_a:
        for row_b in file_b:
            #print(row_a, row_a[col_a], row_b, row_b[col_b])
            if row_a[col_a] == row_b[col_b]:
                print(','.join(row_a+row_b))
            #    if row_a[col_a] != row_b[col_b]:
            #        print(','.join(row_a)+',NULL'*len(row_b))
            #else:
            #    print(','.join(row_a)+',NULL'*len(row_b))


print('1st')
left_outer_join('file_a.txt', 1, 'file_b.txt', 3)
print('2nd')
left_outer_join('file_a.txt', 0, 'file_b.txt', 0)
