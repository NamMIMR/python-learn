from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Novel:

    novelID: int
    novelName: str
    novelAuthor: str
    addTime: datetime


@dataclass
class NovelContent:

    novelID: int
    novelName: str
    chapterNum: int
    sectionNum: int
    content: str