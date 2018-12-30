#!/usr/bin/python3

import logging, sys, time 

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
filename, identifier, count, delay = '', '', 0, 0

try:

	filename = sys.argv[1]	
	identifier = sys.argv[2]
	count = int(sys.argv[3])
	delay = int(sys.argv[4])
	
	if (count < 1): 
		logging.error("One iteration is minimum")
		raise ValueError()
		
except (ValueError, IndexError):
	logging.error("Syntax: %i filename identifier count delay-in-ms" % sys.argv[0])
	sys.exit()

with open(filename, 'r') as fd:
		for line in fd:
			line = line.strip()
			logging.info("%s : %s" % (identifier, line))
			count -= 1;
			time.sleep(delay/1000)
			if (count < 1): sys.exit()
			