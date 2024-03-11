# Wallets

Show wallets balancies and assets prices for crypto assets (currently).

# Install

## In a virtualenv

A short way to install it
```shell
git clone https://github.com/maurob/wallets.git
cd wallets  # go to the downloaded repository directory
source ./install.sh
cp examples/kkit_config.json .  # to use public node endpoints
```
This will create a virtualenv for you, inside the `wallets/venv` directory, and install the application there, using a
frozen set of dependencies version ([`requirements.lock`](requirements.lock)). It'll also activate that environment to
start using the application with the `wallets` command.

> As regular virtualenvs, you should call `source path/to/wallets/venv/bin/activate`, everytime you start a new shell
> session. Like `source venv/vin/activate` if you already are in the repository directory.

An anternative manual way to install it without cloning the repository with `git` yourself:
```shell
python3 -m venv --system-site-packages venv_wallets
source venv_wallets/bin/activate
pip install git+https://github.com/maurob/wallets.git
```
but this way doesn't use [`requirements.lock`](requirements.lock), but it uses the dependencies more flexible defined
inside [`pyproject.toml`](pyproject.toml).

## In a virtualenv for development

```shell
git clone https://github.com/maurob/wallets.git
cd wallets
python3 -m venv --system-site-packages venv
source venv/bin/activate
pip install --editable .
pip install -r requirements-dev.txt
cp examples/kkit_config.json .  # to use public node endpoints
```

## User wallets

Create a `wallets.yaml` file with a list of this structure:

```yaml
- address: "0x..."  # Ensure string (between "")
  name: some_wallet
  description: |  # Inline or multi-line description
    I have to behave well. I have to behave well. I have to behave well. I have to behave well. I
    have to behave well. I have to behave well. 
```

### Example

Just after installed or after calling `source path/to/wallets/venv/bin/activate`

```shell
wallets balance --wallets-file examples/binance.yaml
```
