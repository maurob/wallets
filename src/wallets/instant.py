import logging
from datetime import datetime

from karpatkit.node import get_node

from .natives import chains

logger = logging.getLogger(__name__)


def latest_blocks_time_dict(chains=chains):
    blocks_dict = {"latest": True}
    for chain in chains:
        node = get_node(chain)
        blocks_dict[chain] = node.eth.block_number

    now = datetime.now().replace(microsecond=0)
    blocks_dict["date"] = now.strftime("%Y-%m-%d")
    blocks_dict["dttm"] = now.strftime("%Y-%m-%d %H:%M:%S")

    return blocks_dict


if __name__ == "__main__":
    print(latest_blocks_time_dict())
