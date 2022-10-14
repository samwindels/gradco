def test_0():

    triu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 0, expected_counts)


