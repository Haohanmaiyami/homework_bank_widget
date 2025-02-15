from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, state="EXECUTED")
    assert len(result) == 2
    assert all(tx["state"] == "EXECUTED" for tx in result)


def test_sort_by_date(sample_transactions):
    result = sort_by_date(sample_transactions)
    assert result[0]["date"] == "2025-02-05"
    assert result[-1]["date"] == "2025-01-01"
