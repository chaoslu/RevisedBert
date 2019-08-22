from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tokenization
import tensorflow as tf
import numpy as np

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("input_file", None,
                    "Input raw text file (or comma-separated list of files).")

flags.DEFINE_string(
    "output_file", None,
    "Output file of text with basic tokenization.")

flags.DEFINE_string("output_vocab_file",None,
	"Output file of vocabulary")



def main(_):
	tokenizer = tokenization.basicTokenizer(do_lower_case=True)
	vocab = {}
	vocab_id = 0
	new_document = []

	input_files = []
	for input_patterns in FLAGS.input_file.split(','):
		input_files.extend(tf.gfile.glob(input_patterns))

	for input_file in input_files:
		with tf.gfile.Gfile(input_file,'r') as reader:
			while True:
				line = tokenization.convert_to_unicode(reader.readlines())
				if not line:
					break
				line.strip()
				if line:
		 	 	 	line = tokenizer.tokenize(line)
			 	 	for token in line:
			 	 		if token not in vocab：
			 	 			vocab[token] = vocab_id
			 	 			vocab_id += 1
			 	 	new_document.append(line)
			 	 else；
			 	 	new_document.append('\n')

		with open(output_file,'w') as writer:
			for line in new_document:
				writer.write(line)
				writer.write('\n')

		

	with open(out_vocab_file,'w') as f:
		f.write("[UNK]\n[CLS]\n[SEP]\n[PAD]\n[MASK]\n")
		for token in vocab:
			f.write(token)
			f.write('\n')

if __name__ == '__main__':
	tf.flags.mark_flags_as_required("input_file")
	tf.flags.mark_flags_as_required("output_file")
	tf.flags.mark_flags_as_required("output_vocab_file")
	tf.app.run()


