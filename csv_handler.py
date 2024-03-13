from dataset_handle.read_data import BookCsvReader

csv_reader = BookCsvReader()

if __name__ == "__main__":
    csv_reader.read_and_save_data()