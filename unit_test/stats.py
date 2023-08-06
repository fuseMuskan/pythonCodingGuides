import numpy as np
import math
class OneLengthException(Exception):
    pass

def calculate_statistics(dataset: list) -> dict:
    """This function takes a list of numerical data and performs
    calculations for mean, median and standard deviation.

    Args:
        data (list): a list of numerical data

    Returns:
        result (dict): a dictionary containing mean, median, and standard deviation 
    """
    result = dict()
    length = len(dataset)
    try:
        if length == 1:
            raise OneLengthException
        # Calculating mean of the dataset
        mean = sum(dataset) / length
        result["mean"] = mean

        # Calculating median
        dataset.sort()
        if length % 2 != 0:
            median = dataset[int((length)/2)]
        else:
            median= 0.5*(dataset[int(((length-1)/2))] + dataset[int(((length-1)/2)+1)])
        result["median"] = median

        # Calculating standard deviation
        deviation = []
        deviation_square = []
        for num in dataset:
            deviation.append((num-mean))
            deviation_square.append((num-mean) ** 2)
        deviation = sum(deviation)
        deviation_square = sum(deviation_square)

        standard_deviation = math.sqrt((deviation_square + deviation) / length)
        
        result["standard_deviation"] = standard_deviation

        return result

    except ZeroDivisionError:
        return "Dataset cannot be empty"
    except OneLengthException:
        return  "Please provide more than one elements in the dataset" 

    
    

