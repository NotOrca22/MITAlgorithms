def SeqToSet(seq):
    set = {}
    for i in range(len(seq)):
        set[i] = seq[i]
    return set
if __name__ == "__main__":
    print(SeqToSet([2,5,8,1]))
