# Algorithm Whiteboard Resources

<a href="https://www.youtube.com/watch?v=wWNMST6t1TA&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb">
    <img src="images/logo.png">
</a>

This is where we share notebooks and projects used in our [youtube channel](https://www.youtube.com/watch?v=wWNMST6t1TA&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb).

<a href="https://www.youtube.com/watch?v=vWStcJDuOUk&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb">
    <img src="images/vid-1.jpg" width=170 align="right">
</a>

## Video 1: [DIET Architecture - How it Works](https://www.youtube.com/watch?v=vWStcJDuOUk&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb)

This video explains the parts of the DIET architecture. It does not discuss any code.

<a href="https://www.youtube.com/watch?v=KUGGuJ0aTL8&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb">
    <img src="images/vid-2.jpg" width=170 align="right">
</a>

## Video 2: [DIET Architecture - Design Decisions](https://www.youtube.com/watch?v=KUGGuJ0aTL8&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb)

This video explains the parts of the DIET architecture. It does not discuss any code.

<a href="https://www.youtube.com/watch?v=oj5oPGDlep4&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb">
    <img src="images/vid-3.jpg" width=170 align="right">
</a>

## Video 3: [DIET Architecture - Benchmarks](https://www.youtube.com/watch?v=oj5oPGDlep4&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb)

In this video we make changes to a configuration file. The configuration files, the streamlit application as well as an instructions manual can be found in the `diet` folder.

<a href="https://www.youtube.com/watch?v=mWvnlVw_LiY&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb">
    <img src="images/vid-4.jpg" width=170 align="right">
</a>

## Video 4: [Word Embeddings - Letter Embeddings](https://www.youtube.com/watch?v=mWvnlVw_LiY&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb)

In this video we demonstrate how to train letter embeddings in order to gain intuition on what word embeddings are. 

The kaggle dataset that we use in this video can be found [here](https://www.kaggle.com/therohk/million-headlines).

We've added the two notebooks in this repo in the `letter-embeddings` folder. But you can also run them yourself in google colab. The notebooks are mostly identical but the `v1` notebook only uses one token to predict the next one while `v2` uses two tokens to predict the next one.

Notebook with one token input:  <a href="https://colab.research.google.com/drive/1jbjQtu5d1E88uM8oaJ3BAfHcI7JVUdu2"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

Notebook with two token input: <a href="https://colab.research.google.com/drive/1N5wv75vbFRF3lPO1ZpSddBeb_DRaBNOY"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

<a href="https://www.youtube.com/watch?v=BWaHLmG1lak&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb&index=6">
    <img src="images/vid-5.jpg" width=170 align="right">
</a>


## Video 5: [Word Embeddings - CBOW & SkipGram](https://www.youtube.com/watch?v=BWaHLmG1lak&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb&index=6)


This video explains two algorithms but it does not discuss any code.

<br>

<a href="https://www.youtube.com/watch?v=BWaHLmG1lak&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb&index=6">
    <img src="images/vid-6.jpg" width=170 align="right">
</a>

## Video 6: [Word Embeddings - GloVe](https://www.youtube.com/watch?v=BWaHLmG1lak&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb&index=7)

This video discusses GloVe but also offers code to train a variant of your own. The keras model can be found in the `glove` folder.
The `glove.py` file contains just the keras algorithm while the notebook contains the full code. You can also go online to colab 
and play with the full notebook from there.

The full notebook: <a href="https://colab.research.google.com/drive/1iwzxOmprqJXbzhtBhXrbzvLFX3PoFxvj"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

<a href="https://www.youtube.com/watch?v=FwkwC7IJWO0&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb&index=9">
    <img src="images/vid-7.jpg" width=170 align="right">
</a>

## Video 7: [Word Embeddings - WhatLies](https://www.youtube.com/watch?v=FwkwC7IJWO0&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb&index=9)

This video discusses a small visualisation package we've open sourced. The documentation for it can be found [here](https://rasahq.github.io/whatlies/).

The notebook that we made in this video can be found in the `diet` folder.


<!-- #### Video X: Conditional Random Fields [video not released yet]

The entire project was too big to add here so we've created a seperate github repo which can be found [here](https://github.com/RasaHQ/crf-demo).

The main file that we've changed, the `config.yml` file, can be found in the `crf` folder of this repo as well. There may be some online material that might help you appreciate some details. 

- The [implementation of CRF in Rasa](https://github.com/RasaHQ/rasa/blob/master/rasa/nlu/extractors/crf_entity_extractor.py#L44) directly in github.
- Extra [maths](https://timvieira.github.io/blog/post/2015/04/29/multiclass-logistic-regression-and-conditional-random-fields-are-the-same-thing/) that details the similarity between CRFs and Logistic Regression
 -->
