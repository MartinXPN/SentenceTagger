# sentence2tags
Given a sentence predict lemma, morphological tags, pos-tag for each word.

This repo is a modification of the [COMBO](https://github.com/360er0/COMBO) architecture.

## Instructions

* To get the data
```commandline
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Armenian-ArmTDP/master/hy_armtdp-ud-train.conllu -P datasets
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Armenian-ArmTDP/master/hy_armtdp-ud-test.conllu -P datasets
```

* To train the model
```commandline
PYTHONHASHSEED=0 python -m sentence2tags.main --mode autotrain --train datasets/hy_armtdp-ud-train.conllu --valid datasets/hy_armtdp-ud-train.conllu --embed external_embedding.txt --model model_name.pkl --force_trees
```

* To make predictions
```commandline
PYTHONHASHSEED=0 python -m sentence2tags.main --mode predict --test test_data.conllu --pred output_path.conllu --model model_name.pkl
```
