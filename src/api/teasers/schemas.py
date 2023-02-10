from ninja import Schema


class IdList(Schema):
    ids: list[str]


class Account(Schema):
    current_balance: float


class Author(Schema):
    user_id: int
    first_name: str
    last_name: str
    account: Account


class Teaser(Schema):
    id: int
    title: str
    description: str | None = None
    category: str
    status: str
    author: Author
