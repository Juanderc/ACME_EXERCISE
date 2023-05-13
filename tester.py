import unittest

# Import the functions and classes you want to test
from ACME import read_file, evaluate_compensation, execute
# from 

class TestScript(unittest.TestCase):

    def test_evaluate_compensation(self):
        file_name_to_write_content = "test_cases/" + "test_employees_compensation.txt"
        
        # Define test input and expected output
        compensation = {
            "MO": {"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
            "TU":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20}, 
            "WE":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
            "TH":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
            "FR":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
            "SA":{"00:01-09:00":30, "09:00-18:00":20, "18:01-00:00":25},
            "SU":{"00:01-09:00":30, "09:00-18:00":20, "18:01-00:00":25}
        }
        
        information = ["PEDRO=TU06:40-13:10,TH07:00-16:35,FR00:00-03:00,SU10:00-15:00   === 455 USD"]
        expected_result = "El monto a pagar de PEDRO es: 455 USD"
        
        result = None
        for i in information:
            result = (execute(i, file_name_to_write_content)).strip()
        self.assertEqual(result, expected_result)
       

# Run the tests
if __name__ == "__main__":
    unittest.main()
