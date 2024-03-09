repo_dir=$(dirname "$(readlink -f "$0")")
python3 -m venv --prompt wallets $repo_dir/venv
source $repo_dir/venv/bin/activate
pip install --upgrade pip
pip install .
for interpreter in bash zsh fish pwsh; do
    wallets --install-completion $interpreter 2> /dev/null
done
