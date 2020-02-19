def sieve_of_eratosthenes(n):
    bool_list = [True for x in range(n-1)]
    prime_list = [0]

    for i in range(len(bool_list)):
        if bool_list[i]:
            prime_list.append(i+2)
            for k in range(1, (len(bool_list)+1) // (i+2)):
                bool_list[i + (i+2) * k] = False
                
    return prime_list
