#!/usr/bin/python

import sys

if len(sys.argv) != 4:
	print "USAGE: insert_desc.py <desc_file> <in_blast> <out_blast>"
	sys.exit(1)

descriptions = dict()
for line in open(sys.argv[1]):
	lexemes = line.strip().split('\t')
	if descriptions.has_key(lexemes[0]):
		descriptions[lexemes[0]].append(lexemes[1])
	else:
		descriptions[lexemes[0]] = [lexemes[1]]


out = open(sys.argv[3], "w")
for line in open(sys.argv[2]):
	lexemes = line.strip().split("\t")
	if descriptions.has_key(lexemes[2]):
		new_info_ini = descriptions[lexemes[2]]
		new_info = ",".join(new_info_ini)
	else:
		new_info = "no_annotation"
	lexemes.insert(2, new_info)
	out.write("%s\n" % ("\t".join(lexemes)))
