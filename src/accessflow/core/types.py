from typing import Any, Union, TypeAlias
from pandas import DataFrame
from accessflow.exceptions.errors import EmptyDataFrame

DataTable: TypeAlias = Union[
    dict[str, list[Any]],
    dict[int, list[Any]]
]

# Dict
# "Header": list[]
def dataframe_to_datatable(df: DataFrame) -> DataTable:
    data_table: DataTable
    try:
        if df.empty:
            raise EmptyDataFrame()      
        data_table = df.to_dict(orient="list")  
        return data_table             
    except Exception as err:
        raise Exception(str(err))