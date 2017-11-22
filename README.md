# jsonshredder-py
a highly-configurable, flexible JSON-to-MDList converter

This function is built for difficult JSON, that needs to be converted to a tabular format, but which doesn't have an easily-convertible format (unique/non-standardized keys, ragged hierarchy, etc)

It takes JSON, converts it to a generic object (of nested dictionaries, lists, and primitives), and then converts that object into a 'tabular' format (aka a list of lists)

The function takes three dictionaries as configuration objects:
include, exclude and melded.
include defines branches to include explicitly.
exclude defines branches to exclude (thereby including all other branches implicitly).
melded defines parent-children to combine, to normalize ragged hierarchies.

currently there are four differently-configured calls to the core function (iterprint), that each parse pieces of the NFL Gameday API JSON

# notes:
-include and exclude are mutually exclusive by level.
  so that means, that you can either include specific members in your filter, or exclude specific members.
-if you include members, it filters the subsequent read to only those and their descendants.
-if you exclude members, it filters the subsequent read to every sibling on their level and their respective descendants
-including some members and excluding some members on the same level would confuse it

-melding 'melds' the member to it's children's names... thereby collapsing them into one level in the output

-the order they're written doesn't matter

-the syntax is as follows:
      excluding 'nextupdate' at level 1 would be: exclude.Add("nextupdate",1)

# example usage:
-an example of how the 'shred1' config works (with the included NFL Gameday JSON file) is as follows:

 -starts at the top
 
 -in the first key/value list (aka level 1), which is just the gameid and 'nextupdate', it excludes 'nextupdate' and anything that might be below it.    excl['nextupdate']=1
      so by default it automatically brings in the gameid, without knowing what it is.
      
 -in the next level (level 2, i.e. children of the gameid), it only includes drives and its descendants  incl['drives']=2
 
 -in the next level (level 3), it only excludes 'crntdrv' and its descendants     excl['crntdrv']=3
 
 -in the next level (level 4), it only excludes 'plays' and its descendats   excl['plays']=4
 
 -'start' and 'end' on level 4 have children, whereas none of the other members do.. so those two members are 'melded' to their children to collapse the level. (if those children had descendants it would still keep going though and end up with more columns for those rows)  melded['start']=4   melded['end']=4
