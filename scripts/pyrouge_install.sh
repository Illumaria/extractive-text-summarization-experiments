#!/usr/bin/env bash
git clone https://github.com/bheinzerling/pyrouge
cd pyrouge/
pip install -e .

git clone https://github.com/andersjo/pyrouge.git rouge
pyrouge_set_rouge_path $(pwd)/rouge/tools/ROUGE-1.5.5/

sudo apt-get update && sudo apt-get install libxml-parser-perl
cd rouge/tools/ROUGE-1.5.5/data
rm WordNet-2.0.exc.db
./WordNet-2.0-Exceptions/buildExeptionDB.pl ./WordNet-2.0-Exceptions ./smart_common_words.txt ./WordNet-2.0.exc.db

python -m pyrouge.test