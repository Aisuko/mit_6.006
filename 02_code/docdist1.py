###############################
# Count frequency of each word
###############################
def count_frequency(word_list):
    """
    Return a list giving pairs of form: (word, frequency)
    """
    L = []
    for new_word in word_list:
        for entry in L:
            if new_word==entry[0]:
                entry[1]+=1
                break
            else:
                L.append([new_word,1])
    return L



###################################
# Operation 4: sort words into alphabetic order
###################################
def insertion_sort(A):
    """
    Sort list A into order, in place
    """
    s=len(A)
    for j in range(s):
        key=A[j]
        i=j-1
        while i>-1 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A


# cf=count_frequency([1,1,1,2,3,4,5,5])
# print(cf)

a=insertion_sort([2,7,1,0,5])
print(a)
