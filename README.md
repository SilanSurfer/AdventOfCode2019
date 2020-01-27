# AdventOfCode2019
Solutions for Advent of Code 2019 (in Python) with notes, lessons learned, thoughts and frustrations...
I'm still working on solutions even though it's already January. My goal is to finish all challenges

__Day 11__

I wrote code with some debug prints and run it with provided input. Code was running for about 30 seconds and I've, incorrectly, assumed that code stuck in infinite loop. I spend half day debugging only to find out that code was correct I just had to wait longer... I'm too impatient...

__Lessons learned__:
- prints in Python are reeeealy slow, without them code runs 10x faster
- be patient...

__Day 10__
Part 1
- I don't understand how to check visibility of asteroid. Instruction is written in very obfuscated way.
- I thought about cells and this is bad approach. It's simple geometry, you only need to check if asteroid (point) lays on the line between two points.
- I've checked solution on reddit and whole problem is really simple, you just need to calculate angle between asteroids using atan2 and check if such angle for asteroid already exists.
Part 2
- Issue doesn't look hard but I don't know how to calculate steps so that asteroids aren't omitted.
- I was going back in circles so I've looked at some solution and was inspired with my own solution.
- I'm using again angles and distances to calculate rotation of the laser to destroy each asteroid and then I sort them from smallest angle.
- Solution is not working yet, probably I've mixed something with coordinates or calculating angles since laser is rotating clockwise.
- I don't know yet if this is an issue but I'm not taking into account that I shouldn't be storing results because after destruction of each asteroid, old ones could become visible.
- Found description of approach similar to mine but with dictionary with angles as keys, which gave me idea how to solve this. Maybe it will work.
- It finally works!!! I've also used collections.OrderedDict

__Day 13__
Part 1
- Reading intcode and printing output is simple.
- I think that I will create namedtuple for coordinates, variables for tracking paddle and ball positions and some structure for holding block tiles that are on screen
- Instruction is not clear to me. When ball collides with block? When there is collision I should remove one point or whole block?
- I wasn't sure how to calculate colisions so I just printed out length of list of blocks taken from intcode output and it worked...
Part 2
- It looks hard, I will start with playing around with intcode and see what's the output
- Still can get it how to set memory and how computer is working. I will move to next challenge and think about this in the mean time.

__Day14__
Part 1
- First I will figure out how to parse input.
- Parsing input done, I'm not sure in what datastructure keep data... I'm thinking about dictionary (as an adjacency list) with following tuples (substance, quantity)
- I've added some recursion but I'm not sure if this ok, since I still don't know how to calculate quantity of elements.