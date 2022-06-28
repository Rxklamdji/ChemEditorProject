import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit import DataStructs
import numpy as np



#m = Chem.MolFromSmiles('COc1cc(C=O)ccc1O')
#print(m)

data = pd.read_csv('./external_mol2vec.csv')
data.head()

#my_one_smile_string = data['Canonical SMILES'][0]
#my_one_mole_string = Chem.MolFromSmiles(my_one_smile_string)
#my_result = Chem.MolToMolBlock(my_one_mole_string)
#print(my_result)

smiles_list = data['Canonical SMILES']
mol_list = []
for smiles in smiles_list:
    mol = Chem.MolFromSmiles(smiles)
    mol_list.append(mol)
img = Draw.MolsToGridImage(mol_list)
img




