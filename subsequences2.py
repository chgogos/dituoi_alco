def all_subsequences(s):
    out = []
    for c in s:
        # new_seqs: αντίγραφα των λεκτικών που υπάρχουν στο out, 
        # σε καθένα από τα οποία προστίθεται ο χαρακτήρας c στο τέλος
        new_seqs = []
        for x in out:
            new_seqs.append(x + c)
        out += new_seqs
        out.append(c)
    return out


subsequences = all_subsequences("ΤΑΞΗ")
print(subsequences)
