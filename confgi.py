import numpy as np


path_data = 'input_data\Blockchain Adoption in Digital Healthcare 2 - 15012023 (1).csv' 


x = np.arange(0, 1.1, 0.01)
membership_function = 'Gaussian' #'Gaussian' # 'Triangular'


# Very low
# Low	
# Medium
# High	
# Very high

#### ---> Triangular membership function generator
triangular_fuzzy_number = {
    'Very low' :[0.0, 0.0, 0.2],
    'Low': [0.0, 0.2, 0.4],
    'Medium':[0.2, 0.4, 0.6],
    'High':[0.4, 0.6, 0.8],
    'Very high': [0.6, 0.8, 1.0]
}

#### --->  Gaussian fuzzy membership function.
sigma = 0.09
alpha = 0.2
gaussian_fuzzy_mean = {
    'Very low' :0,
    'Low': 0.2,
    'Medium':0.4,
    'High':0.6,
    'Very high': 0.8
}


