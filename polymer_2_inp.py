# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:02:42 2022

@author: 983045
"""
import ase as ase
from ase.data.pubchem import pubchem_atoms_search, pubchem_atoms_conformer_search
from ase.io import read,write
from ase.io.xyz import write_xyz
import os
from rdkit import Chem
from rdkit.Chem import AllChem
import glob as glob
import numpy as np

parent_path = "C:/Users/983045/OneDrive - Swansea University/phd_one/molecule_maker/polymers"
project_dir = parent_path + "/project_one" # This is the name of the folder you want to contain all of your inputs in

def make_polymers_inp(name, base_unit, repeat_unit, max_units, generate_inputs):
    name = name
    smiles = []
    for i in range(max_units):
        smile = base_unit
        if i == 0:
            smiles.append(smile)
        else:
            for j in range(i):
                smile = smile + repeat_unit
            smiles.append(smile)
    if generate_inputs == False:
        return(smiles)
    naming = ["monomer", "dimer", "trimer", "tetramer", "pentamer"]
    error_list = [[], []]
    for i in range(len(smiles)):
        naming_string = name + "_" + naming[i]
         # [[Names], [Smiles]]
        mol = Chem.MolFromSmiles(smiles[i])
        mol = Chem.AddHs(mol,explicitOnly=False)
        AllChem.EmbedMolecule(mol)
        xyz = (Chem.MolToXYZBlock(mol))
        if not os.path.isdir(project_dir):
            os.mkdir(project_dir)
        xyz_dir_2_make = project_dir + "/" + name 
        if not os.path.isdir(xyz_dir_2_make):
            os.mkdir(xyz_dir_2_make)
        final_xyz_path = xyz_dir_2_make + "/XYZ"
        if not os.path.isdir(final_xyz_path):
            os.mkdir(final_xyz_path)
        final_input_path = xyz_dir_2_make + "/inputs"
        if not os.path.isdir(final_input_path):
            os.mkdir(final_input_path)
        final_results_path = xyz_dir_2_make + "/results"
        if not os.path.isdir(final_results_path):
            os.mkdir(final_results_path)
        xyz_filepath = final_xyz_path + "/" + naming_string + ".xyz"     
        input_filepath = final_input_path + "/" + naming_string + ".inp"
        print(naming_string)
        x = open(xyz_filepath, "w")
        x.write(xyz)            
        x.close()
        mol = ase.io.read(xyz_filepath)
        atomic_number_array = mol.numbers
        atomic_num = np.sum(atomic_number_array)
        assert atomic_num % 2 == 0
        homo_num = int(atomic_num/2 - 1)
        lumo_num = homo_num + 1
        homo_cube_name = naming_string + '.homo.cube", ' + str(homo_num) 
        lumo_cube_name = naming_string + '.lumo.cube", ' + str(lumo_num)
        lines = ['! B3LYP def2-tzvp D3BJ keepdens opt', '%scf', ' MaxIter 1000', 'end', '%output', ' Print[ P_Hirshfeld] 1', 'end', '%elprop', ' Polar 1', 'end', '%plots', ' dim1 100', ' dim2 100', ' dim3 100', ' Format Gaussian_Cube', ' ElDens("%s.dens.cube");' % naming_string, ' MO("%s, 0);' % homo_cube_name, ' MO("%s, 0);' % lumo_cube_name, 'end', '%pal', ' nprocs 10', 'end', '*xyz 0 1']                    
        f = open(xyz_filepath, 'r')
        counter = 0
        for line in f:        
            if counter < 2:
                print("six eggs")   
            else:
                stripped_line = line.strip()
                lines.append(stripped_line)
                print(line)
            counter += 1
        f.close()
        lines.append("*")
        z = open(input_filepath, "w")
        for line in lines:
            z.write(line)
            z.write('\n')
        z.close()  
    output_filepath = xyz_dir_2_make + "/" + name + ".out"  
    f = open(output_filepath, "w")   
    line_list = []
    header = "Output file for:" + name
    next_line = "Smilesstring for " + str(max_units) + " repeated units"
    line_list.append(header)
    line_list.append("")
    line_list.append(next_line)
    for smile in smiles:
        line_list.append(smile)
    line_list.append("")
    for line in line_list:
        f.write(line)
        f.write('\n')
    f.close()   
    return(smiles)
        
names = ["3HB", "3HV", "3HHX", "4HB"]
base_units = ["OC(C)CC(=O)O", "OC(CC)CC(=O)O", "OC(CCC)CC(=O)O", "OCCCC(=O)O"] 
repeat_units = ["C(C)CC(=O)O", "C(CC)CC(=O)O", "C(CCC)CC(=O)O", "CCCC(=O)O"] 
 
for i in range(len(names)):
    make_polymers_inp(names[i], base_units[i], repeat_units[i], 5, True)
 



        