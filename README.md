# Wallets

# Install

## In a virtualenv

```shell
python -m venv --system-site-packages venv_wallets
source venv_wallets/bin/activate
pip install git+https://github.com/maurob/wallets.git
```

## In a virtualenv for development

```shell
git clone https://github.com/maurob/wallets.git
cd wallets
python -m venv --system-site-packages venv
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

```shell
python -m wallets balance --wallets-file examples/binance.yaml
```
