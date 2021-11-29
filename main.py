import pandas as pd
import json
from flask import Flask
from flask import request
app = Flask(__name__)

def group_by_feature(df, feature):
    group = df.groupby(feature).sum()
    
    json_group = group.to_json(orient="columns", indent=4)    
    with open(f'grouped_data_by_{feature}.json', 'w') as outfile:
        json.dump(json_group, outfile)
    
    group.to_csv('data.csv',sep=",",index=False)
    
    return json_group

# def hello_world():
#   return "Hello, World!"

@app.route("/")
def run():
    # page = request.args.get('page', default = 1, type = int)
    filter_by = request.args.get('filter', default = None, type = str)
    
    data = pd.read_csv('https://www.openml.org/data/get_csv/37/dataset_37_diabetes.arff')
    data.to_csv('data.csv',sep=",",index=False)
    
    if filter_by:
        data = data[data['class']==filter_by]
        data.to_csv(f'data_{}.csv',sep=",",index=False)
    
    group = group_by_feature(data, 'class')
    
    return group



