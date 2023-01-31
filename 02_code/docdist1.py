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
            if new_word ==entry[0]:
                entry[1]+=1
                break
        else:
            L.append([new_word,1])
    return L



###################################
# Operation 4: sort words into alphabetic order(inplace)
###################################
def insertion_sort(A):
    """
    Sort list A into order, in place and it uses 0-indexing
    """
    a_length=len(A)
    for j in range(a_length):
        key=A[j]
        i=j-1
        while i>-1 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A

##################################################
# Operation: 4: sort words into alphabetic order #
##################################################
def merge_sort(A):
    """
    Sort list A into order, and return result
    """
    n=len(A)
    if n==1:
        return A
    mid=n//2 #floor division
    L=merge_sort(A[:mid])
    R=merge_sort(A[mid:])
    return merge(L,R)


def merge(L,R):
    """
    Given two sorted sequences L and R, return their merge
    """
    i=0
    j=0
    answer=[]
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i+=1
        else:
            answer.append(R[j])
            j+=1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer




cf=count_frequency([1,1,1,2,3,4,5,5])
print(cf)

a=insertion_sort([2,7,1,0,5])
print(a)

b=merge_sort([2,2,7,1,0,5,3,4,8])
print(b)