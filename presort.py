#!/usr/bin/env python2.7
# presorter for python ANAGRAM finder
# Alex Eames RasPi.TV I wrote this in 2012 when I was first learning Python

# This program works with the scrabble/words with friends word list wordlist.txt
# The file is modified so each line contains an alphabetically sorted version of  
# each word, then the word itself. e.g. abeprrrsy, raspberry 
# and stored as /home/pi/sortedwordlist.txt

# The whole file (line order) is then alphabetically sorted and stored as  
# (/home/pi/sortedwordlist2.txt) 
# It's a bit of a hack, but makes for much more efficient anagram searching.

import time
start_time = time.time()
print "Starting now..."

# Open the word list file and read it into a Python list
results = list(open("/home/pi/wordlist.txt", "r"))
clean_lines = [x.strip() for x in results] # takes out the /n line ends

results = clean_lines

target = open("/home/pi/sortedwordlist.txt", 'w')

target.truncate() # bin the old file if it exists

for i in range(len(results)):
    unsorted_word = results[i]
    results[i] = sorted(results[i]) 
    sorted_word = ''.join(results[i])  # this is what is written to sortedwordlist.txt
    output = "%s %s\n" % (sorted_word, unsorted_word)     
    target.write(output)               # write results to sortedwordlist.txt
target.close()

# Sort the lines in the file alphabetically
results = list(open("/home/pi/sortedwordlist.txt", "r"))

results = sorted(results)              # alphabetical sort

target = open("/home/pi/sortedwordlist2.txt", 'w')

target.truncate() # bin the old file if it exists

for i in range(len(results)):
    target.write(results[i])
target.close()

end_time = time.time()

elapsed_time = end_time - start_time

print "Finished. That took %.2f seconds" % elapsed_time

#Pre-processing is now done.

#In the actual program, take the inputted letters and sort them alphabetically.
#Then do a findall for each line containing that string, stuffing them into a list

#Then take each of those lines in the list and print the second entry or 
# substitute out the sorted search string and delimiter.


