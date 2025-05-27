### API ####

# Skriv eller vis API keys i env på mac
1) I terminalen skriv
nano ~/.zshrc
2) Skriv herefter
export API_KEY_NAME="6e..."
3) Gem filen og derefter kør denne her i terminalem:
source ~/.zshrc
4) Så bør den være gemt og klar

# Get API key i Python
import os
key = os.getenv("API_KEY_NAME")

