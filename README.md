# Polymer_gen_orca
This repository contains the code to generate polymers from their base units in smilestring format. The code also has the added functionality of being able to generate orca input files for quatum chemistry calculations.

1) To use this code, some filepaths need to be defined. A 'parent_path' which will be your main project folder, and a secondary path within this where you want the input   files, xyz files and results directories to be created.

2) The next step is to define a base unit for you polymer in smilesstring format and the repeat unit (also in smilesstring format) along with the names of the polymers. 

3) Using the "make_polymers_inp" function:

    USAGE: a = make_polymers_inp(name, base_unit, repeat_unit, max_units, generate_inputs)
    
    name = "3HB" (only an example)
    
    base_unit = "OC(C)CC(=O)O" (only an example)
    
    repeat_unit = "C(C)CC(=O)O" (only an example)
    
    max_units = integer (i.e. 5 will make all polymers up to the pentamer)
    
    generate_inputs  = boolean (True/False - True will create input files for each polymer generated but False will just return a list of polymers in smilesstring format)
    
Note: The final argument is the most important - True will create a filetree for the polymer you are making and generate an input for each polymer up to the polymer that is the length of the max unit (i.e. if max_units = 5, there will be 5 input files created, one for each polymer of incresing size for monomer --> pentamer). 

The code in "polymer_2_inp.py" utilises the the function decribed above in a for loop to generate input files for monomers --> pentamers for 4 different base units - so this is a good examples of how to use the function.
![image](https://user-images.githubusercontent.com/93723782/205310621-071e1f24-fae2-451c-92d7-56d208e855b2.png)

Any issues, email: daniel.yyork@gmail.com

