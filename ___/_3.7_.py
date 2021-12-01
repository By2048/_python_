from dataclasses import field, dataclass
from datetime import datetime
from typing import List

import dateutil

"""

https://www.python.org/dev/peps/pep-0557/

"""


class Article(object):
    def __init__(self, _id, author_id, title, text, tags=None,
                 created=datetime.now(),
                 edited=datetime.now()):

        self._id = _id
        self.author_id = author_id
        self.title = title
        self.text = text
        self.tags = list() if tags is None else tags
        self.created = created
        self.edited = edited

        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)

        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return NotImplemented
            return (self._id, self.author_id) == (other._id, other.author_id)

        def __lt__(self, other):
            if not isinstance(other, self.__class__):
                return NotImplemented
            return (self._id, self.author_id) < (other._id, other.author_id)

        def __repr__(self):
            return '{}(id={}, author_id={}, title={})'.format(
                self.__class__.__name__, self._id, self.author_id, self.title)


@dataclass(order=True)
class Article(object):
    _id: int
    author_id: int
    title: str = field(compare=False)
    text: str = field(repr=False, compare=False)
    tags: List[str] = field(default=list(), repr=False, compare=False)
    created: datetime = field(default=datetime.now(), repr=False, compare=False)
    edited: datetime = field(default=datetime.now(), repr=False, compare=False)

    def __post_init__(self):
        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)

        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)
