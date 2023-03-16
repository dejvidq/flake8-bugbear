import collections
from collections import defaultdict

this_is_bad = defaultdict(int)

# this_is_fine = defaultdict(str)

# this_is_also_fine = defaultdict()

this_is_not_good = collections.defaultdict(int)

# this_is_fine_too = collections.defaultdict()
