# union - lab 1 - variant 5

In lab 1 variant 5, we required to design a set based on hash-map and
using open address of collision resolution.

## Project structure

- `hashmap.py` -- implementation of immutable`hash_map`class with
  `capacity`,`length`,`add_value`,`reduce_value`,`find_value`
features.
- `hashmap_test.py` -- unit and PBT tests for `Hashmap` in
`hashmap.py`.

## Features

- `capacity()` -- return the capacity of hash map.
- `length()` -- return the length of existing data.
- `add_value(value)` -- add a new element to the hash map.
- `reduce(value)` -- delete the specified element.
- `find_value(value)` -- check whether the specified element is
in the hash table.

## Contribution

- Liao Pengfei (212320014@hdu.edu.cn)
- Wang Luyao(wlysbox@126.com)

## Changelog

- 13.04.2022
  - Initial
  - Add formal sections.
  - Add test coverage.
  - Update README.

## Design notes

- For a Hash Map, I specify that the number of times it finds a
  space is 10, so the maximum allowed is 10 elements with the same
  Hash value. The growth factors for the Hash map can be set by
  yourself, but only if the Hash map is initialized, and then by default
  if more space is needed. My design is for positive numbers only.

- Advantages and disadvantages of PBT test

  - Advantages: For individually constructed data structures,

    equality tests can be performed using their properties rather

    than just the basic modes and data types already provided.

  - Disadvantages: The logic of this test is still controlled by

    humans, so there are still omissions.
