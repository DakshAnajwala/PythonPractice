import multiprocessing
import sys

def round_robin_count():
	while(True):
		number = 0
		if(number >= sys.maxsize):
			number = 0
		else:
			number = number + 1


if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == '--about':
		print(__doc__)
	elif len(sys.argv) == 2 and sys.argv[1] == '--help':
		print('Heater', 'USAGE: python3 ' + sys.argv[0] + ' [option]', sep='\n')
		print('To read about.', 'python3 ' + sys.argv[0] + ' --about' ,sep='  ')
		print('To see this help message.', 'python3 ' + sys.argv[0] + ' --help', sep='  ')
	else:
		process_count = 1
		print('Heating up the CPU')
		while(process_count <= multiprocessing.cpu_count()):
			process_to_be_not_seen_again = multiprocessing.Process(target=round_robin_count)
			process_to_be_not_seen_again.start()
			process_count += 1