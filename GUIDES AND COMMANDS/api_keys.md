# API KEYS

# Add API-key to env (Linux / Mac)
- Write in terminal:
nano ~/.zshrc
- Write and save:
export="API-KEY"

# Show API-keys in env (Linux / Mac)
cat ~/.zshrc

# Get API
import os
key = os.getenv("API_KEY")

