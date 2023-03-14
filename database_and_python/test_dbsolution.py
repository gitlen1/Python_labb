import unittest
import json
import os
from pathlib import Path  # Added to use Path instead of string path
from database_and_python.dbsolution import ObjectStore

class TestObjectStore(unittest.TestCase):

    def setUp(self):
        self.file_path = "test.json"
        self.object_store = ObjectStore(self.file_path)

    def tearDown(self):
        if Path(self.file_path).exists():
            os.remove(self.file_path)

    def test_AddRecord(self):
        key = 'test_key'
        value = 'test_value'
        self.object_store.AddRecord(key, value)
        self.assertEqual(self.object_store.__records[key], value)

    
    def test_AddDict(self):
        dict_data = {'test_key': 'test_value'}
        self.object_store.AddDict(dict_data)
        self.assertEqual(self.object_store.__records, dict_data)


    def test_searchValue_found(self):
        dict_data = {'test_key': 'test_value'}
        self.object_store.AddDict(dict_data)
        result = self.object_store.searchValue('test_key')
        self.assertEqual(result, 'test_value')

    
    def test_searchValue_not_found(self):
        dict_data = {'test_key': 'test_value'}
        self.object_store.AddDict(dict_data)
        result = self.object_store.searchValue('non_existent_key')
        self.assertIsNone(result)


    def test_viewSavedRecords(self):
        dict_data = {'test_key': 'test_value'}
        self.object_store.AddDict(dict_data)
        self.assertEqual(self.object_store.viewSavedRecords(), dict_data)

        
    def test_saveDataToFile(self):
        dict_data = {'test_key': 'test_value'}
        self.object_store.AddDict(dict_data)
        self.object_store.saveDataToFile()
        with open(self.file_path, "r") as f:
            self.assertEqual(json.load(f), dict_data)

    
    def test_saveDataToFile_modified(self):
        dict_data = {'test_key': 'test_value', 'new_key': 'new_val'}
        self.object_store.AddDict(dict_data)
        self.object_store.saveDataToFile()
        with open(self.file_path, "r") as f:
            self.assertEqual(json.load(f), dict_data)

    
    def test_saveDataToFile_empty_records(self):
        dict_data = {}
        self.object_store.AddDict(dict_data)
        self.object_store.saveDataToFile() 
        with open(self.file_path, "r") as f:
            self.assertEqual(json.load(f), dict_data)

            
    def test_saveDataToFile_already_exists(self):
        dict_data = {'test_key': 'test_value'}
        self.object_store.AddDict(dict_data)
        self.object_store.saveDataToFile()
        with self.assertRaises(FileExistsError):   # uses context manager to catch raised exception
            self.object_store.saveDataToFile()

    
    def test_deleteRecord(self):
        dict_data = {'test_key': 'test_value', 'new_key': 'new_val', 'last_key' : 'last_val'}
        self.object_store.AddDict(dict_data)
        del_key = 'new_key'
        self.object_store.deleteRecord(del_key)
        self.assertNotIn(del_key, self.object_store.__records.keys())
        
        
    def test_deleteNonExistingRecord(self):
        dict_data = {'test_key': 'test_value', 'new_key': 'new_val', 'last_key' : 'last_val'}
        self.object_store.AddDict(dict_data)
        del_key = 'non_existing_key'
        with self.assertRaises(KeyError):  # uses context manager to catch raised exception
            self.object_store.deleteRecord(del_key)
       
  
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # argv set so jupyter notebook doesn't throw errors