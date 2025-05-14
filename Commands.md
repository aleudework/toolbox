

### Conda

- Conda env
conda create --name "name of env"

- Hent conda pakker ligesom med pip  (pip virker stadig fint dertil, men conda er bedre)
conda install "dependency"

- Lav .yml fil (freeze) med (alle conda) dependencies
conda env export > environment.yml

### Git

- Clone repo med ssh. MEGA OBS PÅ. Vælg github-work. Ellers bliver det aleude og ikke aleudework
git clone git@github-work:aleudework/fine-tune-models-exp.git 
