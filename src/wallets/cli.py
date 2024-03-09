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
def prices(datetime: str = ""):
    pass
