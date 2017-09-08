#!/usr/bin/env python3
import wget
import zipfile
import pandas as pd
import os
from pdb import set_trace as bp
#
def dclean(dfiles):
    for i, ival in enumerate(dfiles):
        try:
            os.remove(ival)
        except OSError:
            pass
    return
#
zipfilename = 'occupancy_data.zip'
dfiles = ['datatest2.txt', 'datatest.txt', 'datatraining.txt']
dfiles.append(zipfilename)
dclean(dfiles)
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00357/'+zipfilename
filename = wget.download(url)
zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall('./')
zip_ref.close()
df = pd.read_csv('datatraining.txt')
directory = 'asset/data'
if not os.path.exists(directory):
    os.makedirs(directory)
df['time'] = df.index
df[['time','Temperature','Humidity']].to_csv(directory+'/sample.csv', index=False)
import train
if os.path.exists('asset'):
        os.remove('asset')
dclean(dfiles)
