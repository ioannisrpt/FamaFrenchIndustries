# -*- coding: utf-8 -*-
# Python 3.7.7
"""

Last Updated : 14 JUne 2021

Assign Stocks to Industries according to their 4-digit SIC.

Industry definitions are extracted from the Fama-French library available at 
"https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html"

SIC code defined by SEC available at 
"https://www.sec.gov/info/edgar/siccodes.htm"
"""


import os
import pandas as pd
from pandas import DataFrame, Series




# -------------------------------------------------------------------
#             PRELIMINARY FUNCTIONS
# --------------------------------------------------------------


def save_df(df, filename, save_dir = os.getcwd()):
    # true filename
    name = filename +'.csv'
    # Full file path
    file_path = os.path.join(save_dir, name)
    # save as csv 
    df.to_csv(file_path)
    
    
# Function that converts any column of a dataframe that conntains the string 'date' 
# to a datetime object. 
# Implicitly, datetime format is inferred from data.
def ConvertDate(df):
    """
    Parameters:
    ------------
    df: dataframe
        input dataframe
        
    Returns:
    --------
    df_new: dataframe
        transformed dataframe
    """
    for name in df.columns:
        if 'date' in name.lower():
            # Conert to datetime object of monthly period
            df[name] = pd.to_datetime(df[name])
    return df






# -----------------------------------------------------------------------
#      ASSIGN INDUSTRY BASED ON SIC AND FAMA-FRENCH CLASSIFICATION
# -----------------------------------------------------------------------


def FFIndustry(ff_txt, encoding = "utf-8"):
    """
    
    Parameters
    ----------
    ff_txt : path directory
        Path directory that corresponds to a .txt file for industry classification
        on the 4-digit SIC code as extracted from the Fama-French Library.
    encoding : str, Default="utf-8"
        the type of encoding to be used in opening the .txt file.


    Returns
    -------
    dict_ff : dictionary
        Dictionary with keys = FF industry and items =  list of SIC intervals

    """
    
    # Read all the lines of the txt file
    f = open(ff_txt, 'r', encoding = encoding)
    lines = f.readlines()
    f.close()
    
    # Strip lines 
    Lines = [line.strip() for line in lines]
    
    
    # Dictionary with keys = industry as a string and items a list with elements
    # other lists that correspond to an interval of SIC.
    dict_ff = {}
    
    # We exploit the text structure of the .txt file of Fama-French to construct 
    # the industry dictionary.
    
    for line in Lines:
        # When a line is not empty and the first element is an integer with less
        # than 3 digits, the name of the industry is retrieved.
        first_element = line.split(' ')[0]
        if len(line)> 0 and len(first_element) < 3:
            # Exctract the second element which of the line
            industry_name = line.split(' ')[1]
            # Insert the industry in the dict
            dict_ff[industry_name] = []
        # When a line is not empty and the first element has a length more than 
        # 3, the SIC intervals are retrieved.
        if len(line) > 0 and len(first_element) > 3:
            # Retrieve the interval
            line_interval = line.replace('-', ' ').split(' ')
            # The first and second element is the lower and upper limit of 
            # the interval.
            lower = int(line_interval[0])
            upper = int(line_interval[1])
            interval = [lower, upper]
            # Append the interval to the correct industry
            dict_ff[industry_name].append(interval)
            
    return dict_ff
            
            
            
# Assign a FF industry to a stock based on the FF definition and SIC number.
def AssignFFIndustry(dict_ff, SIC, Other = False):
    """
    
    Parameters
    ----------
    dict_ff : dictionary
        Dictionary with keys = FF industry and items =  list of SIC intervals
    SIC : integer
        The 4-digit SIC code which is an integer. 
    Other : boolean
        If True, any SIC that is not included in the dict_ff, will be 
        categorized as 'Other'. Default is False.

    Returns
    -------
    industry : string
        The FF industry in which firm with SIC belongs

    """
    # Iterature through all industries
    for industry in dict_ff:
        # Iterate through all intervals
        for interval in dict_ff[industry]:
            # If SIC lies inside the interval, assign industry
            if interval[0] <= SIC and SIC <= interval[1]:
                return industry
            else:
                if Other:
                    return 'Other'
            
                

                








        
    
    




