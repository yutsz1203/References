# Regular Expressions (Regex)

- Useful for matching strings in code, user input, documents, spreadsheets, log files, and more
- When without anchors (^$), the regex partially match pieces across all the text

## Characters

- \d: Digit (0-9)
- \D: Not a Digit
- \w: Word Character (a-z, A-z, 0-9, \_)
- \W: Not a word character
- \s: Any whitespace characters (Space, tab, newline, carriage return, vertical tab)
- \S: Any character that is not whitespace characters

## MetaCharacters (Need to be escaped)

. ^ $ \* + ? { } [ ] \ | ( )

## Quantifiers

- +: 1 or more
  - .+: One or more any character
- \*: 0 or more
  - a\*: Zero or more "a"(s)
- ?: 0 or One
  - plurals?: matches plural and plurals
- {3}: Exactly Number
  - a{3}: matches aaa
- {2,4}: Range of Numbers (Minimum, Maximum)
  - a{2-4}: matches aa, aaa, aaaa
- {3, }: Number or more times
  - a{3, }: matches aaa, aaaa

## More Characters

- . : Wildcard. Any character except new line

## More Whitespaces

- \t: Tab
- \r: Carriage return character
- \n: New line character

## Character Classes

- [...]: Match specific characters, inside the square bracket (Does not need to escape characters inside the square bracket)
- [x-y]: Match one of the characters in the range from x to y
- [^x]: One character that is not x

## Anchors and Boundaries

- ^: Start of string
- $: End of string
- \b: Word boundary, where one side only is an ASCII letter, digit or underscore
  - Bob.\*\bcat\b: matches Bob ate the cat
- \B: Not a word boundary

## Logic

- (...): Capturing group
  - ^(IMG\d+)\.png$: matches the file name only
- \1: Contents of Group 1
  - r(\w)g\1x: matches regex
- \2: Contents of Group 2
  - (\d\d)\+(\d\d)=\2\+\1: matches 12+65=65+12
- (...(...)): Capturing subgroups
  - ^(IMG(\d+))\.png$: matches both the file name and the digits in the file name
- |: OR
  - I love (cats|dogs): matches "I love cats" and "I love dogs"

## Common regex

- Email addresses: [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

## Resources

- https://regexone.com/
- https://regex101.com/
- https://www.rexegg.com/regex-quickstart.php
