import os

PATHS = {
    'saves': f'{os.getcwd()}\\saves'  
}

SEARCH_LINE = r'(?<=: ).*'
CLEAN_LINE = r'(.*\s:\s)'