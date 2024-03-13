import pandas as pd
import re
from pipeline import pipeline, topic

class BookCsvReader:
    
    kafka_connector = pipeline.KafkaConnector()

    def read_and_save_data(self, path_to_files='dataset_handle/raw_data'):
        # for file in os.listdir(path_to_files):
        #     file_name, file_extension = os.path.splitext(file)
        data = pd.read_csv(path_to_files + "/" + "dataset0_0.csv")
        data.drop('isBestSeller', inplace=True, axis=1)
        data.drop('isEditorsPick', inplace=True, axis=1)
        data.drop('isGoodReadsChoice', inplace=True, axis=1)
        data.rename(columns= {'Name': 'Title', 'pagesNumber': 'Pages', 'CountsOfReview': 'ReviewCounts', 'PagesNumber': 'Pages', 'Authors': 'Author'}, inplace= True)
        data = data[['Title', 'Author', 'Description', 'Pages', 'PublishYear', 'Language', 'Rating', 'Genres', 'ReviewCounts']]

        for index, row in data.iterrows():
            print("Row", index+1)
            # for column in data.columns:
            #     value = row[column] if not pd.isna(row[column]) else None
            #     if column == "Description" and value != None:
            #         value = _convert_html_to_text(value)

            #     print(f"{_camel_to_snake(column)}: {value}")
            print("\n")

    def _camel_to_snake(self, camelcase_str: str):
        snakecase_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camelcase_str).lower()
        return snakecase_str

    def _convert_html_to_text(self, html: str) -> str:
        return re.sub(r"<[^>]*>", " ", html)
    
    def _make_msg(row) -> dict:
        return None
