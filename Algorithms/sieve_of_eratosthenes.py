MAX = 1000010
primes = []
divis = []
sieve = None

def build_sieve_opt():
    global sieve, primes, divis
    sieve = [True for i in range(MAX)]
    divis = [None for i in range(MAX)]
    sieve[0], sieve[1], sieve[2] = False, False, True
    primes.append(2)
    divis[2] = 2; divis[1] = 1
    for i in range(4, MAX, 2):
        sieve[i] = False; divis[i] = 2
    for i in range(3, MAX, 2):
        if sieve[i]:
            primes.append(i); divis[i] = i
            for j in range(i*i, MAX, i):
                sieve[j] = False
                divis[j] = i
                
build_sieve_opt()

print(divis[:100])
