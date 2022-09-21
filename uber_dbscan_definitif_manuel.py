#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install numpy


# In[2]:


conda install -c intel mkl


# In[3]:


pip install -U numpy


# In[3]:


import pandas as pd 
import numpy as np 

from sklearn.preprocessing import  OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.cluster import DBSCAN


import plotly.express as px
import plotly.io as pio
pio.renderers.default = "iframe_connected"
from IPython.display import HTML, Image


# In[4]:


df_apr = pd.read_csv('uber-raw-data-apr14.csv')


# In[5]:


df_may = pd.read_csv('uber-raw-data-may14.csv')


# In[6]:


df_jun = pd.read_csv('uber-raw-data-jun14.csv')


# In[7]:


df_jul = pd.read_csv('uber-raw-data-jul14.csv')


# In[8]:


df_aug = pd.read_csv('uber-raw-data-aug14.csv')


# In[9]:


df_sep = pd.read_csv('uber-raw-data-sep14.csv')


# In[10]:


df_def = pd.concat([df_apr, df_aug, df_jul, df_jun, df_may, df_sep])


# In[11]:


df_def.columns = [x.lower().replace('/', '_') for x in df_def.columns]


# In[12]:


df_def.date_time = pd.to_datetime(df_def['date_time'])


# In[13]:


new_dates, new_times = zip(*[(d.date(), d.time()) for d in df_def['date_time']])
df_def = df_def.assign(new_date=new_dates, new_time=new_times)
df_def['hour'] = df_def.date_time.dt.hour
df_def['day'] = df_def.date_time.dt.dayofweek


# In[14]:


df_def = df_def.drop(columns=["date_time"])


# In[15]:


len(df_def)


# DROP OUTLIERS

# In[16]:


for i in ['lat', 'lon',]:
    df_def = df_def[~(np.abs(df_def[i]-df_def[i].mean()) > (3*df_def[i].std()))]


# In[17]:


len(df_def)


# VISUALISATION DES LUNDI TOUTES LES HEURES.

# In[16]:


df_j1 = df_def[(df_def.day == 0) & (df_def.hour <=23)]


# In[17]:


df_j1 = df_j1.drop(columns=['base', 'new_date', 'new_time'])


# In[18]:


df_j1.head()


# In[19]:


numeric_features = [0, 1, 2, 3] # Positions des colonnes quantitatives dans X
numeric_transformer = StandardScaler()

# On combine les transformers dans un ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        
    ])


# In[20]:


X_j1 = preprocessor.fit_transform(df_j1) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j1)
np.unique(db.labels_)
df_j1["cluster"] = db.labels_


# In[21]:


fig = px.scatter_mapbox(df_j1[(df_j1.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "lundi_trafic_by_hour"
)
fig.show()


# VISUALITION MARDI TOUTES LES HEURES

# In[22]:


df_j2 = df_def[(df_def.day == 1) & (df_def.hour <=23)]


# In[23]:


df_j2 = df_j2.drop(columns=['base', 'new_date', 'new_time'])


# In[24]:


df_j2.head()


# In[25]:


numeric_features = [0, 1, 2, 3] # Positions des colonnes quantitatives dans X
numeric_transformer = StandardScaler()

# On combine les transformers dans un ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        
    ])


# In[26]:


X_j2 = preprocessor.fit_transform(df_j2) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j2)
np.unique(db.labels_)
df_j2["cluster"] = db.labels_


# In[27]:


fig = px.scatter_mapbox(df_j2[(df_j2.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "mardi_trafic_by_hour"

)
fig.show()


# VISUALITION MERCREDI TOUTES LES HEURES

# In[23]:


df_j3 = df_def[(df_def.day == 2) & (df_def.hour <=23)].drop(columns=['base', 'new_date', 'new_time'])


# In[24]:


numeric_features = [0, 1, 2, 3] # Positions des colonnes quantitatives dans X
numeric_transformer = StandardScaler()

# On combine les transformers dans un ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        
    ])


# In[25]:


X_j3 = preprocessor.fit_transform(df_j3) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j3)
np.unique(db.labels_)
df_j3["cluster"] = db.labels_


# In[26]:


fig = px.scatter_mapbox(df_j3[(df_j3.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "mercredi_trafic_by_hour"

)
fig.show()


# JEUDI

# In[ ]:


df_j4 = df_def[(df_def.day == 3) & (df_def.hour <=23)].drop(columns=['base', 'new_date', 'new_time'])


# In[ ]:


X_j4 = preprocessor.fit_transform(df_j4) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j4)
np.unique(db.labels_)
df_j4["cluster"] = db.labels_


# In[ ]:


fig = px.scatter_mapbox(df_j4[(df_j4.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "jeudi_trafic_by_hour"

)
fig.show()


# VENDREDI

# In[ ]:


df_j5 = df_def[(df_def.day == 4) & (df_def.hour <=23)].drop(columns=['base', 'new_date', 'new_time'])


# In[ ]:


X_j5 = preprocessor.fit_transform(df_j5) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j5)
np.unique(db.labels_)
df_j5["cluster"] = db.labels_


# In[ ]:


fig = px.scatter_mapbox(df_j5[(df_j5.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "vendredi_trafic_by_hour"

)
fig.show()


# SAMEDI

# In[18]:


df_j6 = df_def[(df_def.day == 5) & (df_def.hour <=23)].drop(columns=['base', 'new_date', 'new_time'])


# In[21]:


X_j6 = preprocessor.fit_transform(df_j6) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j6)
np.unique(db.labels_)
df_j6["cluster"] = db.labels_


# In[22]:


fig = px.scatter_mapbox(df_j6[(df_j6.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "samedi_trafic_by_hour"

)
fig.show()


# DIMANCHE

# In[ ]:


df_j7 = df_def[(df_def.day == 6) & (df_def.hour <=23)].drop(columns=['base', 'new_date', 'new_time'])


# In[ ]:


X_j7 = preprocessor.fit_transform(df_j7) # fit_transform !!

db = DBSCAN(eps=0.2, min_samples=100, algorithm="brute")

db.fit(X_j7)
np.unique(db.labels_)
df_j7["cluster"] = db.labels_


# In[ ]:


fig = px.scatter_mapbox(df_j7[(df_j7.cluster >=0)], 
        lat="lat", 
        lon="lon",
        hover_name = 'hour',                
        color="cluster",
        mapbox_style="carto-positron",
        animation_frame="hour",
        title = "dimanche_trafic_by_hour"

)
fig.show()


# In[ ]:




