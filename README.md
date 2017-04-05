# Trip Parser Demo

## Summary
Reads from stdin or an input file of drivers and their trips.
Outputs aggregated data for each driver's trips.

config.ini is set up to handle log related options

## Using the Parser
./main.py input.txt
python main.py input.txt
cat input.txt | python3 main.py

## Running unit tests
python.exe -m trip_parser.tests.trip_parser_tests

## Assumptions
  * Using Python 3.6+. Anything older will not work due to 3.6+ features (strict type checking)
  * There will be input from either stdin or a file
  * If not stdin, file exists (exception is not handled, since you can't do much without input anyways)
  * If stdin and no input, press ctrl+d to quit
  * Input data is assumed to be valid. If not, it will log the exception and discard the record that was invalid


## Overview
I chose python over other languages for a few reasons:

  * Dynamically typed so easier to parse files without lots of polymorphism/patterns
  * Scripting language so no compiling overhead while testing
  * Syntax lends itself to easier text processing because it's concise/compact (especially when it came to parsing the commands)
  * I know python better than I do ruby

To sort the results, I relied on a sorting the results with max heap (priority queue).

I considered using F# instead, because the [units of measure type checking](https://fsharpforfunandprofit.com/posts/units-of-measure) would reduce the chance of any unit conversion bugs as the project grows.

F# might be a compiled language with strict typing, but it's flexible enough to do the same sort of jobs as a scripting language with being symbol heavy and a functional language.

I started initially with writing it in F#, but I had the flu over the weekend and had to fight with the tooling for F# with .net core/standard. The tooling for it in Visual Studio 2017 has not been released yet and I wasn't sure if anyone would be able to run my demo with a Windows PC or with Mono. I ending up losing my patience and went with Python instead.

 ## Future Considerations

It's hard to tell exactly what direction this project would go or if it's a "one off". However, if I were to extend it out, I would consider the following:

  * Parallel processing of multiple files asynchronously to speed up parse times
  * Making the command processing more flexible by making each command parser its own function
    * Store each function in a dictionary with the command string as the key
    * When reading the input, access the proper function from the dictionary and invoke it