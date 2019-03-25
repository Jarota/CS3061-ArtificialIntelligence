#addressed like -> ProbabilityRewardMatrices[<a>][<s>][<s'>][0 or 1]
ProbabilityRewardMatrices = {
	'exercise': {
		'fit': {
			'fit': [0.9*0.99, 8],
			'unfit': [0.9*0.01, 8],
			'dead': [0.1, 0]
		},
		'unfit': {
			'fit': [0.9*0.2, 0],
			'unfit': [0.9*0.8, 0],
			'dead': [0.1, 0]
		},
		'dead': {
			'fit': [0, 0],
			'unfit': [0, 0],
			'dead': [1, 0]
		}
	},
	'relax': {
		'fit': {
			'fit': [0.99*0.7, 10],
			'unfit': [0.99*0.3, 10],
			'dead': [0.01, 0],
		},
		'unfit': {
			'fit': [0.99*0, 5],
			'unfit': [0.99*1, 5],
			'dead': [0.01, 0]
		},
		'dead': {
			'fit': [0, 0],
			'unfit': [0, 0],
			'dead': [1, 0]
		}
	}
}

n = input("Enter a positive integer n: ")
try:
	n = int(n)
except:
	print("n must be an integer!")
	exit(1)

G = input("Enter a lambda-setting G (0 < G < 1): ")
try:
	G = float(G)
	if G <= 0 or G >= 1:
		raise Exception
except:
	print("G must be a number between 0 and 1!")
	exit(2)

S = ['fit', 'unfit', 'dead']	# states

s = input("Enter a statae 's' (fit, unfit, dead): ")
if s not in S:
	print("s must be either fit, unfit, or dead!")
	exit(3)

print("")
print("n:", n)
print("G:", G)
print("s:", s)

def p(s, a, sprime):
	return ProbabilityRewardMatrices[a][s][sprime][0]

def r(s, a, sprime):
	return ProbabilityRewardMatrices[a][s][sprime][1]

def V(n, s):
	return max(q(n, s, 'exercise'), q(n, s, 'relax'))

def q(n, s, a):
	if n == 0:
		return (
			p(s, a, 'fit')*r(s, a, 'fit') +
			p(s, a, 'unfit')*r(s, a, 'unfit') +
			p(s, a, 'dead')*r(s, a, 'dead')
		)

	return (
		q(0, s, a) +
		(G*(p(s, a, 'fit')*V(n-1, 'fit') +
		p(s, a, 'unfit')*V(n-1, 'unfit') +
		p(s, a, 'dead')*V(n-1, 'dead')))
	)

print("")
print("qn(s, exercise):", q(n, s, 'exercise'))
print("qn(s, relax):", q(n, s, 'relax'))
exit(0)
