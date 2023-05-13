#!bin/env/python3

from datetime import time, datetime, timedelta

compensation = {
    "MO": {"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
    "TU":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20}, 
    "WE":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
    "TH":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
    "FR":{"00:01-09:00":25, "09:01-18:00":15, "18:01-00:00":20},
    "SA":{"00:01-09:00":30, "09:00-18:00":20, "18:01-00:00":25},
    "SU":{"00:01-09:00":30, "09:00-18:00":20, "18:01-00:00":25}
}

def read_file(file_name):
    informations = []
    with open(file_name, "r") as file:
        
        for f in file:
            line = f.strip()
            if line:
                information = (line.split("==="))[0].strip()
                # print(information)
                informations.append(information)
                
    return informations
                
def write_file(file_name, value):
    with open(file_name, "a") as file:
        file.write(value + "\n")

def evaluate_compensation(compensation, employee, _day, start_hour_in_time_format_from_input, end_hour_in_time_format_from_input):
    """
            This are transforming strings time into time data type, by taking "10:00-12:00", spliting it and t
            hen transforming it to time data type, return "1900-01-01 10:00:00", then by using strftime we extract 
            just the time part of the string.
    """
    _value = []
    for d in compensation.keys():
        
        if d == _day:
            
            for h in compensation.get(d).keys():
                start_hour_in_time_format = datetime.strptime(h.split("-")[0], "%H:%M").strftime("%H:%M") 
                end_hour_in_time_format = datetime.strptime(h.split("-")[1], "%H:%M").strftime("%H:%M")
                
                if end_hour_in_time_format.split(":")[0] == datetime.strptime("00", "%H").strftime("%H"):
                    end_hour_in_time_format = f'24:{end_hour_in_time_format.split(":")[1]}'
                    
                if start_hour_in_time_format <= start_hour_in_time_format_from_input <= end_hour_in_time_format:
                    #print(f"{start_hour_in_time_format_from_input} - {end_hour_in_time_format_from_input} is in range of {start_hour_in_time_format} - {end_hour_in_time_format}")
                   
                    if end_hour_in_time_format_from_input <= end_hour_in_time_format:
                        if end_hour_in_time_format.split(":")[0] == "24":
                            end_hour_in_time_format = f'00:{end_hour_in_time_format.split(":")[1]}'
                            
                        print(f"{start_hour_in_time_format_from_input} - {end_hour_in_time_format_from_input} is in range of {start_hour_in_time_format} - {end_hour_in_time_format}")
                        
                        _time = f"{start_hour_in_time_format}-{end_hour_in_time_format}".strip()
                        
                        start_hour_from_input = (datetime.strptime(start_hour_in_time_format_from_input, "%H:%M"))
                        end_hour_from_compensation = (datetime.strptime(end_hour_in_time_format_from_input, "%H:%M"))
                        
                        _time_spended = round(abs((start_hour_from_input - end_hour_from_compensation).total_seconds() / 3600))
            
                        _payment = compensation.get(d).get(_time) * _time_spended
                        _value = []
                        _value.append(_payment)
                        print(f"{compensation.get(d).get(_time)} {_time_spended} {_payment}")
                        return _value

                    else:
                        if start_hour_in_time_format <= start_hour_in_time_format_from_input and end_hour_in_time_format <= end_hour_in_time_format_from_input:
                            print(f"{start_hour_in_time_format_from_input} - {end_hour_in_time_format_from_input} is in range of {start_hour_in_time_format} - {end_hour_in_time_format}")
                            
                            if end_hour_in_time_format.split(":")[0] == "24":
                                end_hour_in_time_format = f'00:{end_hour_in_time_format.split(":")[1]}'

                            _time = f"{start_hour_in_time_format}-{end_hour_in_time_format}".strip()
                     
                            start_hour_from_input = (datetime.strptime(start_hour_in_time_format_from_input, "%H:%M"))
                            end_hour_from_compensation = (datetime.strptime(end_hour_in_time_format, "%H:%M"))

                            _time_spended = round(abs((start_hour_from_input - end_hour_from_compensation).total_seconds() / 3600))
                            _payment = compensation.get(d).get(_time) * _time_spended
                            print(f"{compensation.get(d).get(_time)} {_time_spended} {_payment}")
                            _value.append(_payment)

                if start_hour_in_time_format >= start_hour_in_time_format_from_input and start_hour_in_time_format <= end_hour_in_time_format_from_input:            
                            
                            if end_hour_in_time_format.split(":")[0] == "24":
                                end_hour_in_time_format = f'00:{end_hour_in_time_format.split(":")[1]}'

                            print(f"{start_hour_in_time_format_from_input} - {end_hour_in_time_format_from_input} is in range of {start_hour_in_time_format} - {end_hour_in_time_format}")

                            _time = f"{start_hour_in_time_format}-{end_hour_in_time_format}".strip()
                            
                            start_hour_from_compensation = (datetime.strptime(start_hour_in_time_format, "%H:%M"))
                            end_hour_from_input = (datetime.strptime(end_hour_in_time_format_from_input, "%H:%M")) if (datetime.strptime(end_hour_in_time_format_from_input, "%H:%M")) <= (datetime.strptime(end_hour_in_time_format, "%H:%M")) else (datetime.strptime(end_hour_in_time_format, "%H:%M"))

                            if end_hour_from_input == datetime.strptime("00:00", "%H:%M"):
                                end_hour_from_input += timedelta(days=1) # This is adding one day to the end_hour_from_input because the it is comming in 00:00 so every number rested by 0 is iqual to it self
                            
                            _time_spended = round(abs((start_hour_from_compensation - end_hour_from_input).total_seconds() / 3600))
                            _payment = compensation.get(d).get(_time) * _time_spended
                            
                            print(f"{compensation.get(d).get(_time)} {_time_spended} {_payment}")
                            _value.append(_payment)
                                      
    return _value
                            
def make_list_with_data(work_days):
    """
        Here I create a list of dict with the day, start and end time 
    """
    elements = []
    for d_t in work_days:
        _day = d_t[:2].strip()
        _time = d_t[2:].strip()
        
        start_hour_in_time_format_from_input = datetime.strptime(_time.split("-")[0], "%H:%M").strftime("%H:%M")
        end_hour_in_time_format_from_input = datetime.strptime(_time.split("-")[1], "%H:%M").strftime("%H:%M")
        
        elements.append({"day":_day, "start_hour_in_time_format_from_input":start_hour_in_time_format_from_input, "end_hour_in_time_format_from_input":end_hour_in_time_format_from_input})
                   
    return elements

def execute(informations, file_name_to_write_content):

    information = informations.split("=")
    employee = information[0]
    work_days = information[1].split(",")
    
    elements = make_list_with_data(work_days) #Here I create a list of dict with the day, start and end time, so we can later loop it and process it.
    
    value_to_pay = []
    for e in elements:
        result = evaluate_compensation(compensation, employee, e["day"], e["start_hour_in_time_format_from_input"], e["end_hour_in_time_format_from_input"])
        value_to_pay.extend(result)
    
    value = f"""El monto a pagar de {employee} es: {sum(value_to_pay)} USD \n"""
    
    write_file(file_name_to_write_content, value)
    return value

def main():
    
    file_name_to_read = input("Please enter the file_name to read content: ") 
    file_name_to_write_content = input("Please enter the file_name to write the result: ")
    
    file_name_to_read = "docs/" + file_name_to_read
    file_name_to_write_content = "docs/" + file_name_to_write_content
    
    information = read_file(file_name_to_read)
    
    for i in information:
        execute(i, file_name_to_write_content)
    
    
if __name__ == "__main__":
    main()
 

