
from datetime import datetime

class Category:
    def __init__(self, name: str, description: str , is_active: bool, created_ad: datetime) -> None:
        self.name = name
        self.description = description
        self.is_active = is_active
        self.created_ad = created_ad



# Create Caterory is a Enterprise Business Rule, not is datebase. Database is persistence.