This is a "Capchecker" that checks the finds all combinations of 4 cards that from a "cap" in a card game named "EvenQuads" invented by Professor Lauren Rose.

What is Quads?
* Quads is a card game similar to SET, with 64 cards. Each card displays one of 4 symbols appearing 1-4 times, in oneof four colors.
* Players try to find quads sets of 4 cards where the symbols either have the same number, coloror shape, different numbers, colors or shapes, or a pair of numbers, colors or states.

Finding Maximum Caps: 
* In Quads, a cap is defined as a subset in which no collection of four cards forms a quad.
* Our objective is to compute the number of caps of a size 𝑟 in a given dimension 𝑛, with 2𝑛 cards.
* Specifically, for 𝑛 = 7, we want to compute
         𝐶𝑟,7  for r = 1, 2, 3, 4, . . .
* Our code used combinatorial algorithms to compute and enumerate valid caps of different sizes within finite integers.
* It incrementally builds and validates caps using XOR operations, with memoization to optimize efficiency.
* We used it to explore the count of valid caps and performance metrics in higher dimensions.
