

import scipy.io
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

for root, dirs,files in os.walk("C:/Users/Ravi/OneDrive/Documents/postulate proj/0_load",topdown=False):
    for file_names in files:
        path =os.path.join(root,file_names)
        print(path)
        
path = r'C:/Users/Ravi/OneDrive/Documents/postulate proj/0_load/ir.mat'
mat = scipy.io.loadmat(path)
mat.items()
list(mat.keys())
key_name = list(mat.keys())[3]
DE_data = mat.get(key_name)
fault = np.full((len(DE_data), 1), file_names[:-4])
df_temp = pd.DataFrame({'DE_data':np.ravel(DE_data) , 'fault':np.ravel(fault)})
df_temp

plt.figure(figsize=(10,3))
plt.plot(df_temp.iloc[:,0])
plt.show()

df=pd.DataFrame(columns=['DE_data','fault'])

for root, dirs, files in os.walk("C:/Users/Ravi/OneDrive/Documents/postulate proj/0_load", topdown=False):
    for file_name in files:
        path = os.path.join(root, file_name)
        print(path)

        mat = scipy.io.loadmat(path)

        key_name = list(mat.keys())[3]
        DE_data = mat.get(key_name)
        fault = np.full((len(DE_data), 1), file_name[:-4])

        df_temp = pd.DataFrame({'DE_data':np.ravel(DE_data) , 'fault':np.ravel(fault)})
        
        df = pd.concat([df,df_temp],axis=0)
        print(df['fault'].unique())
        
df.to_csv('all_faults.csv',index=False)    

faults = df['fault'].unique()
for  f in faults:
    plt.figure(figsize=(10,3))
    plt.plot(df[df['fault']==f].iloc[:,0])
    plt.title(f)
    plt.show()
    
import seaborn as sns
    
plt.figure(figsize=(15,5))
sns.scatterplot(data=df.iloc[::100,:],y='DE_data',x=np.arange(0,len(df),100),hue='fault')
plt.show()