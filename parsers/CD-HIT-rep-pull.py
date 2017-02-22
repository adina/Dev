#!/usr/bin/env python

# Author: Youri Lammers
# Contact: youri.lammers@naturalis.nl / youri.lammers@gmail.com

# Filter the cluster output from CD-hit based on
# the minimum number of sequences per cluster

# command: CD-hit_filter.py -f [cluster .fasta file] -c [.clstr cluster file] -m [min # seqs per cluster]

# the output of the CD-hit_filter.py script is a fasta file [input cluster .fasta file with the min # seqs in the file name]
# with the OTU sequences for the clusters with more than or equal number of sequences to the user specified minimum.

# import modules used by the script
import argparse, os, itertools

# set argument parser
parser = argparse.ArgumentParser(description = 'Filter the output from CD-hit based on the minimum number of read per cluster.\nThe filtered output fasta file produced has the same name as the input file with  _min_[minimum size from -c argument].fasta attachted to the name.')

parser.add_argument('-f', '--fasta', metavar='.fasta file', dest='fasta', type=str,
			help='The .fasta file containing the clusters produced by CD-hit.')
parser.add_argument('-c', '--cluster', metavar='.clstr file', dest='cluster', type=str,
			help='The .clstr file producec by CD-hit that contains the cluster information.')
parser.add_argument('-m', '--minimum', metavar='minimum size', dest='minimum', type=int,
			help='The minimum cluster size.')
parser.add_argument('-d', '--descr', metavar='description file', dest='desc', type=str, help='The description file')
args = parser.parse_args()

def read_clstr():

	# parse through the .clstr file and create a dictionary
	# with the sequences per cluster

	# open the cluster file and set the output dictionary
	cluster_file, cluster_dic = open(args.cluster), {}

	# parse through the cluster file and store the cluster name + sequences in the dictionary
	cluster_groups = (x[1] for x in itertools.groupby(cluster_file, key=lambda line: line[0] == '>'))
	for cluster in cluster_groups:
		name = cluster.next().strip()
		print name[1:], 
		for seq in cluster_groups.next():
			if seq.split('>')[1].rstrip().split('...')[1][-1] == "*":
				print '\t' +  seq.split('>')[1].rstrip().split('...')[0]
		#seqs = [seq.split('>')[1].split('...')[0] for seq in cluster_groups.next()]
		#print seqs

	# return the cluster dictionary
	return cluster_dic


def main():


	# obtain a dictionary with the clusters and sequences
	cluster_dic = read_clstr()

if __name__ == '__main__':
	main()
