from models.IndexSet import IndexSet
from mocks import Patterns, IndexRecords

A = IndexSet(
    Patterns.A,
    [IndexRecords.A, IndexRecords.C]
)


All = [A]
