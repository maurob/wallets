import pandas as pd
from defabipedia import Chain
from rich.progress import track

from . import natives, tokens
from .helpers import listify


def gather(wallets: list, block_ids: dict):
    @listify
    def cases():
        for chain in natives.chains:
            Tokens = tokens.grouped_by_chain.get(chain, [])
            for Asset in [natives.Coin, *Tokens]:
                for index, wallet in enumerate(wallets):
                    yield chain, Asset, (index == 0), wallet

    df = pd.DataFrame(columns="chain wallet amount symbol price amount_usd".split())
    for chain, Asset, new_asset, wallet in track(cases, description="Getting assets info"):
        if new_asset:
            asset = Asset(chain, block_ids[chain])

        if chain == Chain.BINANCE and Asset == natives.Coin:
            continue  # TODO: Fix BNB price

        amount = asset.balance(wallet["address"]).amount
        if amount != 0:
            price = asset.price_usd
            amount_usd = price * amount
            df.loc[len(df)] = chain, wallet["name"], amount, asset.symbol, price, amount_usd

    return df
