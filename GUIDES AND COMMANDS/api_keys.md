# API KEYS

# Add API-key to env (Linux / Mac)
1) Write cmd terminal:
nano ~/.zshrc
2) Write in the file and save:
export="API-KEY"
3) Kør følgende i terminalen (du bruger python i) for at "gemme"
source ~/.zshrc

# Show API-keys in env (Linux / Mac)
cat ~/.zshrc

# Get API
import os
key = os.getenv("API_KEY")

