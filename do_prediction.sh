#!/bin/bash

GLUE_DIR="glue_data"
STORAGE_BUCKET="gs://my-bert-bucket"
MY_CONFIG_DIR="gs://my-bert-bucket/uncased_L-12_H-768_A-12"

TASK_NAME=("WNLI" "RTE" "MRPC" "CoLA" "SST" "QNLI" "MNLI")
TASK_TRAIN_STEP=("59" "233" "343" "801" "6313" "9819" "36815")



for ((i=0 ; i<=${#TASK_NAME[@]}; i++ )); do
	python3 ./RevisedBert/run_classifier.py \
	  --task_name=$TASK_NAME[i] \
	  --do_predict=true \
	  --data_dir=$GLUE_DIR/$TASK_NAME[i] \
	  --vocab_file=$MY_CONFIG_DIR/vocab.txt \
	  --bert_config_file=$MY_CONFIG_DIR/bert_config.json \
	  --init_checkpoint=$STORAGE_BUCKET/step-139000/$TASK_NAME[i]-output/model.ckpt-$TASK_TRAIN_STEP[i] \
	  --max_seq_length=128 \
	  --train_batch_size=32 \
	  --learning_rate=2e-5 \
	  --num_train_epochs=3.0 \
	  --output_dir=$STORAGE_BUCKET/step-139000/$TASK_NAME[i]-output/ \
	  --use_tpu=True \
	  --tpu_nmae=$TPU_NAME
done

	
