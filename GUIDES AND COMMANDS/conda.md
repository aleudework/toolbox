### Conda ###

# Create conda environment
conda create --name "name of env"


# Download conda dependencies
- De fleste dependencies fra pip er også som conda. Conda er dog bedre til afhængighederne.
conda install "dependency"

# Opdater environment.yml fil
- Lav .yml fil (freeze) med (alle conda) dependencies
- Vær obs på, om du er på den korrekte sti
conda env export > environment.yml

# Opret environment.yml fil
1) Opret manuelt en environment.yml fil
2) Skriv noget normalt/standard env i den, f.eks:
name: conda_api
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pandas

3) Freeze den som der gør ovenstående

# Opret / Opdater / Big miljø ud fra environment fil
- Vær obs på at være på den korrekte sti.
conda env update --file environment.yml --prune