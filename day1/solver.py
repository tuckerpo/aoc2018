import sys

def get_inputs(path='.'):
	with open(path) as f:
		return f.readlines()

def do_sum(list, mapping=False):
	sum = 0
	most_recent_freq = set()
	most_recent_freq.add(sum)
	while 1:
		for freq in list:
			sum += int(freq)
			if (mapping):
				if sum in most_recent_freq:
					return sum
			most_recent_freq.add(sum)
	return sum

def main():
	parsed_inputs = [inputs.strip() for inputs in get_inputs('./input.txt')]
	print(do_sum(parsed_inputs, mapping=True))

if __name__ == '__main__':
	main()