#!/usr/bin/env python 
import sys
import getopt
import os.path
import re


def help():
    print "Usage: %s -i <input_file>\n\n\t-h prints this message\n\t-i specifies input file" % sys.argv[0]

def words_count(input_file):
    ""

    f = open(input_file,"r") 

    words = {}

    for line in f.readlines():
        line_words = line.split()
        for word in line_words:
            word = word.strip("\";:,.!").lower()
            if word not in words.keys():
                words[word] = 1
            else:
                words[word] += 1

    f.close()

    return words

def top_words(words_stats, top_n):
    topw = words_stats.keys()

    topw = sorted(topw, key=words_stats.__getitem__, reverse = True)

    for i in xrange(0,top_n):
        print topw[i], ":\t", words_stats[topw[i]]

def main(argv):
    ""
    input_file = ""

    try:
        opts,args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError as err:
        print str(err)
        help()
        sys.exit(2)

    for opt,arg in opts:
        if opt in ("-h"):
            help()
        elif opt in ("-i"):
            input_file = arg
        else:
            help()
            
    if os.path.isfile(input_file):
        stats = words_count(input_file)
    else:
        print "File %s doesn't exist" % input_file
        sys.exit(3)

    top_words(stats,10)

    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])
