
import typing


def to_list(value: typing.Optional[str, list, set], delimiter=',') -> typing.List[str]:
    # TODO: delimiters quoting support
    if isinstance(value, str):
        return [item.strip() for item in value.split(delimiter)]

    if not value:
        return []

    return list(value)


class Flow:
    pass


class FlowRec:
    def __init__(
        self,
        value: float = 0,
        reset: bool = False,
        comment: str = None,
        tags: typing.Optional[str, list] = None,
    ):
        self.value = value
        self.reset = reset
        self.comment = comment
        self.tags = set(to_list(tags))
