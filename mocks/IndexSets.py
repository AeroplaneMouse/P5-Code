from models.IndexSet import IndexSet
from mocks import Patterns, IndexRecords

A = IndexSet(
    Patterns.A,
    [IndexRecords.A0, IndexRecords.B0, IndexRecords.C0]
)


All = [A]
