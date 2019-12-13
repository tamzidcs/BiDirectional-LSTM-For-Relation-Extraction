
# Setup Instruction for Bidirectional LSTM model based sentence level relation extraction 


Please follow original github link(https://github.com/UKPLab/emnlp2017-relation-extraction/blob/master/README.md)  for any confusion 
as the setup is same.

# Source for the dataset:

https://www.informatik.tu-darmstadt.de/ukp/research_6/data/lexical_resources/wikipedia_wikidata_relations/

Folder Structure:
```
relation_extraction/
├── core
│   ├── parser.py
│   ├── embeddings.py
│   ├── entity_extraction.py
│   └── keras_models.py
├── stanford_tag_dataset.py
└── evaluation
    └── metrics.py
resources/
├── properties-with-labels.txt
└── property_blacklist.txt
```



### Wikipedia-Wikidata sentence-level relation data set

*  Download the data set from the paper [here](https://www.informatik.tu-darmstadt.de/ukp/research_6/data/lexical_resources/wikipedia_wikidata_relations/). See the data set ReadMe for more information on the format and see the [paper](http://aclweb.org/anthology/D17-1188) on data set construction.

# Setup:

1. Setup a new pip environment first: http://docs.python-guide.org/en/latest/dev/virtualenvs/

2. Check out the repository and run:

	pip3 install -r requirements.txt

3. Set the Keras (deep learning library) backend to TensorFlow with the following command:
```
export KERAS_BACKEND=tensorflow
```

4. Download the data from :				    
https://www.informatik.tu-darmstadt.de/ukp/research_6/data/lexical_resources/wikipedia_wikidata_relations/

Extract the archive inside emnlp2017-relation-extraction/data/wikipedia-wikidata/

The data was preprocessed using Stanford Core NLP 3.7.0 models. See stanford_tag_dataset.py for more information.
	
	

5. Download the GloVe embeddings, glove.6B.zip (https://nlp.stanford.edu/projects/glove/) and 	
   put them into the folder emnlp2017-relation-extraction/resources/glove/. 	
	
   You can change the path to word embeddings in the model_params.json file if needed.


Complete the setup above

Run python model_train.py in `/relation_extraction/` to see the list of parameters

# Training:

Our Implementation(Bidirectional LSTM model)

If you put the data into the default folders you can train the BidirectionalLSTM model with the following command for

training (From relation_extraction folder):

```
python model_train.py model_BidirectionalLSTM train ../data/wikipedia-wikidata/enwiki-20160501/semantic-graphs-filtered-training.02_06.json ../data/wikipedia-wikidata/enwiki-20160501/semantic-graphs-filtered-validation.02_06.json

```

# Run the following command to compute the precision-recall curves:


```
python precision_recall_curves.py model_BidirectionalLSTM ../data/wikipedia-wikidata/enwiki-20160501/semantic-graphs-filtered-held-out.02_06.json

```

# You can also want to try the Context Weighted Model Similarly run:

Training:

```
python model_train.py model_ContextWeighted train ../data/wikipedia-wikidata/enwiki-20160501/semantic-graphs-filtered-training.02_06.json ../data/wikipedia-wikidata/enwiki-20160501/semantic-graphs-filtered-validation.02_06.json

```
For precision-recall curve:

```
python precision_recall_curves.py model_ContextWeighted ../data/wikipedia-wikidata/enwiki-20160501/semantic-graphs-filtered-held-out.02_06.json

```

# Requirements:
	Python 3.6
	Keras 2.1.5
	TensorFlow 1.6.0
