import json

class ObjectStore:
    """
    A class that allows to store and fetch data from a file in json format
    """

    __file_path = ""
    __records = {}

    def __init__(self, file_path):
        """
        Initialize the file path and fetch data from the file
        """
        self.__file_path = file_path
        self._fetchAllData()

    def _fetchAllData(self):
        """
        Fetch saved data from a file in json format and updates
        the records
        """
        saved_data = {}

        db_file = open(self.__file_path)
        for record in db_file:
            saved_data.update(json.loads(record))
        db_file.close()

        self.__records.update(saved_data)
        return self.__records

    def viewSavedRecords(self):
        """
        View the saved records
        """
        print(self.__records)

    
    def AddRecord(self, key, value):
        """
        Add a new record with the given key and value
        """
        self.__records.update({key:value})
        print("Record added")


    def AddDict(self , dict_data):
        """
        Add a dictionary to the records
        """
        self.__records.update(dict_data)
        print("Added successfully")


    def searchValue(self, key):
        """
        Search for a value in the records with the given key
        """
        if key in self.__records:
            print(f"{key}: {self.__records[key]}")
            return self.__records[key]
        else:
            print("Key not found!")
            return None

    def saveDataToFile(self):
        """
        Save records to a file in json format
        """
        jsonData = json.dumps(self.__records)

        db_file = open(self.__file_path, "w")
        db_file.write(jsonData)
        db_file.close()
        print("Data saved to file")