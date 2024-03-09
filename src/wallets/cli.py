import typer

app = typer.Typer()


@app.command()
def balance(wallets_file: str = "wallets.yaml", when: str = ""):
    from . import balance, instant, views
    from .loader import load_file

    wallets = load_file(wallets_file)
    block_ids = instant.create_blocks_time_dict(when) if when else instant.latest_blocks_time_dict()
    df = balance.gather(wallets, block_ids)
    views.show_all(block_ids, df)


@app.command()
def prices(when: str = "", json: bool = False):
    from . import instant, prices, views

    block_ids = instant.create_blocks_time_dict(when) if when else instant.latest_blocks_time_dict()
    df = prices.gather(block_ids)
    if json:
        views.print(df.to_json())
    else:
        views.print(views.prices(df))


@app.command()
def latest(dict: bool = False):
    """
    Show the latest block numbers for the known blockchains.
    """
    from .instant import latest_blocks_time_dict
    from .views import block_ids_table, print

    block_ids = latest_blocks_time_dict()
    if dict:
        print(block_ids)
    else:
        print(block_ids_table(block_ids))
