# sentence2tags
Given a sentence predict lemma, morphological tags, pos-tag for each word.

This repo is a modification of the [COMBO](https://github.com/360er0/COMBO) architecture.

## Instructions

* To get the data (from https://github.com/UniversalDependencies)
```commandline
# Armenian data
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Armenian-ArmTDP/master/hy_armtdp-ud-train.conllu -P datasets
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Armenian-ArmTDP/master/hy_armtdp-ud-dev.conllu -P datasets
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Armenian-ArmTDP/master/hy_armtdp-ud-test.conllu -P datasets


# Russian data
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Russian-SynTagRus/master/ru_syntagrus-ud-train.conllu -P datasets
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Russian-SynTagRus/master/ru_syntagrus-ud-dev.conllu -P datasets
wget https://raw.githubusercontent.com/UniversalDependencies/UD_Russian-SynTagRus/master/ru_syntagrus-ud-test.conllu -P datasets
```

* To train the model
```commandline
PYTHONHASHSEED=0 python -m sentence2tags.main --mode autotrain 
        --train datasets/ru_syntagrus-ud-train.conllu --valid datasets/ru_syntagrus-ud-dev.conllu 
        --embed datasets/ru.vec --model ru.pkl --force_trees 
        --targets lemma upostag feats --loss_weights 0.2 0.2 0.8
```

* To make predictions
```commandline
PYTHONHASHSEED=0 python -m sentence2tags.main --mode predict 
        --test test_data.conllu --pred output_path.conllu --model ru.pkl
```
