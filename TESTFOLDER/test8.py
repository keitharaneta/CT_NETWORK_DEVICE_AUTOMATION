def limit(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def eliminate(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


set1 = [1, 1, 2, 3, 3, 4, 5]


def source_data():
    for items in limit(5, eliminate(set1)):
        print(items)


if __name__ == "__main__":
    source_data()
