

### Conda

- Conda env
conda create --name "name of env"

- Hent conda pakker ligesom med pip  (pip virker stadig fint dertil, men conda er bedre)
conda install "dependency"

- Lav .yml fil (freeze) med (alle conda) dependencies
conda env export > environment.yml

- Opdate conda miljø (prune fjerner pakker, som ikke er med i env)
conda env update --file environment.yml --prune

### Git

- Clone repo med ssh. MEGA OBS PÅ. Vælg github-work. Ellers bliver det aleude og ikke aleudework
git clone git@github-work:aleudework/fine-tune-models-exp.git 

- Reset commit
git reset


### HuggingFace

- Find din HuggingFace nøgle, A sådan her:
cat ~/.cache/huggingface/token

Eller sådan her
cat ~/.huggingface/token

### SSH

- Tjek config names i SSH
cat ~/.ssh/config


### Terminal commands

- Go back Alt+Arrow (skip 1 word).
- Ctrl+A go to the start
- Ctrl+E go to the end

### API ####

# Skriv eller vis API keys i env på mac
1) I terminalen skriv
nano ~/.zshrc
2) Skriv herefter
export API_KEY_NAME="6e..."
3) Gem

# Hent API key i 