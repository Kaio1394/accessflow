class EmptyDataTable(ValueError):
    """Exception raised when a data table is empty or invalid."""
    def __init__(self, message="Data table is empty or invalid."):
        super().__init__(message)


class EmptyDataFrame(ValueError):
    """Exception raised when a pandas DataFrame is empty or not usable."""
    def __init__(self, message="DataFrame is empty or was not loaded correctly."):
        super().__init__(message)


class WorkbookNullObject(Exception):
    """Exception raised when the Workbook object is null or not properly loaded."""
    def __init__(self, message="Workbook is null or was not loaded correctly."):
        super().__init__(message)
        
class WorksheetNullObject(Exception):
    """Exception raised when the Worksheet object is null or not properly loaded."""
    def __init__(self, message="Worksheet is null or was not loaded correctly."):
        super().__init__(message)
        
class TabNameNotFound(ValueError):
    """Exception raised when the specified worksheet/tab name is not found in the workbook."""
    def __init__(self, message="The specified worksheet/tab name was not found in the workbook."):
        super().__init__(message)
