## readme 

This gist contains the code to repeat the steps in the DIET benchmarking youtube video. You can download all the files by cloning this gist; 

```
git clone git@gist.github.com:81fc9433182ccfb9dece4bb4dbde1f7a.git
```

You'll also need to clone the repository over [here](https://github.com/RasaHQ/rasa-demo) to get the dataset you'll need. You can clone that repository via; 

```
git clone git@github.com:RasaHQ/rasa-demo.git
```

You will also need to ensure that you've installed the bert dependencies if you
want to run the heavy model. 

```
pip install "rasa[transformers]"
```

Once that is done you can repeat everything we've done here by running; 

```
mkdir results
rasa test nlu --config configs/config-orig.yml --cross-validation --runs 1 --folds 2 --out results/config-orig
rasa test nlu --config configs/config-init.yml --cross-validation --runs 1 --folds 2 --out results/config-init
rasa test nlu --config configs/diet-replace.yml --cross-validation --runs 1 --folds 2 --out results/diet-replace
rasa test nlu --config configs/diet-minimum.yml --cross-validation --runs 1 --folds 2 --out results/diet-minimum
rasa test nlu --config configs/diet-heavy.yml --cross-validation --runs 1 --folds 2 --out results/diet-heavy
```

Once done you can use streamlit to see a dasbboard of the results. 

```
pip install streamlit
streamlit run viewresults.py
```

