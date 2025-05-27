### Conda ###

- Conda env
conda create --name "name of env"

- Hent conda pakker ligesom med pip  (pip virker stadig fint dertil, men conda er bedre)
conda install "dependency"

- Lav .yml fil (freeze) med (alle conda) dependencies
conda env export > environment.yml

- Opdate conda miljø (prune fjerner pakker, som ikke er med i env)
conda env update --file environment.yml --prune