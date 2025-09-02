from typing import Any, Union, TypeAlias

DataTable: TypeAlias = Union[
    dict[str, list[Any]],
    dict[int, list[Any]]
]