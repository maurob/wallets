from typing import TypeVar as Cols

from defabipedia import Chain
from rich import print
from rich.table import Table


def money(amount):
    return f"{amount:,.2f}".replace(",", "_")


def price_str(price):
    if price < 1:
        return f"{price:,.8g}".replace(",", "_")
    else:
        return f"{price:,.9g}".replace(",", "_")


def block_ids_table(block_ids: dict):
    table = Table(title="Block ids utilizados")
    table.add_column("Chain", justify="left", style="cyan", no_wrap=True)
    table.add_column("Block id", justify="right", style="white", no_wrap=True)
    table.add_column("Datetime", justify="right", style="red", no_wrap=True)

    dttm = block_ids["dttm"]
    for chain in Chain._by_id.values():
        try:
            block_id = block_ids[chain]
        except KeyError:
            pass
        else:
            table.add_row(chain, f"{block_id:,}".replace(",", "_"), dttm)
    return table


def main(df: Cols("chain wallet amount symbol price amount_usd")):
    table = Table(title="Balances crypto")
    table.add_column("Chain", justify="left", style="cyan", no_wrap=True)
    table.add_column("Wallet", justify="left", style="yellow", no_wrap=True)
    table.add_column("Amount", justify="right", style="green bold", no_wrap=True)
    table.add_column("Symbol", justify="left", style="white", no_wrap=True)
    table.add_column("USD", justify="right", style="green", no_wrap=True)
    for t in df.itertuples():
        table.add_row(
            t.chain,
            t.wallet,
            price_str(t.amount),
            t.symbol,
            money(t.amount_usd),
        )
    total_usd = df.amount_usd.sum()
    table.add_section()
    table.add_row("", "", "", "Total", money(total_usd))

    grid = Table.grid()
    grid.add_row(table, prices(df))
    return grid


def prices(df: Cols("chain symbol price")):
    table = Table(title="Symbols prices")
    table.add_column("Chain", justify="left", style="cyan", no_wrap=True)
    table.add_column("Symbol", justify="left", style="white", no_wrap=True)
    table.add_column("Price [USD]", justify="right", style="white", no_wrap=True)
    for t in df.drop_duplicates(subset=["chain", "symbol"]).itertuples():
        table.add_row(t.chain, t.symbol, price_str(t.price))
    return table


def table_by_symbol(df: Cols("symbol amount amount_usd"), sufix=""):
    table = Table(title=f"Grouped by symbol{sufix}")
    table.add_column("Symbol", justify="left", style="white", no_wrap=True)
    table.add_column("Amount", justify="right", style="green bold", no_wrap=True)
    table.add_column("USD", justify="right", style="green", no_wrap=True)
    for t in df.groupby("symbol").agg({"amount": "sum", "amount_usd": "sum"}).itertuples():
        table.add_row(t.Index, money(t.amount), money(t.amount_usd))
    return table


def from_values_to_key(*pairs):
    return {value: key for key, values in pairs for value in values.split()}


def table_by_symbol_group(df: Cols("symbol amount amount_usd")):
    df = df.copy()
    df.symbol = df.symbol.apply(convert_symbol_to_group_name)
    return table_by_symbol(df, sufix=" group")


def convert_symbol_to_group_name(symbol):
    return symbol_to_group.get(symbol, symbol)


symbol_to_group = from_values_to_key(
    ("ETH", "WETH stETH"),
    ("cUSD", "DAI USDT USDC"),
)


def table_by_chain(df: Cols("chain amount_usd")):
    table = Table(title="Grouped by chain")
    table.add_column("Chain", justify="left", style="cyan", no_wrap=True)
    table.add_column("USD", justify="right", style="green", no_wrap=True)
    for chain, amount in df.groupby("chain")["amount_usd"].sum().items():
        table.add_row(chain, money(amount))
    return table


def table_by_wallet(df: Cols("wallet amount_usd")):
    table = Table(title="Grouped by wallet")
    table.add_column("Wallet", justify="left", style="yellow", no_wrap=True)
    table.add_column("USD", justify="right", style="green", no_wrap=True)
    for wallet, amount in df.groupby("wallet")["amount_usd"].sum().items():
        table.add_row(wallet, money(amount))
    return table


def show_all(block_ids, df: Cols("chain wallet amount symbol price amount_usd")):
    grouped = Table.grid()
    grouped.add_row(table_by_symbol(df), table_by_symbol_group(df), table_by_chain(df), table_by_wallet(df))
    print(block_ids_table(block_ids), main(df), grouped)
