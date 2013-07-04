### 1.1 BIN INSTALLATION
bin:
	cd ../bin; make

SEED=1  # Random seed
BIN=../bin/
DATA=train.trc.tok.gz # wc = 39595781 491195991 3592903739
LIMIT=100000


### 2.2 SRILM options:/matl
LM_NGRAM=4# n-gram order
LM_VOCAB=50 # words seen less than this in GETTRAIN will be replaced with <unk>
LM_MTYPE=i686-m64 # architecture for compiling srilm

train.vocab-all.gz: ${DATA}
	zcat $< | head -n -${LIMIT} | awk 'length($$0) < 1001' | \
	ngram-count -write-order 1 -text - -write - | gzip > $@

train.vocab.gz: train.vocab-all.gz
	zcat $< | awk '{if ($$2 >= ${LM_VOCAB}) print $$1}' | gzip > $@
	zcat $@ | wc -l

train.lm.gz: train.tok.gz train.vocab.gz
	zcat $< | awk 'length($$0) < 1001' | \
	ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab train.vocab.gz -text - -lm $@

%.ppl.gz:
	#test.ppl.gz trial.ppl.gz
	zcat $*.tok.gz | ngram -order ${LM_NGRAM} \
	-unk -lm ukwac.lm.gz -ppl - -debug 2 | gzip > $@

%.ngram.gz: %.tab
	cat $< | cut -f1 | sed "s/’//g" | tr -d '[:punct:]' | \
	tr '[:upper:]' '[:lower:]' | gzip > $@

%.index.gz: %.tab
	cat $< | cut -f2 | gzip > $@

%.root.gz: %.tab
	cat $< | cut -f3 | gzip > $@

%.pos.gz: %.tab
	cat $< | cut -f4 | gzip > $@

%.ans.gz: %.tab
	cat $< | cut -f5 | gzip > $@

%.context: %.ngram.gz extract-context.py 
	zcat $< | ./extract-context.py $* > $@

.INTERMEDIATE: train.ngram.gz train.index.gz train.root.gz train.pos.gz train.ans.gz train.context
%.all: %.tab %.ngram.gz %.index.gz %.root.gz %.pos.gz %.ans.gz %.context
	echo "done"


%.clean:
	rm -rf $*.ngram.gz $*.root.gz $*.pos.gz $*.ans.gz $*.index.gz $*.context.gz
