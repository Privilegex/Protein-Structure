def save_dist_to_contacts_rr(seq, pred_matrix, file_rr):
    rr = open(file_rr, 'w')
    rr.write(seq + "\n")
    P = np.copy(pred_matrix)
    maxd = np.max(P)
    L = len(P[:])
    for j in range(0, L):
        for k in range(j, L):
            P[j, k] = (P[k, j, 0] + P[j, k, 0]) / 2.0
    PROB = 4.0 / P
    PROB[PROB > 1.0] = 1.0
    for j in range(0, L):
        for k in range(j, L):
            if abs(j - k) < 5:
                continue
            rr.write("%i %i 0 8 %.5f\n" %(j+1, k+1, PROB[j][k]))
    rr.close()
    print('Written RR ' + file_rr + ' !')
