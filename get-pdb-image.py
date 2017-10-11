import urllib2
input_file = open("data/hemoglobin-test.txt")
for i in input_file.read().split('\n'):
    print "processing " + i
    link = "http://www.rcsb.org/pdb/images/%s_bio_r_500.jpg?bioNum=1" % i
    response = urllib2.urlopen(link)
    image = response.read()
    out_file = i + "-500.jpg"
    f = open("data/images/test/hemoglobin/"+out_file,"wb")
    f.write(image)