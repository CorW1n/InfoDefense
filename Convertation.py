def StrToVec(p):
	p = p.replace('+', ' ')
	p = p.split()
	for i in xrange(len(p)):
		if p[i] == '1':
			p[i] = 0
		elif p[i] == 'x':
			p[i] = 1
		elif 'x' in p[i]:
			p[i] = int(p[i].replace('x', ''))
		else:
			p[i] = None
	a = [0] * (max(p) + 1 if len(p) > 0 and max(p) != None else 0)
	for i in p:
		if i != None:
			a[i] = 1 - a[i]
	return a[::-1]

def ArrToStr(a):
	res = '@'
	for i in a:
		if i == 0:
			res += ' + 1'
		elif i == 1:
			res += ' + x'
		else:
			res += ' + x' + repr(i)
	res = res.replace('@ + ', '')
	if res == '@':
		res = '0'
	return res

def VecToArr(v):
	res = []
	vec = v[::-1]
	for i in xrange(len(v)):
		if vec[i] == 1:
			res.append(i)
	return res[::-1]

def ArrToVec(a):
	if len(a) > 0:
		return [1 if i in a else 0 for i in xrange(max(a) + 1)][::-1]
	else:
		return [0]

def VecToStr(v):
	return ArrToStr(VecToArr(v))

def StrToArr(s):
	return VecToArr(StrToVec(s))

def ArrToNum(a):
	if len(a) > 0:
		return sum([2 ** i for i in a])
	else:
		return 0

def NumToArr(n):
	if n == 0:
		return []
	cur = 1
	i = 0
	while cur <= n:
		cur *= 2
		i += 1
	cur //= 2
	i -= 1
	arr = []
	while cur > 0:
		if n >= cur:
			arr.append(i)
			n -= cur
		cur //= 2
		i -= 1
	return arr

def NumToVec(n):
	if n == 0:
		return []
	cur = 1
	while cur <= n:
		cur *= 2
	cur //= 2
	vec = []
	while cur > 0:
		if n >= cur:
			vec.append(1)
			n -= cur
		else:
			vec.append(0)
		cur //= 2
	return vec

def VecToNum(v):
	return sum([2 ** i for i in xrange(len(v)) if v[-1 - i] == 1])

def StrToNum(s):
	return ArrToNum(StrToArr(s))

def NumToStr(n):
	return ArrToStr(NumToArr(n))

def VecToVec8(v):
	if len(v) == 8:
		return v
	elif len(v) < 8:
		return [0] * (8 - len(v)) + v
	else:
		return v[:8]