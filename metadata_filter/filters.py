import re
from functools import reduce
from operator import or_
from typing import Dict, Optional, Sequence

from metadata_filter.rules import *


def apply_filter(rule: FilterRule, s: str) -> str:
    idx = rule.source.rfind("/")
    pattern = rule.source[1:idx]
    modifiers = rule.source[idx + 1 :]
    flags = _modifiers_to_flags(modifiers)
    kwargs = {}
    if flags is not None:
        kwargs["flags"] = flags
    return re.sub(pattern, rule.target, s, **kwargs)


def apply_filters(
    rules: Sequence[FilterRule], s: str, until_stable: bool = True
) -> str:
    def apply(x: str, rule: FilterRule) -> str:
        return apply_filter(rule, x)

    def reduce_until_stable(f, x):
        x_prev, x = x, f(x)
        while x != x_prev:
            x_prev, x = x, f(x)
        return x

    apply_rules = lambda x: reduce(apply, rules, x)

    if not until_stable:
        return apply_rules(s)

    return reduce_until_stable(apply_rules, s)


_modifier_lut: Dict[str, int] = {"i": re.I}


def _modifiers_to_flags(modifiers: str) -> Optional[int]:
    flag_list = [_modifier_lut[x] for x in modifiers]
    if len(modifiers) == 0:
        return None
    return reduce(or_, flag_list)


__all__ = [
    "apply_filter",
    "apply_filters",
]
