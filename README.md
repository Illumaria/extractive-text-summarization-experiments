# Extractive Text Summarization

A demo project on extractive text summarization.

## Prerequisites

* Python >= 3.7.4
* pip >= 21.0.1
* git >= 2.23.0

## Usage

Prepare the environment:

```bash
git clone https://github.com/Illumaria/extractive-text-summarization-experiments.git
cd extractive-text-summarization-experiments/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


Prepare the data:

```bash
python scripts/download_dataset.py
sh scripts/download_corenlp.sh
sh scripts/pyrouge_install.sh
python src/preprocess.py -mode tokenize -raw_path raw_stories -save_path tokenized
python src/preprocess.py -mode format_to_lines -raw_path tokenized -save_path json_data -n_cpus 1 -use_bert_basic_tokenizer false -map_path urls
python src/preprocess.py -mode format_to_bert -raw_path json_data -save_path bert_data -lower -n_cpus 1 -log_file logs/preprocess.log
```

Train model:

```bash
python src/train.py -task ext -mode train -bert_data_path bert_data -ext_dropout 0.1 -model_path checkpoints -lr 2e-3 -visible_gpus 0 -report_every 50 -save_checkpoint_steps 250 -batch_size 2000 -train_steps 500 -accum_count 2 -log_file logs/ext_bert_cnndm -use_interval true -warmup_steps 100 -max_pos 512
```

Evaluate model:

```bash
python src/train.py -task ext -mode validate -batch_size 2000 -test_batch_size 500 -bert_data_path bert_data -log_file logs/val_ext_bert_cnndm -model_path checkpoints -sep_optim true -use_interval true -visible_gpus 1 -max_pos 512 -max_length 200 -alpha 0.95 -min_length 50 -result_path logs/ext_bert_cnndm
```
