from pybloomfilter import BloomFilter

bf = BloomFilter(1000, 0.01, 'filter.bloom')

bf.add("apple")
bf.add("pear")
bf.add("apple")

print bf.capacity
print len(bf)
print bf.__len__()

print "apple" in bf
