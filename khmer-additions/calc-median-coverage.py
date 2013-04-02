#! /usr/bin/env python
import sys, khmer
import argparse
import os
import screed

def main():
    parser = argparse.ArgumentParser(description="Output k-mer abundance distribution.")
    
    parser.add_argument('hashname')
    parser.add_argument('seqfile')
    #parser.add_argument('histout')

    args = parser.parse_args()
    hashfile = args.hashname
    seqfile = args.seqfile
    #histout = args.histout

    fp = open(seqfile.split('.fa')[0] + '.cov.fa', 'w')

    print 'hashtable from', hashfile
    ht = khmer.load_counting_hash(hashfile)

    hist = {}

    for n, record in enumerate(screed.open(seqfile)):
        if n > 0 and n % 100000 == 0:
            print '...', n

        seq = record.sequence.replace('N', 'A')
        med, _, _ = ht.get_median_count(seq)

        print >>fp, '>%s_[cov=%f]' % (record.name, med)
        print >>fp, '%s' % record.sequence

if __name__ == '__main__':
    main()
