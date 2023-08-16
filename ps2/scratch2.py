def greater_elements(elements):
    if not elements:
        return []
    if not elements[1:]:
        return elements
    max_previous = max(elements[:-1])
    if elements[-1] > max_previous:
        return greater_elements(elements[:-1]) + [elements[-1]]
    else:
        return greater_elements(elements[:-1])

print(greater_elements([2, 8, 7, 1, 5]))
