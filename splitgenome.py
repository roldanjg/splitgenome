import gzip
import time
import datetime

print(datetime.datetime.now().time())
def append_chrfile(line):
    elements_in_line = line.split('\t')
    chr = elements_in_line[0]
    met_count = True if elements_in_line[3] != '0' else False
    unmet_count = True if elements_in_line[4] != '0' else False # ask jose about if it is necessary
    if met_count or unmet_count:
        with open('chr' + chr + '_coveragemet.tsv', 'a+') as chrfile:
            chrfile.write(line)



with gzip.open('contextgenome.gz', 'rt') as f:
    for line in f:
        append_chrfile(line)
print(datetime.datetime.now().time())

