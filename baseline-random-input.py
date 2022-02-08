import gzip
import random
random.seed(42)

for dataset in 'dev-0', 'test-A':
    with gzip.open(f'{dataset}/in.tsv.gz', 'rt') as f_in, open(f'{dataset}/out.tsv', 'w') as f_out:
        for line in f_in:
            line = line.rstrip('\n').split('\t')
            line = line[1:]
            #line = random.shuffle(line)
            line = '\t'.join(line) + '\n'
            f_out.write(line)