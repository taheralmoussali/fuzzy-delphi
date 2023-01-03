import pandas as pd
import math 
import statistics
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from confgi import gaussian_fuzzy_mean , triangular_fuzzy_number , sigma , path_data , membership_function ,alpha ,x



def draw_figure():


    if membership_function == 'Gaussian': 
        # gaussmf = fuzz.gaussmf(x, mean, sigma)
        very_low = fuzz.gaussmf(x, gaussian_fuzzy_mean['Very low'], sigma)
        low = fuzz.gaussmf(x, gaussian_fuzzy_mean['Low'], sigma)
        medium = fuzz.gaussmf(x, gaussian_fuzzy_mean['Medium'], sigma)
        high = fuzz.gaussmf(x, gaussian_fuzzy_mean['High'], sigma)
        very_high = fuzz.gaussmf(x, gaussian_fuzzy_mean['Very high'], sigma)

    else:
        # Generate fuzzy membership functions
        very_low = fuzz.trimf(x, triangular_fuzzy_number['Very low'])
        low = fuzz.trimf(x, triangular_fuzzy_number['Low'])
        medium = fuzz.trimf(x, triangular_fuzzy_number['Medium'])
        high = fuzz.trimf(x, triangular_fuzzy_number['High'])
        very_high = fuzz.trimf(x, triangular_fuzzy_number['Very high'])


    plt.title('Level of effect')
    plt.plot(x, very_low, 'b', linewidth=1.5, label='very low')
    plt.plot(x, low, 'g', linewidth=1.5, label='low')
    plt.plot(x, medium, 'r', linewidth=1.5, label='medium')
    plt.plot(x, high, 'c', linewidth=1.5, label='high')
    plt.plot(x, very_high, 'm', linewidth=1.5, label='very high')

    plt.legend()

    name_img = 'level_of_effect_Gaussian' if membership_function == 'Gaussian' else 'level_of_effect_Triangular'
    plt.savefig('images/'+name_img+'.png')
    plt.show()




def Fuzzy_delphi_mathod():

    """Fuzzy delphi ----->>

    Xmax = ((X1 + X2 + X3)/3)/N  = α
    X Item
    Xmax average score of fuzzy numberNnumber of expert panel involved
    (X1, X2, X3) triangular fuzzy number according to linguistic variable
    """
    ######## read file csv ################
    data = pd.read_csv(path_data)
    # remove columns not important
    data = data.drop(data.columns[0:5], axis=1)
    data = data.drop(data.columns[-2:] ,axis=1)

    if membership_function == 'Gaussian':
        gaussian_fuzzy_numbers = {}
        for key in gaussian_fuzzy_mean.keys():
            mean = gaussian_fuzzy_mean[key]
            lower = mean - math.sqrt(math.log((1/math.pow(alpha,sigma**2)) , math.e))
            upper = mean + math.sqrt(math.log((1/math.pow(alpha,sigma**2)) , math.e))
            gaussian_fuzzy_numbers[key] = [lower , mean, upper]
        print(gaussian_fuzzy_numbers)
        fuzzy_numbers = gaussian_fuzzy_numbers
    else :
        fuzzy_numbers = triangular_fuzzy_number

    ########  each expert’s responses are converted into fuzzy numbers
    for column in data.columns:
        for i in range(len(data[column])):
            data[column][i] = statistics.mean(fuzzy_numbers[data[column][i]])
            print(data[column][i])
    #########
    Xmax = []
    ### ------ > store and convert (average score of fuzzy numbers)
    for column in data.columns:
        Xmax.append(statistics.mean(data[column]))

    ######### -------- ########

    list_of_tuples = list(zip(data.columns, Xmax))
    # Converting lists of tuples into
    # pandas Dataframe.
    df = pd.DataFrame(list_of_tuples,
                    columns=['Item', 'Average score of fuzzy number Xmax)'])
    
    output_name = 'output_Gaussian' if membership_function == 'Gaussian' else 'output_Triangular'

    df.to_csv(output_name+'.csv')



if __name__ == "__main__" :
    Fuzzy_delphi_mathod()
    draw_figure()
