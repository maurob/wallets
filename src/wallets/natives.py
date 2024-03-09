from decimal import Decimal

from defabipedia import Chain
from defyes.prices.prices import get_price as get_price_in_usd
from defyes.types import Addr
from karpatkit.constants import Address
from karpatkit.node import get_node
from web3 import Web3

symbols = {
    Chain.ETHEREUM: "ETH",
    Chain.POLYGON: "MATIC",
    Chain.BINANCE: "BNB",
}


chains = list(symbols)


def get_native_balance(wallet, block, node):
    wei = node.eth.get_balance(wallet, block)
    return Web3.from_wei(wei, "ether")


class Coin:
    def __init__(self, chain, block):
        self.chain = chain
        self.block = block

    def balance(self, wallet: Addr):
        class Amount:
            @property
            def amount(_self):
                return get_native_balance(wallet, self.block, get_node(self.chain))

        return Amount()

    @property
    def symbol(self):
        return symbols[self.chain]

    @property
    def price_usd(self):
        price, _, _ = get_price_in_usd(Address.ZERO, self.block, self.chain)
        return Decimal(price)
