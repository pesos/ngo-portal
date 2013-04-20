# Running clean.sh initially
source clean.sh

cd ../../ # Change to project root directory

# Enable virtual environment
source ./venv/bin/activate

# Setting python path
export PYTHONPATH="$PYTHONPATH:$PWD/src"


cd src/scripts # Change back to the scripts directory

# Enable pyclean command
alias pyclean="source $PWD/clean.sh"
