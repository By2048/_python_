from veryprettytable import VeryPrettyTable


def test_table_print():
    table = VeryPrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

    table.align["City name"] = "l"
    table.padding_width = 3

    table.add_row(["Adelaide", 1295, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556, 619.5])
    table.add_row(["Sydney", 2058, 4336374, 1214.8])
    table.add_row(["Melbourne", 1566, 3806092, 646.9])
    table.add_row(["Perth", 5386, 1554769, 869.4])

    print(table)


def test_table_format():
    table = VeryPrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

    table.title = "Australian capital cities"
    table.sortby = "Population"
    table.reversesort = True
    table.int_format["Area"] = "04"
    table.float_format = "6.1"

    table.add_row(["Adelaide", 1295, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556, 619.5])
    table.add_row(["Sydney", 2058, 4336374, 1214.8])
    table.add_row(["Melbourne", 1566, 3806092, 646.9])
    table.add_row(["Perth", 5386, 1554769, 869.4])

    return table.get_string()


if __name__ == '__main__':
    test_table_print()
    print(test_table_format())
