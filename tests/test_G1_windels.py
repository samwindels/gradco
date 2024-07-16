from test.test_helper import matches_count_windels


# def test_0():

#     triu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     assert matches_count_windels(triu, 1, expected_counts)


def test_1():

    triu = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_2():

    triu = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_3():

    triu = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_4():

    triu = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_5():

    triu = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_6():

    triu = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_7():

    triu = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    expected_counts = [2, 2, 2, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_8():

    triu = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_9():

    triu = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_10():

    triu = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_11():

    triu = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [2, 2, 0, 2, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_12():

    triu = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_13():

    triu = [1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [2, 0, 2, 2, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_14():

    triu = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [0, 2, 2, 2, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_15():

    triu = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    expected_counts = [3, 3, 3, 3, 1, 1, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_16():

    triu = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_17():

    triu = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_18():

    triu = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_19():

    triu = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_20():

    triu = [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_21():

    triu = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [2, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_22():

    triu = [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 2, 1, 0, 1, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_23():

    triu = [1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 1, 2, 0, 0, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_24():

    triu = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_25():

    triu = [1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [2, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_26():

    triu = [0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 2, 0, 1, 1, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_27():

    triu = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 1, 0, 2, 0, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_28():

    triu = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_29():

    triu = [1, 0, 1, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [3, 1, 2, 2, 1, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_30():

    triu = [0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [1, 3, 2, 2, 1, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_31():

    triu = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    expected_counts = [2, 2, 3, 3, 0, 1, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_32():

    triu = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_33():

    triu = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_34():

    triu = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_35():

    triu = [1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [2, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_36():

    triu = [0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_37():

    triu = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_38():

    triu = [0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 1, 2, 0, 0, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_39():

    triu = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 2, 1, 0, 1, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_40():

    triu = [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_41():

    triu = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [2, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_42():

    triu = [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_43():

    triu = [1, 1, 0, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [3, 2, 1, 2, 1, 1, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_44():

    triu = [0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 2, 1, 0, 1, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_45():

    triu = [1, 0, 1, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 1, 2, 0, 0, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_46():

    triu = [0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [1, 2, 3, 2, 0, 1, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_47():

    triu = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    expected_counts = [2, 3, 2, 3, 1, 0, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_48():

    triu = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_49():

    triu = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [2, 1, 1, 0, 2, 2, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_50():

    triu = [0, 1, 0, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_51():

    triu = [1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_52():

    triu = [0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_53():

    triu = [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_54():

    triu = [0, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [2, 2, 2, 0, 2, 2, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_55():

    triu = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_56():

    triu = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_57():

    triu = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [3, 1, 1, 1, 2, 2, 1, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_58():

    triu = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_59():

    triu = [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_60():

    triu = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_61():

    triu = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_62():

    triu = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [2, 3, 3, 2, 2, 2, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_63():

    triu = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    expected_counts = [1, 2, 2, 3, 1, 1, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_64():

    triu = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_65():

    triu = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_66():

    triu = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_67():

    triu = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [2, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_68():

    triu = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_69():

    triu = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [2, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_70():

    triu = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_71():

    triu = [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    expected_counts = [3, 2, 2, 1, 1, 1, 1, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_72():

    triu = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_73():

    triu = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_74():

    triu = [0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 1, 0, 2, 0, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_75():

    triu = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 2, 0, 1, 1, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_76():

    triu = [0, 0, 1, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 1, 2, 0, 0, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_77():

    triu = [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 2, 1, 0, 1, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_78():

    triu = [0, 1, 1, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [1, 2, 2, 3, 0, 0, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_79():

    triu = [1, 1, 1, 1, 0, 0, 1, 0, 0, 0]
    expected_counts = [2, 3, 3, 2, 1, 1, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_80():

    triu = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_81():

    triu = [1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [2, 1, 0, 1, 2, 0, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_82():

    triu = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_83():

    triu = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 1, 0, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_84():

    triu = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_85():

    triu = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [3, 1, 1, 1, 2, 1, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_86():

    triu = [0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_87():

    triu = [1, 1, 1, 0, 1, 0, 1, 0, 0, 0]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_88():

    triu = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 1, 0, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_89():

    triu = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_90():

    triu = [0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [2, 2, 0, 2, 2, 0, 2, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_91():

    triu = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_92():

    triu = [0, 0, 1, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_93():

    triu = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_94():

    triu = [0, 1, 1, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [2, 3, 2, 3, 2, 0, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_95():

    triu = [1, 1, 1, 1, 1, 0, 1, 0, 0, 0]
    expected_counts = [1, 2, 3, 2, 1, 1, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_96():

    triu = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_97():

    triu = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [2, 0, 1, 1, 0, 2, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_98():

    triu = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_99():

    triu = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [3, 1, 1, 1, 1, 2, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_100():

    triu = [0, 0, 1, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 0, 2, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_101():

    triu = [1, 0, 1, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 1, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_102():

    triu = [0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_103():

    triu = [1, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_104():

    triu = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 1, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_105():

    triu = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 0, 2, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_106():

    triu = [0, 1, 0, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_107():

    triu = [1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_108():

    triu = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [2, 0, 2, 2, 0, 2, 2, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_109():

    triu = [1, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_110():

    triu = [0, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [2, 2, 3, 3, 0, 2, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_111():

    triu = [1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    expected_counts = [1, 3, 2, 2, 1, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_112():

    triu = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [0, 0, 0, 0, 2, 2, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_113():

    triu = [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [3, 1, 1, 1, 3, 3, 3, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_114():

    triu = [0, 1, 0, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [1, 1, 0, 0, 3, 2, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_115():

    triu = [1, 1, 0, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [2, 0, 1, 1, 2, 3, 3, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_116():

    triu = [0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [1, 0, 1, 0, 2, 3, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_117():

    triu = [1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [2, 1, 0, 1, 3, 2, 3, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_118():

    triu = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [2, 2, 2, 0, 3, 3, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_119():

    triu = [1, 1, 1, 0, 1, 1, 1, 0, 0, 0]
    expected_counts = [1, 1, 1, 1, 2, 2, 3, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_120():

    triu = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [1, 0, 0, 1, 2, 2, 3, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_121():

    triu = [1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [2, 1, 1, 0, 3, 3, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_122():

    triu = [0, 1, 0, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [2, 2, 0, 2, 3, 2, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_123():

    triu = [1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [1, 1, 1, 1, 2, 3, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_124():

    triu = [0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [2, 0, 2, 2, 2, 3, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_125():

    triu = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [1, 1, 1, 1, 3, 2, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_126():

    triu = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_127():

    triu = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    expected_counts = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_128():

    triu = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_129():

    triu = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_130():

    triu = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_131():

    triu = [1, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [1, 2, 1, 0, 1, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_132():

    triu = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_133():

    triu = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [1, 1, 2, 0, 0, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_134():

    triu = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_135():

    triu = [1, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    expected_counts = [2, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_136():

    triu = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_137():

    triu = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_138():

    triu = [0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 2, 1, 1, 0, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_139():

    triu = [1, 1, 0, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [2, 3, 1, 2, 1, 0, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_140():

    triu = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 2, 1, 0, 0, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_141():

    triu = [1, 0, 1, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [2, 1, 3, 2, 0, 1, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_142():

    triu = [0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 2, 0, 0, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_143():

    triu = [1, 1, 1, 1, 0, 0, 0, 1, 0, 0]
    expected_counts = [3, 2, 2, 3, 1, 1, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_144():

    triu = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_145():

    triu = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_146():

    triu = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 2, 1, 0, 2, 1, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_147():

    triu = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_148():

    triu = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_149():

    triu = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [2, 2, 2, 0, 2, 2, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_150():

    triu = [0, 1, 1, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_151():

    triu = [1, 1, 1, 0, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_152():

    triu = [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_153():

    triu = [1, 0, 0, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [2, 1, 0, 1, 2, 1, 1, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_154():

    triu = [0, 1, 0, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 3, 1, 1, 2, 1, 0, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_155():

    triu = [1, 1, 0, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 2, 1, 2, 1, 1, 1, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_156():

    triu = [0, 0, 1, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [0, 1, 2, 1, 1, 1, 0, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_157():

    triu = [1, 0, 1, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [3, 2, 3, 2, 2, 2, 1, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_158():

    triu = [0, 1, 1, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [1, 2, 1, 2, 2, 1, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_159():

    triu = [1, 1, 1, 1, 1, 0, 0, 1, 0, 0]
    expected_counts = [2, 1, 2, 3, 1, 2, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_160():

    triu = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_161():

    triu = [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_162():

    triu = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_163():

    triu = [1, 1, 0, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [2, 2, 2, 0, 2, 2, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_164():

    triu = [0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 2, 0, 1, 2, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_165():

    triu = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 2, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_166():

    triu = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_167():

    triu = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 0, 0, 2, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_168():

    triu = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_169():

    triu = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [2, 0, 1, 1, 1, 2, 1, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_170():

    triu = [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [0, 2, 1, 1, 1, 1, 0, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_171():

    triu = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [3, 3, 2, 2, 2, 2, 1, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_172():

    triu = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 3, 1, 1, 2, 0, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_173():

    triu = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 2, 2, 1, 1, 1, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_174():

    triu = [0, 1, 1, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 2, 2, 1, 2, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_175():

    triu = [1, 1, 1, 1, 0, 1, 0, 1, 0, 0]
    expected_counts = [2, 2, 1, 3, 2, 1, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_176():

    triu = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_177():

    triu = [1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [2, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_178():

    triu = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 2, 1, 0, 1, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_179():

    triu = [1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 2, 0, 0, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_180():

    triu = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 2, 0, 0, 1, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_181():

    triu = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 2, 1, 0, 1, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_182():

    triu = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [2, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_183():

    triu = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_184():

    triu = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_185():

    triu = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_186():

    triu = [0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_187():

    triu = [1, 1, 0, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_188():

    triu = [0, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_189():

    triu = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_190():

    triu = [0, 1, 1, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_191():

    triu = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_192():

    triu = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_193():

    triu = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_194():

    triu = [0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_195():

    triu = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [2, 2, 1, 1, 1, 0, 1, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_196():

    triu = [0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_197():

    triu = [1, 0, 1, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [2, 1, 2, 1, 0, 1, 1, 1, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_198():

    triu = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_199():

    triu = [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_200():

    triu = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_201():

    triu = [1, 0, 0, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_202():

    triu = [0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 2, 1, 2, 0, 0, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_203():

    triu = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_204():

    triu = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 2, 2, 0, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_205():

    triu = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_206():

    triu = [0, 1, 1, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_207():

    triu = [1, 1, 1, 1, 0, 0, 1, 1, 0, 0]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_208():

    triu = [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 2, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_209():

    triu = [1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [2, 1, 0, 1, 3, 1, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_210():

    triu = [0, 1, 0, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 2, 1, 0, 3, 1, 1, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_211():

    triu = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 1, 1, 2, 1, 2, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_212():

    triu = [0, 0, 1, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 2, 1, 1, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_213():

    triu = [1, 0, 1, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [3, 2, 2, 1, 3, 2, 2, 2, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_214():

    triu = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_215():

    triu = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_216():

    triu = [0, 0, 0, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 2, 1, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_217():

    triu = [1, 0, 0, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_218():

    triu = [0, 1, 0, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [2, 3, 1, 2, 3, 1, 2, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_219():

    triu = [1, 1, 0, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_220():

    triu = [0, 0, 1, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 2, 2, 2, 1, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_221():

    triu = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [2, 2, 3, 1, 3, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_222():

    triu = [0, 1, 1, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [2, 2, 1, 3, 3, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_223():

    triu = [1, 1, 1, 1, 1, 0, 1, 1, 0, 0]
    expected_counts = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_224():

    triu = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_225():

    triu = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [2, 0, 1, 1, 1, 3, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_226():

    triu = [0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [0, 1, 1, 0, 1, 2, 1, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_227():

    triu = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [3, 2, 2, 1, 2, 3, 2, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_228():

    triu = [0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 1, 2, 0, 1, 3, 1, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_229():

    triu = [1, 0, 1, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 1, 1, 1, 1, 2, 2, 2, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_230():

    triu = [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_231():

    triu = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_232():

    triu = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 1, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_233():

    triu = [1, 0, 0, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_234():

    triu = [0, 1, 0, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 2, 1, 2, 1, 2, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_235():

    triu = [1, 1, 0, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [2, 3, 2, 1, 2, 3, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_236():

    triu = [0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 3, 2, 1, 3, 2, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_237():

    triu = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_238():

    triu = [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 2, 3, 1, 3, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_239():

    triu = [1, 1, 1, 1, 0, 1, 1, 1, 0, 0]
    expected_counts = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_240():

    triu = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_241():

    triu = [1, 0, 0, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [3, 1, 1, 1, 2, 2, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_242():

    triu = [0, 1, 0, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [1, 2, 1, 0, 2, 1, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_243():

    triu = [1, 1, 0, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 2, 1, 1, 2, 3, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_244():

    triu = [0, 0, 1, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [1, 1, 2, 0, 1, 2, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_245():

    triu = [1, 0, 1, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [2, 2, 1, 1, 2, 1, 3, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_246():

    triu = [0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_247():

    triu = [1, 1, 1, 0, 1, 1, 1, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_248():

    triu = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_249():

    triu = [1, 0, 0, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_250():

    triu = [0, 1, 0, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [2, 3, 1, 2, 2, 1, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_251():

    triu = [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [1, 2, 2, 1, 1, 2, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_252():

    triu = [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [2, 1, 3, 2, 1, 2, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_253():

    triu = [1, 0, 1, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_254():

    triu = [0, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [3, 2, 2, 3, 2, 2, 3, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_255():

    triu = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_256():

    triu = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_257():

    triu = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_258():

    triu = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_259():

    triu = [1, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [1, 2, 0, 1, 1, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_260():

    triu = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_261():

    triu = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_262():

    triu = [0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 2, 1, 1, 0, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_263():

    triu = [1, 1, 1, 0, 0, 0, 0, 0, 1, 0]
    expected_counts = [2, 3, 2, 1, 1, 1, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_264():

    triu = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_265():

    triu = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [1, 1, 0, 2, 0, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_266():

    triu = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_267():

    triu = [1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [2, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_268():

    triu = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 1, 2, 0, 0, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_269():

    triu = [1, 0, 1, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [2, 1, 2, 3, 0, 1, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_270():

    triu = [0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 2, 1, 0, 0, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_271():

    triu = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    expected_counts = [3, 2, 3, 2, 1, 1, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_272():

    triu = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_273():

    triu = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 1, 0, 0, 2, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_274():

    triu = [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 2, 0, 1, 2, 0, 1, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_275():

    triu = [1, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_276():

    triu = [0, 0, 1, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_277():

    triu = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [2, 1, 1, 0, 2, 1, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_278():

    triu = [0, 1, 1, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 3, 1, 1, 2, 0, 1, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_279():

    triu = [1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 2, 2, 1, 1, 1, 1, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_280():

    triu = [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_281():

    triu = [1, 0, 0, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [2, 2, 0, 2, 2, 0, 2, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_282():

    triu = [0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 1, 0, 0, 2, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_283():

    triu = [1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 0, 0, 1, 1, 0, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_284():

    triu = [0, 0, 1, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [0, 1, 1, 2, 1, 0, 1, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_285():

    triu = [1, 0, 1, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [3, 2, 2, 3, 2, 1, 2, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_286():

    triu = [0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [1, 2, 2, 1, 2, 0, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_287():

    triu = [1, 1, 1, 1, 1, 0, 0, 0, 1, 0]
    expected_counts = [2, 1, 3, 2, 1, 1, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_288():

    triu = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_289():

    triu = [1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_290():

    triu = [0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_291():

    triu = [1, 1, 0, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 1, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_292():

    triu = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_293():

    triu = [1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_294():

    triu = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 2, 2, 1, 0, 1, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_295():

    triu = [1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_296():

    triu = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_297():

    triu = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [2, 1, 1, 2, 0, 1, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_298():

    triu = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_299():

    triu = [1, 1, 0, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_300():

    triu = [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 2, 2, 0, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_301():

    triu = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_302():

    triu = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_303():

    triu = [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_304():

    triu = [0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 2, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_305():

    triu = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [2, 1, 1, 0, 3, 2, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_306():

    triu = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 2, 0, 1, 3, 1, 1, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_307():

    triu = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 2, 1, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_308():

    triu = [0, 0, 1, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 2, 2, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_309():

    triu = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_310():

    triu = [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [2, 3, 2, 1, 3, 2, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_311():

    triu = [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_312():

    triu = [0, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 2, 1, 1, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_313():

    triu = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [3, 2, 1, 2, 3, 2, 2, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_314():

    triu = [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_315():

    triu = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_316():

    triu = [0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_317():

    triu = [1, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [2, 2, 1, 3, 3, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_318():

    triu = [0, 1, 1, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [2, 2, 3, 1, 3, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_319():

    triu = [1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
    expected_counts = [1, 1, 2, 2, 2, 1, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_320():

    triu = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_321():

    triu = [1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 0, 0, 1, 1, 0, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_322():

    triu = [0, 1, 0, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_323():

    triu = [1, 1, 0, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [2, 2, 0, 2, 2, 0, 2, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_324():

    triu = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_325():

    triu = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [2, 0, 1, 1, 1, 1, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_326():

    triu = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [0, 2, 1, 1, 1, 0, 1, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_327():

    triu = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]
    expected_counts = [3, 3, 2, 2, 2, 1, 2, 1, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_328():

    triu = [0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 0, 2, 1, 0, 2, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_329():

    triu = [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 0, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_330():

    triu = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 0, 0, 1, 1, 0, 2, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_331():

    triu = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 0, 0, 2, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_332():

    triu = [0, 0, 1, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 1, 3, 1, 0, 2, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_333():

    triu = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 2, 2, 1, 1, 1, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_334():

    triu = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 2, 2, 1, 0, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_335():

    triu = [1, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    expected_counts = [2, 2, 3, 1, 2, 1, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_336():

    triu = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_337():

    triu = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [2, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_338():

    triu = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 2, 0, 1, 1, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_339():

    triu = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 0, 2, 0, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_340():

    triu = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_341():

    triu = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_342():

    triu = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_343():

    triu = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_344():

    triu = [0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 0, 2, 0, 0, 1, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_345():

    triu = [1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 2, 0, 1, 1, 0, 0, 0, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_346():

    triu = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [2, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_347():

    triu = [1, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_348():

    triu = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_349():

    triu = [1, 0, 1, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_350():

    triu = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_351():

    triu = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_352():

    triu = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_353():

    triu = [1, 0, 0, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [2, 0, 1, 1, 1, 2, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_354():

    triu = [0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 1, 2, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_355():

    triu = [1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [3, 2, 1, 2, 2, 2, 3, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_356():

    triu = [0, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_357():

    triu = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_358():

    triu = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 2, 2, 1, 1, 2, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_359():

    triu = [1, 1, 1, 0, 0, 1, 1, 0, 1, 0]
    expected_counts = [2, 3, 1, 2, 2, 1, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_360():

    triu = [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 1, 0, 2, 1, 1, 3, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_361():

    triu = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 1, 1, 1, 1, 2, 2, 0, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_362():

    triu = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_363():

    triu = [1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_364():

    triu = [0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 2, 3, 1, 2, 3, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_365():

    triu = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_366():

    triu = [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 3, 2, 1, 2, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_367():

    triu = [1, 1, 1, 1, 0, 1, 1, 0, 1, 0]
    expected_counts = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_368():

    triu = [0, 0, 0, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_369():

    triu = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [3, 1, 1, 1, 2, 3, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_370():

    triu = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [1, 2, 0, 1, 2, 2, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_371():

    triu = [1, 1, 0, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 1, 2, 1, 3, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_372():

    triu = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_373():

    triu = [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_374():

    triu = [0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [2, 3, 2, 1, 2, 3, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_375():

    triu = [1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    expected_counts = [1, 2, 1, 2, 1, 2, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_376():

    triu = [0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [1, 1, 0, 2, 1, 2, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_377():

    triu = [1, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [2, 2, 1, 1, 2, 3, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_378():

    triu = [0, 1, 0, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_379():

    triu = [1, 1, 0, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_380():

    triu = [0, 0, 1, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [2, 1, 2, 3, 1, 3, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_381():

    triu = [1, 0, 1, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_382():

    triu = [0, 1, 1, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [3, 2, 3, 2, 2, 3, 2, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_383():

    triu = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_384():

    triu = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_385():

    triu = [1, 0, 0, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_386():

    triu = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 2, 1, 1, 0, 0, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_387():

    triu = [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_388():

    triu = [0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_389():

    triu = [1, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [1, 1, 2, 0, 0, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_390():

    triu = [0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_391():

    triu = [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 1, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_392():

    triu = [0, 0, 0, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_393():

    triu = [1, 0, 0, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [1, 1, 0, 2, 0, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_394():

    triu = [0, 1, 0, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_395():

    triu = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 0, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_396():

    triu = [0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 2, 2, 2, 0, 0, 0, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_397():

    triu = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [2, 2, 3, 3, 0, 1, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_398():

    triu = [0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_399():

    triu = [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]
    expected_counts = [3, 1, 2, 2, 1, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_400():

    triu = [0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 2, 1, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_401():

    triu = [1, 0, 0, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_402():

    triu = [0, 1, 0, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 3, 1, 1, 3, 1, 1, 3, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_403():

    triu = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 3, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_404():

    triu = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 2, 1, 1, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_405():

    triu = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [2, 2, 2, 0, 3, 2, 1, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_406():

    triu = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 2, 0, 1, 3, 1, 1, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_407():

    triu = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 2, 1, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_408():

    triu = [0, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 2, 1, 1, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_409():

    triu = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [2, 2, 0, 2, 3, 1, 2, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_410():

    triu = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 2, 1, 0, 3, 1, 1, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_411():

    triu = [1, 1, 0, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 1, 2, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_412():

    triu = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [0, 2, 2, 2, 2, 1, 1, 3, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_413():

    triu = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [3, 3, 3, 3, 3, 2, 2, 3, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_414():

    triu = [0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 3, 1, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_415():

    triu = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    expected_counts = [2, 0, 2, 2, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_416():

    triu = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_417():

    triu = [1, 0, 0, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 0, 1, 0, 1, 2, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_418():

    triu = [0, 1, 0, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [0, 2, 1, 1, 1, 1, 0, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_419():

    triu = [1, 1, 0, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [2, 3, 2, 1, 2, 2, 0, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_420():

    triu = [0, 0, 1, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 1, 2, 0, 1, 2, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_421():

    triu = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_422():

    triu = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 1, 2, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_423():

    triu = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_424():

    triu = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_425():

    triu = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_426():

    triu = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_427():

    triu = [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [3, 2, 2, 1, 2, 2, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_428():

    triu = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 3, 2, 1, 2, 0, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_429():

    triu = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 2, 3, 1, 1, 1, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_430():

    triu = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_431():

    triu = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_432():

    triu = [0, 0, 0, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_433():

    triu = [1, 0, 0, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [2, 1, 1, 0, 2, 1, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_434():

    triu = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 3, 1, 1, 2, 0, 1, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_435():

    triu = [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 2, 1, 1, 1, 1, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_436():

    triu = [0, 0, 1, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 1, 2, 0, 1, 1, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_437():

    triu = [1, 0, 1, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_438():

    triu = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 2, 1, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_439():

    triu = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_440():

    triu = [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_441():

    triu = [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [3, 2, 1, 2, 2, 1, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_442():

    triu = [0, 1, 0, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_443():

    triu = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_444():

    triu = [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 2, 3, 2, 1, 1, 1, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_445():

    triu = [1, 0, 1, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [2, 3, 2, 3, 2, 0, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_446():

    triu = [0, 1, 1, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_447():

    triu = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_448():

    triu = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_449():

    triu = [1, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 0, 0, 1, 1, 0, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_450():

    triu = [0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [0, 2, 1, 1, 1, 0, 1, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_451():

    triu = [1, 1, 0, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [2, 3, 1, 2, 2, 0, 2, 2, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_452():

    triu = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 1, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_453():

    triu = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_454():

    triu = [0, 1, 1, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_455():

    triu = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
    expected_counts = [3, 2, 1, 2, 2, 1, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_456():

    triu = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 1, 0, 2, 1, 0, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_457():

    triu = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_458():

    triu = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 1, 0, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_459():

    triu = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_460():

    triu = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 2, 3, 1, 0, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_461():

    triu = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 3, 2, 1, 1, 1, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_462():

    triu = [0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_463():

    triu = [1, 1, 1, 1, 0, 0, 1, 1, 1, 0]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_464():

    triu = [0, 0, 0, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_465():

    triu = [1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [2, 1, 0, 1, 2, 1, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_466():

    triu = [0, 1, 0, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 3, 1, 1, 2, 1, 0, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_467():

    triu = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 1, 2, 1, 1, 1, 3, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_468():

    triu = [0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_469():

    triu = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [3, 2, 2, 1, 2, 2, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_470():

    triu = [0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_471():

    triu = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_472():

    triu = [0, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 1, 0, 2, 1, 1, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_473():

    triu = [1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_474():

    triu = [0, 1, 0, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 2, 1, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_475():

    triu = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_476():

    triu = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 2, 2, 3, 1, 1, 1, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_477():

    triu = [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [2, 3, 3, 2, 2, 2, 0, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_478():

    triu = [0, 1, 1, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_479():

    triu = [1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_480():

    triu = [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_481():

    triu = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [2, 0, 1, 1, 2, 3, 3, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_482():

    triu = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [0, 2, 1, 1, 2, 2, 2, 3, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_483():

    triu = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [3, 3, 2, 2, 3, 3, 3, 3, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_484():

    triu = [0, 0, 1, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 2, 0, 2, 3, 2, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_485():

    triu = [1, 0, 1, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 2, 3, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_486():

    triu = [0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 3, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_487():

    triu = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 0, 2, 3, 2, 3, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_488():

    triu = [0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 0, 2, 2, 2, 3, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_489():

    triu = [1, 0, 0, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 3, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_490():

    triu = [0, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 2, 2, 3, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_491():

    triu = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 2, 0, 3, 3, 2, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_492():

    triu = [0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 3, 3, 2, 3, 3, 3, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_493():

    triu = [1, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [0, 2, 2, 2, 2, 2, 2, 3, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_494():

    triu = [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [2, 0, 2, 2, 2, 3, 3, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_495():

    triu = [1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 1, 1, 3, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_496():

    triu = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_497():

    triu = [1, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [3, 1, 1, 1, 1, 2, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_498():

    triu = [0, 1, 0, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [1, 3, 1, 1, 1, 1, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_499():

    triu = [1, 1, 0, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 2, 2, 0, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_500():

    triu = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_501():

    triu = [1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_502():

    triu = [0, 1, 1, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_503():

    triu = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_504():

    triu = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_505():

    triu = [1, 0, 0, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_506():

    triu = [0, 1, 0, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_507():

    triu = [1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_508():

    triu = [0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [2, 2, 3, 3, 0, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_509():

    triu = [1, 0, 1, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [1, 3, 2, 2, 1, 1, 1, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_510():

    triu = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [3, 1, 2, 2, 1, 2, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_511():

    triu = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_512():

    triu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_513():

    triu = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_514():

    triu = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_515():

    triu = [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_516():

    triu = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_517():

    triu = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [1, 0, 2, 1, 0, 1, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_518():

    triu = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 1, 2, 1, 0, 0, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_519():

    triu = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1]
    expected_counts = [2, 2, 3, 1, 1, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_520():

    triu = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_521():

    triu = [1, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [1, 0, 1, 2, 0, 0, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_522():

    triu = [0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 1, 1, 2, 0, 0, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_523():

    triu = [1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [2, 2, 1, 3, 1, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_524():

    triu = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_525():

    triu = [1, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [2, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_526():

    triu = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [0, 2, 1, 1, 0, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_527():

    triu = [1, 1, 1, 1, 0, 0, 0, 0, 0, 1]
    expected_counts = [3, 3, 2, 2, 1, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_528():

    triu = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_529():

    triu = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_530():

    triu = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_531():

    triu = [1, 1, 0, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_532():

    triu = [0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_533():

    triu = [1, 0, 1, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [2, 1, 2, 1, 1, 1, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_534():

    triu = [0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 2, 2, 1, 1, 0, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_535():

    triu = [1, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_536():

    triu = [0, 0, 0, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_537():

    triu = [1, 0, 0, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [2, 1, 1, 2, 1, 0, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_538():

    triu = [0, 1, 0, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 2, 1, 2, 1, 0, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_539():

    triu = [1, 1, 0, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_540():

    triu = [0, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_541():

    triu = [1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_542():

    triu = [0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_543():

    triu = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_544():

    triu = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_545():

    triu = [1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 1, 0, 0, 2, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_546():

    triu = [0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_547():

    triu = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [2, 1, 1, 0, 1, 2, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_548():

    triu = [0, 0, 1, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 2, 1, 0, 2, 1, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_549():

    triu = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_550():

    triu = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 1, 3, 1, 0, 2, 1, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_551():

    triu = [1, 1, 1, 0, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 2, 2, 1, 1, 1, 1, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_552():

    triu = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_553():

    triu = [1, 0, 0, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [2, 0, 2, 2, 0, 2, 2, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_554():

    triu = [0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [0, 1, 1, 2, 0, 1, 1, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_555():

    triu = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [3, 2, 2, 3, 1, 2, 2, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_556():

    triu = [0, 0, 1, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 1, 0, 0, 2, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_557():

    triu = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 0, 1, 0, 1, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_558():

    triu = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [1, 2, 2, 1, 0, 2, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_559():

    triu = [1, 1, 1, 1, 0, 1, 0, 0, 0, 1]
    expected_counts = [2, 3, 1, 2, 1, 1, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_560():

    triu = [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 1, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_561():

    triu = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [2, 1, 1, 0, 2, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_562():

    triu = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 2, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_563():

    triu = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_564():

    triu = [0, 0, 1, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 2, 1, 1, 3, 1, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_565():

    triu = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 2, 1, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_566():

    triu = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [2, 2, 3, 1, 2, 3, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_567():

    triu = [1, 1, 1, 0, 1, 1, 0, 0, 0, 1]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_568():

    triu = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 1, 2, 1, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_569():

    triu = [1, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [3, 1, 2, 2, 2, 3, 2, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_570():

    triu = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_571():

    triu = [1, 1, 0, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [2, 1, 2, 3, 1, 3, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_572():

    triu = [0, 0, 1, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_573():

    triu = [1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_574():

    triu = [0, 1, 1, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [2, 3, 2, 1, 2, 3, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_575():

    triu = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
    expected_counts = [1, 2, 1, 2, 1, 2, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_576():

    triu = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_577():

    triu = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 0, 1, 0, 1, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_578():

    triu = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_579():

    triu = [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [2, 1, 0, 1, 1, 1, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_580():

    triu = [0, 0, 1, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_581():

    triu = [1, 0, 1, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [2, 0, 2, 2, 0, 2, 2, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_582():

    triu = [0, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [0, 1, 2, 1, 0, 1, 1, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_583():

    triu = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    expected_counts = [3, 2, 3, 2, 1, 2, 2, 1, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_584():

    triu = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 1, 2, 0, 1, 2, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_585():

    triu = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 0, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_586():

    triu = [0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 1, 1, 3, 0, 1, 2, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_587():

    triu = [1, 1, 0, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 2, 1, 2, 1, 1, 1, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_588():

    triu = [0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 0, 1, 0, 1, 2, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_589():

    triu = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 1, 0, 0, 2, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_590():

    triu = [0, 1, 1, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [1, 2, 1, 2, 0, 1, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_591():

    triu = [1, 1, 1, 1, 0, 0, 1, 0, 0, 1]
    expected_counts = [2, 3, 2, 1, 1, 2, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_592():

    triu = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_593():

    triu = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [2, 1, 0, 1, 2, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_594():

    triu = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 2, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_595():

    triu = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_596():

    triu = [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [0, 0, 1, 1, 1, 1, 2, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_597():

    triu = [1, 0, 1, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [3, 1, 2, 2, 2, 2, 3, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_598():

    triu = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_599():

    triu = [1, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    expected_counts = [2, 1, 3, 2, 1, 2, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_600():

    triu = [0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 1, 2, 1, 1, 3, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_601():

    triu = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 1, 2, 0, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_602():

    triu = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [2, 2, 1, 3, 2, 1, 3, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_603():

    triu = [1, 1, 0, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_604():

    triu = [0, 0, 1, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_605():

    triu = [1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_606():

    triu = [0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [2, 3, 1, 2, 2, 1, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_607():

    triu = [1, 1, 1, 1, 1, 0, 1, 0, 0, 1]
    expected_counts = [1, 2, 2, 1, 1, 2, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_608():

    triu = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_609():

    triu = [1, 0, 0, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [2, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_610():

    triu = [0, 1, 0, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_611():

    triu = [1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_612():

    triu = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 0, 2, 1, 0, 1, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_613():

    triu = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 0, 1, 2, 0, 0, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_614():

    triu = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_615():

    triu = [1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_616():

    triu = [0, 0, 0, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 0, 1, 2, 0, 0, 1, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_617():

    triu = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 0, 2, 1, 0, 1, 0, 0, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_618():

    triu = [0, 1, 0, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_619():

    triu = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_620():

    triu = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [2, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_621():

    triu = [1, 0, 1, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_622():

    triu = [0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_623():

    triu = [1, 1, 1, 1, 0, 1, 1, 0, 0, 1]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_624():

    triu = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [0, 0, 0, 0, 2, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_625():

    triu = [1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [3, 1, 1, 1, 3, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_626():

    triu = [0, 1, 0, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_627():

    triu = [1, 1, 0, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_628():

    triu = [0, 0, 1, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [1, 0, 2, 1, 2, 2, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_629():

    triu = [1, 0, 1, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [2, 1, 1, 2, 3, 1, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_630():

    triu = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [2, 2, 3, 1, 3, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_631():

    triu = [1, 1, 1, 0, 1, 1, 1, 0, 0, 1]
    expected_counts = [1, 1, 2, 2, 2, 1, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_632():

    triu = [0, 0, 0, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [1, 0, 1, 2, 2, 1, 2, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_633():

    triu = [1, 0, 0, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [2, 1, 2, 1, 3, 2, 1, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_634():

    triu = [0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [2, 2, 1, 3, 3, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_635():

    triu = [1, 1, 0, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_636():

    triu = [0, 0, 1, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_637():

    triu = [1, 0, 1, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_638():

    triu = [0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [3, 3, 2, 2, 3, 2, 2, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_639():

    triu = [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_640():

    triu = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_641():

    triu = [1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_642():

    triu = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_643():

    triu = [1, 1, 0, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [1, 2, 1, 0, 1, 0, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_644():

    triu = [0, 0, 1, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 2, 1, 0, 0, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_645():

    triu = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_646():

    triu = [0, 1, 1, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_647():

    triu = [1, 1, 1, 0, 0, 0, 0, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 1, 1, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_648():

    triu = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_649():

    triu = [1, 0, 0, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [1, 0, 1, 2, 0, 0, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_650():

    triu = [0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 2, 2, 2, 0, 0, 0, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_651():

    triu = [1, 1, 0, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [2, 3, 2, 3, 1, 0, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_652():

    triu = [0, 0, 1, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_653():

    triu = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 0, 1, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_654():

    triu = [0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_655():

    triu = [1, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    expected_counts = [3, 2, 1, 2, 1, 1, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_656():

    triu = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_657():

    triu = [1, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 1, 0, 0, 2, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_658():

    triu = [0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 2, 1, 0, 2, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_659():

    triu = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_660():

    triu = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 2, 1, 1, 1, 0, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_661():

    triu = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [2, 2, 3, 1, 2, 2, 0, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_662():

    triu = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 1, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_663():

    triu = [1, 1, 1, 0, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_664():

    triu = [0, 0, 0, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 1, 1, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_665():

    triu = [1, 0, 0, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_666():

    triu = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 3, 2, 2, 2, 1, 0, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_667():

    triu = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 2, 2, 3, 1, 1, 1, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_668():

    triu = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_669():

    triu = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [3, 2, 2, 1, 2, 2, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_670():

    triu = [0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_671():

    triu = [1, 1, 1, 1, 1, 0, 0, 1, 0, 1]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_672():

    triu = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 1, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_673():

    triu = [1, 0, 0, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_674():

    triu = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 1, 2, 1, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_675():

    triu = [1, 1, 0, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [2, 2, 2, 0, 2, 3, 1, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_676():

    triu = [0, 0, 1, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 3, 1, 1, 3, 1, 3, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_677():

    triu = [1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 3, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_678():

    triu = [0, 1, 1, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 0, 2, 1, 1, 3, 1, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_679():

    triu = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 2, 1, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_680():

    triu = [0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 1, 2, 1, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_681():

    triu = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [2, 0, 2, 2, 1, 3, 2, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_682():

    triu = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [0, 2, 2, 2, 1, 2, 1, 3, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_683():

    triu = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [3, 3, 3, 3, 2, 3, 2, 3, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_684():

    triu = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 2, 0, 1, 3, 1, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_685():

    triu = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 1, 2, 2, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_686():

    triu = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 1, 3, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_687():

    triu = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1]
    expected_counts = [2, 2, 0, 2, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_688():

    triu = [0, 0, 0, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_689():

    triu = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [2, 1, 1, 0, 1, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_690():

    triu = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 2, 1, 0, 1, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_691():

    triu = [1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_692():

    triu = [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 3, 1, 0, 2, 1, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_693():

    triu = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 2, 2, 1, 1, 1, 1, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_694():

    triu = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 1, 2, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_695():

    triu = [1, 1, 1, 0, 1, 1, 0, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_696():

    triu = [0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_697():

    triu = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [3, 1, 2, 2, 1, 2, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_698():

    triu = [0, 1, 0, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 3, 2, 2, 1, 1, 1, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_699():

    triu = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [2, 2, 3, 3, 0, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_700():

    triu = [0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_701():

    triu = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_702():

    triu = [0, 1, 1, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_703():

    triu = [1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_704():

    triu = [0, 0, 0, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_705():

    triu = [1, 0, 0, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 0, 0, 1, 0, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_706():

    triu = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 0, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_707():

    triu = [1, 1, 0, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_708():

    triu = [0, 0, 1, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [0, 1, 2, 1, 0, 1, 1, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_709():

    triu = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [2, 1, 3, 2, 0, 2, 2, 2, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_710():

    triu = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_711():

    triu = [1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    expected_counts = [3, 1, 2, 2, 1, 2, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_712():

    triu = [0, 0, 0, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 0, 1, 2, 0, 1, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_713():

    triu = [1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_714():

    triu = [0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 2, 2, 3, 0, 1, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_715():

    triu = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 3, 2, 2, 1, 1, 1, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_716():

    triu = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 0, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_717():

    triu = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_718():

    triu = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_719():

    triu = [1, 1, 1, 1, 0, 0, 1, 1, 0, 1]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_720():

    triu = [0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_721():

    triu = [1, 0, 0, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [2, 1, 0, 1, 3, 2, 3, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_722():

    triu = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 2, 1, 0, 3, 2, 2, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_723():

    triu = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 2, 3, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_724():

    triu = [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [0, 1, 2, 1, 2, 2, 2, 3, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_725():

    triu = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [3, 2, 3, 2, 3, 3, 3, 3, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_726():

    triu = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 3, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_727():

    triu = [1, 1, 1, 0, 1, 0, 1, 1, 0, 1]
    expected_counts = [2, 0, 2, 2, 2, 3, 3, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_728():

    triu = [0, 0, 0, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 0, 1, 2, 2, 2, 3, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_729():

    triu = [1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 3, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_730():

    triu = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [2, 3, 2, 3, 3, 2, 3, 3, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_731():

    triu = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [0, 2, 2, 2, 2, 2, 2, 3, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_732():

    triu = [0, 0, 1, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 2, 3, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_733():

    triu = [1, 0, 1, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [2, 2, 2, 0, 3, 3, 2, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_734():

    triu = [0, 1, 1, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [2, 2, 0, 2, 3, 2, 3, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_735():

    triu = [1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
    expected_counts = [1, 1, 1, 1, 2, 3, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_736():

    triu = [0, 0, 0, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_737():

    triu = [1, 0, 0, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [2, 0, 1, 1, 1, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_738():

    triu = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_739():

    triu = [1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [3, 2, 2, 1, 2, 2, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_740():

    triu = [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 1, 3, 1, 1, 2, 0, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_741():

    triu = [1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 1, 2, 2, 1, 1, 1, 3, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_742():

    triu = [0, 1, 1, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_743():

    triu = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_744():

    triu = [0, 0, 0, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 0, 1, 2, 1, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_745():

    triu = [1, 0, 0, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_746():

    triu = [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 2, 2, 3, 1, 1, 1, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_747():

    triu = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [2, 3, 3, 2, 2, 2, 0, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_748():

    triu = [0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 1, 2, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_749():

    triu = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_750():

    triu = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_751():

    triu = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_752():

    triu = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_753():

    triu = [1, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [3, 1, 1, 1, 2, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_754():

    triu = [0, 1, 0, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_755():

    triu = [1, 1, 0, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_756():

    triu = [0, 0, 1, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [1, 1, 3, 1, 1, 1, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_757():

    triu = [1, 0, 1, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [2, 2, 2, 2, 2, 0, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_758():

    triu = [0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_759():

    triu = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_760():

    triu = [0, 0, 0, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_761():

    triu = [1, 0, 0, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_762():

    triu = [0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [2, 3, 2, 3, 2, 0, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_763():

    triu = [1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [1, 2, 3, 2, 1, 1, 1, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_764():

    triu = [0, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_765():

    triu = [1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_766():

    triu = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [3, 2, 1, 2, 2, 1, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_767():

    triu = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_768():

    triu = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_769():

    triu = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_770():

    triu = [0, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_771():

    triu = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [1, 2, 0, 1, 1, 0, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_772():

    triu = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_773():

    triu = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [1, 0, 2, 1, 0, 1, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_774():

    triu = [0, 1, 1, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 2, 2, 2, 0, 0, 0, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_775():

    triu = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
    expected_counts = [2, 3, 3, 2, 1, 1, 0, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_776():

    triu = [0, 0, 0, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 1, 2, 0, 0, 0, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_777():

    triu = [1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_778():

    triu = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 0, 0, 0, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_779():

    triu = [1, 1, 0, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 1, 0, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_780():

    triu = [0, 0, 1, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 0, 0, 0, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_781():

    triu = [1, 0, 1, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 0, 1, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_782():

    triu = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 1, 0, 0, 0, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_783():

    triu = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    expected_counts = [3, 2, 2, 1, 1, 1, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_784():

    triu = [0, 0, 0, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_785():

    triu = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 1, 0, 0, 2, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_786():

    triu = [0, 1, 0, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 2, 0, 1, 2, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_787():

    triu = [1, 1, 0, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_788():

    triu = [0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 1, 0, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_789():

    triu = [1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_790():

    triu = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 3, 2, 2, 2, 0, 1, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_791():

    triu = [1, 1, 1, 0, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 2, 3, 2, 1, 1, 1, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_792():

    triu = [0, 0, 0, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 0, 1, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_793():

    triu = [1, 0, 0, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [2, 2, 1, 3, 2, 0, 2, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_794():

    triu = [0, 1, 0, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 2, 0, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_795():

    triu = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_796():

    triu = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_797():

    triu = [1, 0, 1, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [3, 2, 1, 2, 2, 1, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_798():

    triu = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_799():

    triu = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_800():

    triu = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_801():

    triu = [1, 0, 0, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 0, 1, 0, 0, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_802():

    triu = [0, 1, 0, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 0, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_803():

    triu = [1, 1, 0, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_804():

    triu = [0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 0, 2, 1, 0, 2, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_805():

    triu = [1, 0, 1, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_806():

    triu = [0, 1, 1, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 2, 3, 2, 0, 2, 1, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_807():

    triu = [1, 1, 1, 0, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 3, 2, 2, 1, 1, 1, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_808():

    triu = [0, 0, 0, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [0, 1, 1, 2, 0, 1, 1, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_809():

    triu = [1, 0, 0, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [2, 1, 2, 3, 0, 2, 2, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_810():

    triu = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_811():

    triu = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [3, 1, 2, 2, 1, 2, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_812():

    triu = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 0, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_813():

    triu = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_814():

    triu = [0, 1, 1, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_815():

    triu = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_816():

    triu = [0, 0, 0, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_817():

    triu = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [2, 1, 1, 0, 3, 3, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_818():

    triu = [0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 2, 0, 1, 3, 2, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_819():

    triu = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 2, 3, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_820():

    triu = [0, 0, 1, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 0, 2, 1, 2, 3, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_821():

    triu = [1, 0, 1, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 3, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_822():

    triu = [0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [2, 3, 3, 2, 3, 3, 2, 3, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_823():

    triu = [1, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    expected_counts = [0, 2, 2, 2, 2, 2, 2, 3, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_824():

    triu = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [0, 1, 1, 2, 2, 2, 2, 2, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_825():

    triu = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [3, 2, 2, 3, 3, 3, 3, 2, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_826():

    triu = [0, 1, 0, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 3, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_827():

    triu = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [2, 0, 2, 2, 2, 3, 3, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_828():

    triu = [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 2, 3, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_829():

    triu = [1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [2, 2, 0, 2, 3, 2, 3, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_830():

    triu = [0, 1, 1, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [2, 2, 2, 0, 3, 3, 2, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_831():

    triu = [1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 2, 2, 3, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_832():

    triu = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_833():

    triu = [1, 0, 0, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_834():

    triu = [0, 1, 0, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 1, 1, 2, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_835():

    triu = [1, 1, 0, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [2, 2, 0, 2, 2, 1, 3, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_836():

    triu = [0, 0, 1, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 1, 1, 2, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_837():

    triu = [1, 0, 1, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [2, 0, 2, 2, 1, 2, 3, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_838():

    triu = [0, 1, 1, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [0, 2, 2, 2, 1, 1, 2, 2, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_839():

    triu = [1, 1, 1, 0, 0, 0, 1, 0, 1, 1]
    expected_counts = [3, 3, 3, 3, 2, 2, 3, 2, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_840():

    triu = [0, 0, 0, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_841():

    triu = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 1, 3, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_842():

    triu = [0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 0, 1, 2, 1, 1, 3, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_843():

    triu = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 2, 1, 2, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_844():

    triu = [0, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 0, 2, 1, 1, 3, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_845():

    triu = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 1, 2, 2, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_846():

    triu = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 1, 1, 1, 3, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_847():

    triu = [1, 1, 1, 1, 0, 0, 1, 0, 1, 1]
    expected_counts = [2, 2, 2, 0, 2, 2, 2, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_848():

    triu = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_849():

    triu = [1, 0, 0, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [2, 1, 0, 1, 1, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_850():

    triu = [0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 2, 0, 1, 1, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_851():

    triu = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_852():

    triu = [0, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_853():

    triu = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [3, 1, 2, 2, 1, 2, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_854():

    triu = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 3, 2, 2, 1, 1, 1, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_855():

    triu = [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    expected_counts = [2, 2, 3, 3, 0, 2, 2, 2, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_856():

    triu = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 3, 0, 1, 2, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_857():

    triu = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 2, 1, 2, 1, 1, 1, 1, 2, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_858():

    triu = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 1, 1, 2, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_859():

    triu = [1, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [0, 0, 1, 1, 0, 1, 1, 1, 1, 3]
    assert matches_count_windels(triu, 1, expected_counts)


def test_860():

    triu = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 0, 2, 0, 1, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_861():

    triu = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_862():

    triu = [0, 1, 1, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [2, 2, 1, 1, 1, 1, 2, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_863():

    triu = [1, 1, 1, 1, 1, 0, 1, 0, 1, 1]
    expected_counts = [1, 1, 2, 0, 0, 2, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_864():

    triu = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 0, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_865():

    triu = [1, 0, 0, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [2, 0, 1, 1, 1, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_866():

    triu = [0, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_867():

    triu = [1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [3, 2, 1, 2, 2, 1, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_868():

    triu = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 0, 2, 1, 1, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_869():

    triu = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_870():

    triu = [0, 1, 1, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 2, 3, 2, 1, 1, 1, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_871():

    triu = [1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
    expected_counts = [2, 3, 2, 3, 2, 0, 2, 2, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_872():

    triu = [0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 3, 1, 0, 2, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_873():

    triu = [1, 0, 0, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 1, 2, 2, 1, 1, 1, 1, 3, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_874():

    triu = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 0, 1, 2, 1, 0, 2, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_875():

    triu = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 2, 1, 2, 1, 1, 1, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_876():

    triu = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 1, 1, 2, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_877():

    triu = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [0, 1, 0, 1, 1, 0, 1, 1, 3, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_878():

    triu = [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_879():

    triu = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1]
    expected_counts = [1, 2, 1, 0, 2, 0, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_880():

    triu = [0, 0, 0, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 0, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_881():

    triu = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [3, 1, 1, 1, 2, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_882():

    triu = [0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_883():

    triu = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_884():

    triu = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_885():

    triu = [1, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_886():

    triu = [0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [2, 3, 3, 2, 2, 2, 0, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_887():

    triu = [1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
    expected_counts = [1, 2, 2, 3, 1, 1, 1, 3, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_888():

    triu = [0, 0, 0, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [1, 1, 1, 3, 1, 1, 1, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_889():

    triu = [1, 0, 0, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [2, 2, 2, 2, 2, 2, 0, 2, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_890():

    triu = [0, 1, 0, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 2, 1, 1, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_891():

    triu = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [1, 0, 2, 1, 1, 2, 0, 2, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_892():

    triu = [0, 0, 1, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [2, 1, 1, 2, 1, 2, 1, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_893():

    triu = [1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [1, 2, 0, 1, 2, 1, 0, 2, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_894():

    triu = [0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [3, 2, 2, 1, 2, 2, 1, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_895():

    triu = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    expected_counts = [0, 1, 1, 0, 1, 1, 0, 3, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_896():

    triu = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_897():

    triu = [1, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_898():

    triu = [0, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 0, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_899():

    triu = [1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_900():

    triu = [0, 0, 1, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 0, 0, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_901():

    triu = [1, 0, 1, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_902():

    triu = [0, 1, 1, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 0, 0, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_903():

    triu = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_904():

    triu = [0, 0, 0, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 0, 0, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_905():

    triu = [1, 0, 0, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_906():

    triu = [0, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 0, 0, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_907():

    triu = [1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_908():

    triu = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 0, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_909():

    triu = [1, 0, 1, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_910():

    triu = [0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_911():

    triu = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_912():

    triu = [0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 2, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_913():

    triu = [1, 0, 0, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_914():

    triu = [0, 1, 0, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 3, 1, 1, 3, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_915():

    triu = [1, 1, 0, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_916():

    triu = [0, 0, 1, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 2, 1, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_917():

    triu = [1, 0, 1, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [2, 2, 3, 1, 3, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_918():

    triu = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 3, 1, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_919():

    triu = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_920():

    triu = [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 2, 1, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_921():

    triu = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [2, 2, 1, 3, 3, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_922():

    triu = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 3, 1, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_923():

    triu = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 2, 1, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_924():

    triu = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_925():

    triu = [1, 0, 1, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [3, 3, 2, 2, 3, 2, 2, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_926():

    triu = [0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_927():

    triu = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_928():

    triu = [0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_929():

    triu = [1, 0, 0, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_930():

    triu = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 1, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_931():

    triu = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [2, 3, 2, 1, 2, 3, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_932():

    triu = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 1, 3, 1, 1, 3, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_933():

    triu = [1, 0, 1, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_934():

    triu = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 1, 3, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_935():

    triu = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_936():

    triu = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_937():

    triu = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [2, 1, 2, 3, 1, 3, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_938():

    triu = [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_939():

    triu = [1, 1, 0, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [3, 2, 3, 2, 2, 3, 2, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_940():

    triu = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 1, 3, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_941():

    triu = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 1, 2, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_942():

    triu = [0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_943():

    triu = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_944():

    triu = [0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_945():

    triu = [1, 0, 0, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_946():

    triu = [0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 3, 1, 1, 2, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_947():

    triu = [1, 1, 0, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 1, 2, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_948():

    triu = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 1, 3, 1, 1, 2, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_949():

    triu = [1, 0, 1, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_950():

    triu = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_951():

    triu = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_952():

    triu = [0, 0, 0, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_953():

    triu = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [3, 2, 2, 3, 2, 2, 3, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_954():

    triu = [0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_955():

    triu = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [2, 1, 3, 2, 1, 2, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_956():

    triu = [0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 1, 2, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_957():

    triu = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [2, 3, 1, 2, 2, 1, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_958():

    triu = [0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_959():

    triu = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_960():

    triu = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 1, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_961():

    triu = [1, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_962():

    triu = [0, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 1, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_963():

    triu = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [2, 3, 1, 2, 2, 1, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_964():

    triu = [0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 1, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_965():

    triu = [1, 0, 1, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [2, 1, 3, 2, 1, 2, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_966():

    triu = [0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_967():

    triu = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    expected_counts = [3, 2, 2, 3, 2, 2, 3, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_968():

    triu = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 1, 1, 3, 1, 1, 3, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_969():

    triu = [1, 0, 0, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [0, 1, 1, 2, 1, 1, 2, 0, 2, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_970():

    triu = [0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 1, 1, 3, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_971():

    triu = [1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_972():

    triu = [0, 0, 1, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 1, 1, 3, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_973():

    triu = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 2, 1, 1, 2, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_974():

    triu = [0, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [1, 0, 0, 1, 1, 1, 3, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_975():

    triu = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    expected_counts = [2, 1, 1, 0, 2, 2, 2, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_976():

    triu = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 1, 2, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_977():

    triu = [1, 0, 0, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_978():

    triu = [0, 1, 0, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 3, 1, 1, 2, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_979():

    triu = [1, 1, 0, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 1, 2, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_980():

    triu = [0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_981():

    triu = [1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [3, 2, 3, 2, 2, 3, 2, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_982():

    triu = [0, 1, 1, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_983():

    triu = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
    expected_counts = [2, 1, 2, 3, 1, 3, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_984():

    triu = [0, 0, 0, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 1, 1, 3, 1, 2, 2, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_985():

    triu = [1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_986():

    triu = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_987():

    triu = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [0, 1, 2, 1, 1, 2, 1, 2, 0, 2]
    assert matches_count_windels(triu, 1, expected_counts)


def test_988():

    triu = [0, 0, 1, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 2, 1, 2, 1, 2, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_989():

    triu = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [2, 3, 2, 1, 2, 3, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_990():

    triu = [0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [2, 1, 0, 1, 2, 2, 2, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_991():

    triu = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    expected_counts = [1, 0, 1, 0, 1, 3, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_992():

    triu = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 2, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_993():

    triu = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_994():

    triu = [0, 1, 0, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_995():

    triu = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [3, 3, 2, 2, 3, 2, 2, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_996():

    triu = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 3, 1, 2, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_997():

    triu = [1, 0, 1, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 2, 1, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_998():

    triu = [0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_999():

    triu = [1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 1, 3, 3, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1000():

    triu = [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 1, 3, 2, 1, 2, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1001():

    triu = [1, 0, 0, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1002():

    triu = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 2, 2, 2, 1, 2, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1003():

    triu = [1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 3, 1, 3, 2, 1, 2, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1004():

    triu = [0, 0, 1, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 2, 2, 2, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1005():

    triu = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [0, 2, 1, 1, 2, 1, 1, 2, 2, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1006():

    triu = [0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [2, 0, 1, 1, 2, 2, 2, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1007():

    triu = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 0, 0, 3, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1008():

    triu = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1009():

    triu = [1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1010():

    triu = [0, 1, 0, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1011():

    triu = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1012():

    triu = [0, 0, 1, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1013():

    triu = [1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1014():

    triu = [0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1015():

    triu = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1016():

    triu = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 1, 3, 0, 0, 1, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1017():

    triu = [1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 1, 1, 0, 0, 1, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1018():

    triu = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 1, 0, 1, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1019():

    triu = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [1, 1, 3, 1, 0, 1, 0, 1, 0, 1]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1020():

    triu = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [2, 2, 2, 2, 0, 1, 1, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1021():

    triu = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [1, 3, 1, 1, 1, 0, 0, 1, 1, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1022():

    triu = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [3, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


def test_1023():

    triu = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert matches_count_windels(triu, 1, expected_counts)


