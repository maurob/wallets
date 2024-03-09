from collections import defaultdict
from decimal import Decimal

from defabipedia import Chain
from defyes.contracts import Erc20
from defyes.prices.prices import get_price as get_price_in_usd
from defyes.types import Addr, TokenAmount


class Erc20(Erc20):
    @property
    def last_block_id(self):
        return self.web3.eth.block_number

    def balance(self, wallet: Addr):
        return TokenAmount.from_teu(self.balance_of(wallet), self)

    @classmethod
    def chains(cls):
        return cls.default_addresses.keys()

    @property
    def price_usd(self):
        price, _, _ = get_price_in_usd(self.address, self.block, self.chain)
        return Decimal(price)

    @property
    def chain(self):
        return self.blockchain


class DAI(Erc20):
    default_addresses: dict[str, str] = {
        Chain.ETHEREUM: Addr("0x6B175474E89094C44Da98b954EedeAC495271d0F"),
        Chain.POLYGON: Addr("0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063"),
        Chain.BINANCE: Addr("0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3"),
    }


class USDT(Erc20):
    default_addresses: dict[str, str] = {
        Chain.ETHEREUM: Addr("0xdAC17F958D2ee523a2206206994597C13D831ec7"),
        Chain.POLYGON: Addr("0xc2132D05D31c914a87C6611C10748AEb04B58e8F"),
    }


class USDC(Erc20):
    default_addresses: dict[str, str] = {
        Chain.ETHEREUM: Addr("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"),
    }


class WETH(Erc20):
    default_addresses: dict[str, str] = {
        Chain.POLYGON: Addr("0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619"),
    }


grouped_by_chain = defaultdict(set)
for Token in Erc20.__subclasses__():
    for chain in Token.default_addresses:
        grouped_by_chain[chain].add(Token)


chains = list(grouped_by_chain.keys())
