#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Should be O(n), because after adding n * n to a n times, a will be a + n * n * n because n * n * n == n * n * n


b) The for loop will run n times. The while loop will run log(n) times per run of the for loop, because each run of the while loop, j gets divided by 2. So the run time is O(nlog(n))


c) Should run O(n) since it just uses recursion to iterate down from bunnies to 0, summing up the total number of bunny ears (2 per bunny).

## Exercise II

I would use binary search to find the breaking point f as a way to minimize the number of tests (ie egg droppings)

First I would go to floor n/2 and drop an egg.

If the egg broke, I would know I was too high. I could eliminate all the floors above n/2. I would then move to floor n/4.
If the egg did not break, I would know I was too low. I could eliminate all the floors below n/2. I would then move to floor 3n/4.

I would repeat this pattern - go the midpoint of the section I'm looking at, test by dropping an egg, if the egg breaks go to the midpoint between the current floor and the lowest floor of the section I'm testing, if it doesn't, go to the midpoint between the current floor and the highest floor of the section I'm testing.

Eventually, I would find the floor in about log n tries, worst case scenario.