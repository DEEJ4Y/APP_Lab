def remove_empty_tuples(a: list[tuple]):
    count = 0
    for tpl in range(0, len(a)):
        if len(a[tpl]) == 0:
            count += 1

    for i in range(0, count):
        a.remove(())

    return a


tpl_with_content = (1, 2, 3)
empty_tpl = ()

lis_of_tpls = [tpl_with_content, empty_tpl, tpl_with_content,
               tpl_with_content, empty_tpl, tpl_with_content]

print(f'List of Tuples = {lis_of_tpls}')
print(f'After removal: {remove_empty_tuples(lis_of_tpls)}')
