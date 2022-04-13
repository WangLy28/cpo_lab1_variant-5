# union - lab 1 - variant 5

In lab 1 variant 5, we required to design a set based on hash-map and using open address of collision resolution.

## Project structure

- `hash_map.py` -- implementation of immutable `hash_map` class with `capacity`, `length`, `add_value`,`reduce_value`,`find_value`features. 
- `auto_test.py` -- unit and PBT tests for `hash_map` in `hash_map.py`.
- `hash_map_i.py` -- implementation of immutable `hash_map` class with `capacity`, `length`, `add_value`,`reduce_value`,`find_value`features. 
- `auto_test_i.py` -- tests for `hash_map` in `hash_map_i.py`.

## Features

- `capacity()` -- return the capacity of hash map. 
- `length()` -- return the length of existing data.
- `add_value(value)` -- add a new element to the hash map.
- `reduce(value)` -- delete the specified element.
- `find_value(value)` -- check whether the specified element is in the hash table

## Contribution

- Liao Pengfei (212320014@hdu.edu.cn)
- Wang Luyao(wlysbox@126.com)

## Changelog

- 13.04.2022 - 0
  - Initial
  - Add formal sections.
  - Add test coverage.
  - Update README. 


## Design notes

- For mutable and immutable, I think the biggest difference is whether the initial variable changes. So for Mutability, I will add and remove elements from the Hash map built into the data structure of the Hash Map. For mutability, I define the two operations independently and accept the change using the variable new instead of the initial variable. For a Hash Map, I specify that the number of times it finds a space is 10, so the maximum allowed is 10 elements with the same Hash value. The growth factors for the Hash map can be set by yourself, but only if the Hash map is initialized, and then by default if more space is needed. My design is for positive numbers only.
- Unit test and PBT
  - Unit testing helps developers write code that improves quality and reduces bugs. But Writing unit tests adds to the programmer's workload.
  - PBT test coverage is wide. In some cases, PBT can find bugs that the unit tests did not

