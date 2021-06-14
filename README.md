# FamaFrenchIndustries
A function that classifies a company to a Fama-French Industry according to its 4-digit SIC code. 

There are 2 functions in FFIndustry.py file:
  1. FFIndustry
    Reads the raw .txt file which contains the Fama-French Industry Definitions
    and creates a dictionary with keys = 'industries' and items = list of intervals saved as lists.
    
  2. AssignFFIndustry
    Uses the industry definitions of FFIndustry to assign an industry name to a 4-digit SIC code 
    to a company/entity.
    
   
