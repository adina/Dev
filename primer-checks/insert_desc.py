#!/usr/bin/python

import sys

if len(sys.argv) != 4:
	print "USAGE: insert_desc.py <desc_file> <in_blast> <out_blast>"
	sys.exit(1)

descriptions = dict()
for line in open(sys.argv[1]):
	lexemes = line.strip().split('\t')
	descriptions[lexemes[0]] = lexemes[1]

out = open(sys.argv[3], "w")
for line in open(sys.argv[2]):
	lexemes = line.strip().split("\t")
	lexemes.insert(2, descriptions[lexemes[0]])
	out.write("%s\n" % ("\t".join(lexemes)))
