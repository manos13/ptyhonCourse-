def genPrimes ():
	last = 1
	D = []
	while True:
		last += 1 
		for p in D:
			if last % p == 0:
					break
		else:
			D.append(last)
			yield last