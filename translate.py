import pandas as pd
import json
from datetime import datetime
import argparse
import json
import csv
import numpy as np

ap = argparse.ArgumentParser()

ap.add_argument("--data-dir", type=str, default="templates/", help="path to directory that contains the csv files")
ap.add_argument("--file-name", type=str, default="LocalizationTemplate_English.csv", help="name of the csv file")
ap.add_argument("--target-language", type=str, default="english", help="target language to be translated")
ap.add_argument("--lang-tags", type=str, default="en-us,en-gb", help="tag(s) for the language to be translated")
ap.add_argument("--sys-version", type=str, default="1", help="number of the system versio")
ap.add_argument("--res-dir", type=str, default="res/", help="path to the directory the log files will be written to")

args = ap.parse_args()

if __name__ == '__main__':

    data_dir, res_dir = args.data_dir, args.res_dir
    file_name = args.file_name
    language, tags = args.target_language, args.lang_tags.split(',')
    sys_version = args.sys_version

    print("args values used: ", data_dir, res_dir, file_name, language, tags, sys_version)

    csv_df = pd.read_csv(data_dir + file_name, sep=";|,", engine ='python')
    print("csv read from input ")
    print(csv_df)
    print("columns", csv_df.columns.to_list())

    value_df = csv_df[csv_df['Token'].notna()]

    token_df = value_df[['Token', 'Target Language']]
    token_df.columns = ['Token', 'TargetLanguage']
    print("token dataframe")
    print(token_df)
    replace_df = token_df.replace(np.nan, '', regex=True)

    dict = dict(zip(replace_df.Token, replace_df.TargetLanguage))
    #print("map token to target language")
    #print(dict)

    json_target = json.dumps(dict, allow_nan=True)

    sys = value_df['System'].values[0]
    date = '{:%Y-%m-%d}'.format(datetime.now())

    json_header = {
            "system": sys,
            "systemVersion": sys_version,
            "language": language,
            "language_tags": tags,
            "date": date
    }

    json_output = json_header | dict
    print("json output ")
    print(json_output)

    with open('{}/{}_target.json'.format(res_dir, language), 'w') as json_file:
        json.dump(json_output, json_file)
