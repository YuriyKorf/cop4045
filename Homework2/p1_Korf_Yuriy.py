#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:38:01 2026

@author: Yuriy Korf
p1_Korf_Yuriy.py
COP4045 - Homework 2

"""

def line_number(input_file: str, output_file: str) -> None:
    """
    Description:
        Reads a text file and writes its contents to another text file with each line numbered.

    Numbering is in the format:
        1.
        2.
        3.
        ...

    Parameters:
        input_file (str): The name of the text file to be read from.
        output_file (str): The name of the text file to write to.

    Error handling:
        An OSError is re-raised and an error message is printed to the terminal if an error
        occurs during file read or write operations. 
        
    """
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for number, line in enumerate(infile, start=1):
                outfile.write(f"{number}. {line}")
    except OSError as e:
        print("An error occurred while processing the files.")
        print(f"Details: {e}")
        raise
        
def parse_functions(filename: str) -> tuple:
    """
    Description:
       Reads and parses a Python file line by line and then returns
       each function's details found in the file.

    Return format:
       In alphabetical order, a tuple of tuples is returned with the line number, the function name, 
       the formal argument list as a string, and the function code as a string.

    Parameters:
       filename (str): The name of the Python file to be parsed.

    Error handling:
       An OSError is re-raised and an error message is printed to the terminal
       if an error occurs during file read operations.
   """
   
    try:
        with open(filename, "r") as infile:
            lines = infile.readlines()
            
        functions = []
        
        for number, line in enumerate(lines, start=1):
            if line.startswith("def "):
                function_name = line.split("(")[0].replace("def ", "").strip()
                arguments = line.split("(", 1)[1].split(")", 1)[0]
                function = (number, function_name, arguments)
                functions.append(function)
        return tuple(functions)
            
                
                
    except OSError as e:
        print("An error occurred while reading the file.")
        print(f"Details: {e}")
        raise



def main() -> None:
    """
    Tests the line_number and parse_functions functions on this file.
    """

    in_file = "p1_Korf_Yuriy.py"
    out_file = "p1_Korf_Yuriy_output.txt"

    line_number(in_file, out_file)
    parsing_result = parse_functions(in_file)
    print(parsing_result)

if __name__ == "__main__":
    main()
