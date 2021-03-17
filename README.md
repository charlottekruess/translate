To test the script and create an output .json file from the LocalizationTemplate_English for English run:

    python3 translate.py --file-name LocalizationTemplate_English.csv --target-language english --lang-tags "en-us, en-gb"

To create an output .json for Danish from the the LocalizationTemplate_Dansk run:

    python3 translate.py --file-name LocalizationTemplate_Dansk.csv --target-language danish --lang-tags "da"

By default the directory where the .csv are stored is set to **templates/** and the output .json file is written to **res/target_language.json**, unless the data-dir and res-dir are specified otherwise:

Optional arguments:
  - --data-dir -> path to directory that contains the csv files
  - --file-name -> name of the csv file to use
  - --res-dir -> path to the directory the json files will be written to
  - --target-language -> specify the language that is used in the Target Language column
  - --lang-tags -> specify the tags for the target language
  - --sys-version -> specify the system version

Requirements:
- see requirements.txt
