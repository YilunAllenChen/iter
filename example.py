from iterr import Iter


res = (
    Iter(list(range(10)))
    .filter(lambda x: x % 2 == 0)  # only get the evens
    .inspect(print)  # print them out
    .bind(lambda x: [x, x * 2])  # expand, and then flatten (because bind)
    .map(lambda x: x + 10)  # for each number, add 10
    .inspect(print)  # print again
    .fold(0, lambda acc, num: acc + num)  # sum everything together
)
