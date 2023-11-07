# atmt 
"Advanced Techniques of Machine Translation".\
Experiment Summaries

Experiment 1: Hyperparameter Tuning\
In our first experiment, we focused on the fine-tuning of hyperparameters. After various iterations, we decided to adjust two key hyperparameters: the learning rate and the patience parameter.

Modifications: Changes were implemented in train_hyperparameter_tune.py.\
Outcome: These adjustments led to enhanced translation quality on the test set, which can be reviewed in assignments/03/baseline/translations_tune.p.txt.

Experiment 2: Subword Translation using BPE\
For our second experiment, we ventured into translation at the subword level by incorporating Byte Pair Encoding (BPE). Utilizing resources from the subword-nmt GitHub repository, we employed command-line tools to process and generate BPE data, subsequently stored under data/en-fr/bpe.

Modifications: Essential alterations were made to both train.py and dataset.py, we added postprocess.py to deal with bpe data, enabling the scripts to load and handle BPE data effectively.\
Outcome: The integration of BPE test set translations, with results available in assignments/03/baseline/translations_bpe.pp.txt.
