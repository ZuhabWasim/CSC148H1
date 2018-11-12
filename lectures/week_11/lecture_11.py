""" Lecture 11 Notes
-call stack: when one function calls another and another function calls another,
-names (parameters) are local
-put a break point in the line of code and if i execture that line, the program will stop and you can observe values
-shift alt f9

-tracing, step over, step into, step out of
-references local to a function no longer exist when exiting the function
-frames in the debugger are ordered in a stack formation
-<listcomp> has its own frame in the stack, its own environment

-method resolution order,
if you have an object with a class hierarchy,
python goes from bottom to top (is this method in the child? no? look at the parent? no? look at the grandparent)

-when debugging,
when the variable in the main method, is passed into the function filter_list, the two variables point to the same object
and when the execution of the function is ceased, the data types are all gone, so the variable points to a null list


Hashes
lists are contiguous (adjacent) sequences of references to
objects, so access to a list position is fast (just arithmetic)

lists: first order, top data structure -> we use these everyday

what if we could convert | hash | other data to a suitable
integer for a list index, we'd want:
    I fast
    I deterministic: the same (or equivalent values) gets hashed
    to the same integer each time.
    I well-distributed: We'd like a typical set of values to get
    hashed pretty uniformly over the available list positions.

the differences between hashes and lists
    the key doesn't have to be integers, any immutable objects

the retrieval from a list is constant time
the list knows its starting spot, all references of lists are the same size,
starting spot + 297 * slot size = position of the memory.

pythons has function
hash("fish") -> 8357239587305

you can't hash lists
>>> list1 = [0] # key to "fish"
>>> id(list1)
3069263116
>>> list2 = [0, 1] # key to "foul"
>>> id(list2)
3069528300
>>> list1.append(1)
>>> id(list1) # both lists are the same! which one does it point to?
3069263116
oops!
--> you can't have mutable keys

hash to hash table (dictionary)
Once you have hashed an object to a number, you can easily
use part of that number as an index into a list to store the
object, or something related to that object. If the list is of
length n, you might store information about object o at index
hash(o) % n.

collisions, the uniqueness of each hash
even a well-distributed hash function will have a surprising
number of collisions...
how many people do you need to poll before you nd two with
the same birthday (out of 366 possibilities, including leap-year)?
the mathematics is a bit counter-intuitive... the probability of a
non-collision for 23 birthdays is:
p = 366!/366^23 = 0.493

so how do we avoid such collisions?
when a collision occurs, two values want to be in the same position, so for each item in the list is a sublist

we use chaining, probing
a couple of tactics for dealing with two different keys ending up
at the same index
[[], [], [], [], [], [], [], []]
    chaining: keep a small (one hopes) list at that index
(sometimes called bucket)
    probing: explore, in a systematic way, until the next open
index
either tactic has costs, so keep collisions to a minimum by
keeping the list partly empty

note that its easier to keep the buckets small rather than hash the hash.
-goes through each bucket and if the bucket as several items, iterate through them linearly, as doing this on small buckets are small
-also, to find the right bucket, take the hash of th ekeyand modulus it to get the right bucket

Python dictionaries are implemented1 using hash tables and
probing. The cost of collisions is kept small by enlarging the
underlying list when necessary, and the cost of enlarging is
amortized over many dictionary accesses.
The result is that access to a dictionary element is (1),
essentially the time it takes to access a list element.
One downside is that extra work is required to order the keys
or values of a dictionary. What is their \natural" order?
>> we keep the likelyhood of big buckets low, by increasing the number of buckets to reduce the probability, this threshold is essentially experimental,
>> python's threshold is 70% which is the the number of key values you're storing, once it reaches 70% it doubles the number of buckets in the list.

hashmaps more or less are constant, the most time it takes is when the hashmap doubles, which takes proportional to the
size of the list n, but the requirement to double takes approximately double the size to require another double,
so on average, taking all the points it becomes constant.
"""
