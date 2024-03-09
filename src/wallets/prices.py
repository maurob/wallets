from typing import TypeVar as Cols

import pandas as pd
from defabipedia import Chain
from rich.progress import track

from . import natives, tokens
from .helpers import listify


def gather(block_ids: dict) -> Cols("chain symbol price"):
    @listify
    def cases():
        for chain in natives.chains:
            Tokens = tokens.grouped_by_chain.get(chain, [])
            for Asset in [natives.Coin, *Tokens]:
                yield chain, Asset

    df = pd.DataFrame(columns="chain symbol price".split())

    for chain, Asset in track(cases, description="Getting pices"):
        asset = Asset(chain, block_ids[chain])

        if chain == Chain.BINANCE:
            continue  # TODO: Fix binance price

        df.loc[len(df)] = chain, asset.symbol, asset.price_usd

    return df
