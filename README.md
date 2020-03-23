# Algorithm Whiteboard Resources

<a href="https://www.youtube.com/watch?v=wWNMST6t1TA&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb">
    <img src="images/logo.png">
</a>

This is where we share notebooks and projects used in our [youtube channel](https://www.youtube.com/watch?v=wWNMST6t1TA&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb).

<a href="https://youtu.be/vWStcJDuOUk">
    <img src="images/vid-1.jpg" width=125 align="right">
</a>

#### Video 1: DIET Architecture - How it Works

This video explains the parts of the DIET architecture. It does not discuss any code.

<a href="https://youtu.be/KUGGuJ0aTL8">
    <img src="images/vid-2.jpg" width=125 align="right">
</a>

#### Video 2: DIET Architecture - Design Decisions

This video explains the parts of the DIET architecture. It does not discuss any code.

<a href="https://youtu.be/oj5oPGDlep4">
    <img src="images/vid-3.jpg" width=125 align="right">
</a>

#### Video 3: DIET Architecture - Benchmarks

In this video we make changes to a configuration file. The configuration files, the streamlit application as well as an instructions manual can be found in the `diet` folder.

<a href="https://youtu.be/mWvnlVw_LiY">
    <img src="images/vid-4.jpg" width=125 align="right">
</a>

#### Video 4: Word Embeddings - Letter Embeddings

In this video we demonstrate how to train letter embeddings in order to gain intuition on what word embeddings are. 

The kaggle dataset that we use in this video can be found [here](https://www.kaggle.com/therohk/million-headlines).

We've added the two notebooks in this repo in the `letter-embeddings` folder. But you can also run them yourself in google colab. The notebooks are mostly identical but the `v1` notebook only uses one token to predict the next one while `v2` uses two tokens to predict the next one.

Notebook with one token input:  <a href="https://colab.research.google.com/drive/1jbjQtu5d1E88uM8oaJ3BAfHcI7JVUdu2"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

Notebook with two token input: <a href="https://colab.research.google.com/drive/1N5wv75vbFRF3lPO1ZpSddBeb_DRaBNOY"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

#### Video X: Conditional Random Fields [video not released yet]

The entire project was too big to add here so we've created a seperate github repo which can be found [here](https://github.com/RasaHQ/crf-demo).

The main file that we've changed, the `config.yml` file, can be found in the `crf` folder of this repo as well. There may be some online material that might help you appreciate some details. 

- The [implementation of CRF in Rasa](https://github.com/RasaHQ/rasa/blob/master/rasa/nlu/extractors/crf_entity_extractor.py#L44) directly in github.
- Extra [maths](https://timvieira.github.io/blog/post/2015/04/29/multiclass-logistic-regression-and-conditional-random-fields-are-the-same-thing/) that details the similarity between CRFs and Logistic Regression
