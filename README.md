# iterr
rust styled iterator in python
- lazy evaluation
- strongly typed
- all native python, no dependency


```python
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
```


this prints

```
0
10
10
2
12
14
4
14
18
6
16
22
8
18
26
```


note: because of the lazy nature of `Iter`, the elements in the list are processed in the order they were initially defined! This makes debugging easy.
