import pandas as pd
import re
import ast
from pipeline import pipeline, topic

class BookCsvReader:
    list_regex = r"^[[].*[]]$"
    kafka_connector = pipeline.KafkaConnector()

    def read_and_save_data(self, path_to_files='dataset_handle/raw_data'):
        # for file in os.listdir(path_to_files):
        #     file_name, file_extension = os.path.splitext(file)
        data = pd.read_csv(path_to_files + "/" + "dataset0_0.csv")
        data.rename(columns= {'Name': 'Title', 'pagesNumber': 'Pages', 'CountsOfReview': 'ReviewCounts', 'PagesNumber': 'Pages', 'Authors': 'Author'}, inplace= True)
        data = data[['Title', 'Author', 'Description', 'Pages', 'PublishYear', 'Language', 'Rating', 
                     'Genres', 'ReviewCounts', 'isBestSeller', 'isEditorsPick', 'isGoodReadsChoice']]

        for index, row in data.iterrows():
            print(self._make_msg(row))
            print("------------------------------------------------------------------------------------")
    
    def _make_msg(self, row) -> dict:
        return {
            "title": self._check_str(row["Title"]),
            "author": self._handle_str_to_list(row["Author"]),
            "description": self._convert_html_to_text(row["Description"]),
            "pages": self._str_to_int(row["Pages"]),
            "publish_year": self._str_to_int(row["PublishYear"]),
            "language": self._check_str(row["Language"]),
            "rating": self._str_to_float(row["Rating"]),
            "genres": self._handle_str_to_list(row["Genres"]),
            "review_counts": self._str_to_int(row["ReviewCounts"]),
            "is_best_seller": self._str_to_bool(row["isBestSeller"]),
            "is_editors_pick": self._str_to_bool(row["isEditorsPick"]),
            "is_goodreads_choice": self._str_to_bool(row["isGoodReadsChoice"]),
        }
    
    def _convert_html_to_text(self, html) -> str | None:
        if pd.isna(html):
            return None
        
        return re.sub(r"<[^>]*>", " ", html)

    def _handle_str_to_list(self, string: str) -> str | list[str]:
        if pd.isna(string):
            return None
        
        if isinstance(string, str) and re.search(self.list_regex, string):
            author_list = ast.literal_eval(string)
            return author_list
        else:
            return [string]
    
    def _str_to_int(self, string) -> int | None:
        if pd.isna(string):
            return None
        
        return int(string)
        
    def _str_to_float(self, string) -> float | None:
        if pd.isna(string):
            return None
        
        return float(string)
        
    def _str_to_bool(self, string) -> bool | None:
        if pd.isna(string):
            return None
        
        return True if (str.lower(string.strip()) == "true") else False
        
    def _check_str(self, string) -> bool | None:
        if pd.isna(string):
            return None
        
        return string