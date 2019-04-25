MiniBooNE Machine Learning
==============================

Capstone project for SCS3253 UoT Machine Learning Winter 2019
- Problem statement: https://archive.ics.uci.edu/ml/datasets/MiniBooNE+particle+identification

We will be training, optimizing and comparing the out-of-sample performance of two models:
- Neutral network (Multilayer Perceptron) using Keras
- Random Forest using scikit-learn

Checklist
------------
- [x] Data import
- [x] Data exploration
- [X] Feature engineering
- [x] Outlier detection
- [x] Dimensionality reduction
- [X] Complete data cleaning pipeline
- [X] Random Forest Classifier
- [X] Neutral Network Classifier
- [X] Model comparison

Installation
------------
- Clone and go into the repo
```bash
git clone https://github.com/david-siqi-liu/miniboone.git
```
- Create an environment from `environment.yml`
```bash
conda env create -f environment.yml

conda list
```
- Activate environment
```bash
conda activate miniboone
```
- Setup
```bash
python setup.py install
```

Exploration Work
------------
Exploration work is in the `MiniBooneNE` notebook

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
