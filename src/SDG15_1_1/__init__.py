"""SDG 15.1.1"""

from sdg_base.src.sdg_base_src.sdg_base import SDGBase 
from .sdg_15_1_1 import SDG15_1_1, run_sdg15_1_1

from typing import List

__all__: List[str] = ["SDGBase", "SDG15_1_1", "run_sdg15_1_1"]