description = """
### List of API: 

## user

* **GET user/**: show all users from database
* **GET user/{user_id}**: show user by id
* **POST user/**: create new user
* **DELETE user/{user_id}**: delete user by id 

## protein

* **GET protein/**: show tests from database (max 100)
* **GET protein/{protein_id}**: show test with given id
* **POST protein/{protein_id}**: add new protein
* **POST protein/add_fasta/{protein_id}**: add fasta file to existing protein
* **DELETE protein/{protein_id}**: delete protein by id

## uniprot

* **GET uniprot/id/{protein_id}** show all information about protein from uniprot database
* **GET uniprot/name/{protein_name}** show all information about protein from uniprot database

## AlphaFold

* **GET AlphaFold/prediction/{qualifier}** information about protein structures predicted by AlphaFold such as mmCIF, bCIF and PDB
* **GET /AlphaFold/uniprot_information/summary/{qualifier}** summary information about protein from uniprot
"""
