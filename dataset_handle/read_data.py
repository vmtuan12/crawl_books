import pandas as pd
import re
import ast
import os
from datetime import datetime
from pipeline import pipeline, topic
import json

class BookCsvReader:
    special_chars_set = {'+', '-', '=', '&', '|', '|', '>', '<', '!', '(', ')', '{', '}', '[', ']', '^', '"', '~', '*', '?', ':', '\\', '/', ',', '.'}
    list_regex = r"^[[].*[]]$"
    date_regex = r"(\d{1,2})\/(\d{1,2})\/(\d{4})"
    year_regex = r"\d{4}"
    number_regex = r"\d+(,\d+)*"
    kafka_connector = pipeline.KafkaConnector()

    def read_and_save_data(self, path_to_files='dataset_handle/raw_data'):
        for file in os.listdir(path_to_files):
            print(file)
            data = pd.read_csv(path_to_files + "/" + file)
            data.rename(columns= {'Name': 'Title', 'pagesNumber': 'Pages', 'CountsOfReview': 'ReviewCounts', 'PagesNumber': 'Pages', 'Authors': 'Author'}, inplace= True)
            data = data[['Title', 'Author', 'Description', 'Pages', 'PublishYear', 'Language', 'Rating', 
                        'Genres', 'ReviewCounts', 'isBestSeller', 'isEditorsPick', 'isGoodReadsChoice']]

            for index, row in data.iterrows():
                if pd.isna(row["Title"]):
                    continue
                
                msg = self._make_msg(row)
                self.kafka_connector.send(msg=msg)
                print(msg)
                print("------------------------------------------------------------------------------------")
    
    def _make_msg(self, row) -> dict:
        return {
            "id": self._make_document_id(row["Title"]),
            "title": self._check_str(row["Title"]),
            "author": self._handle_str_to_list(row["Author"]),
            "description": self._convert_html_to_text(row["Description"]),
            "pages": self._get_number(row["Pages"]),
            "publish_year": self._str_to_year(row["PublishYear"]),
            "language": self._check_str(row["Language"]),
            "rating": self._str_to_float(row["Rating"]),
            "genres": self._handle_str_to_list(row["Genres"]),
            "review_counts": self._str_to_int(row["ReviewCounts"]),
            "is_best_seller": self._str_to_bool(row["isBestSeller"]),
            "is_editors_pick": self._str_to_bool(row["isEditorsPick"]),
            "is_goodreads_choice": self._str_to_bool(row["isGoodReadsChoice"]),
        }
    
    def _make_document_id(self, name: str) -> str:
        stripped_name = name.strip()
        result = ''

        for char in stripped_name:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            elif char == ' ':
                if len(result) > 0 and result[len(result) - 1] != '-':
                    result += '-'
            else:
                if char not in self.special_chars_set:
                    result += char

        return result.strip()
    
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
            return string.split(',')
    
    def _str_to_int(self, string) -> int | None:
        if pd.isna(string):
            return None
        
        result = int(string)
        if result == 0:
            return None

        return result
        
    def _str_to_float(self, string) -> float | None:
        if pd.isna(string):
            return None
        
        result = float(string)
        if result == 0:
            return None
        
        return result
        
    def _str_to_bool(self, string) -> bool | None:
        if isinstance(string, bool):
            return string
        
        if pd.isna(string):
            return None
        
        return True if (str.lower(string.strip()) == "true") else False
        
    def _str_to_year(self, string) -> int | None:

        if isinstance(string, int):
            return string

        if pd.isna(string):
            return None
        
        match = re.search(self.year_regex, string)
        return int(match.group()) if match != None else None
        
    def _check_str(self, string) -> bool | None:
        if pd.isna(string):
            return None
        
        return string
    
    def _get_number(self, string) -> int | None:
        if pd.isna(string):
            return None
        
        match = re.search(self.number_regex, string)
        result = int(match.group().replace(',', '')) if match != None else None

        if result == 0:
            return None
        
        return result