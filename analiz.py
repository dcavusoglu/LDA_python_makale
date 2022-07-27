import pyLDAvis
import pyLDAvis.gensim_models
import matplotlib.pyplot as plt
matplotlib inline

pyLDAvis.enable_notebook()
LDAvis_prepared = pyLDAvis.gensim_models.prepare(model, corpus, dictionary, sort_topics=True)
LDAvis_prepared
