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
python -m venv --system-site-packages venv
source venv/bin/activate
pip install --editable .
pip install -r requirements-dev.txt
```

## User wallets

Create a `wallets.yaml` file with a list of this structure:

```yaml
- address: "0x..."  # Ensure string (between "")
  name: MetaTrezor
  description: |  # Inline or multi-line description
    I have to behave well. I have to behave well. I have to behave well. I have to behave well. I
    have to behave well. I have to behave well. 
```

### Example

```shell
python -m wallets balance --wallets-file binance.yaml
```
