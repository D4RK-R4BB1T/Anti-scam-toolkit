# Anti Drainer - MMH3 Hash Generator for Shodan.io

This program is currently supports generating MMH3 Hashes for .html & .ico files, I got fucking tired of no one making a damn simple script so I made one my damn self.
Currently has 3 Options & Is script kiddie friendly.

1. Generate a hash based on a local file (Might Just be .html) so may update this if it's the case.
2. Download + Generate a MMH3 Hash + Hexidecmial Value from a webpage (please prefix with http:// or https:// or you'll get an error)
3. Clone a Github repo and specifiy a file you want to generate a hash from.

This is intended to combat NFT Drainers by calculating Hashes to be used with shodan.io by using the following search: http.html_hash:"[INSERT HASH HERE]" I plan to have ChatGPT update & Add support for tor that way we can easily monitor potential opsec failures via fav.ico hashes. I'll continue to update this file & Hopefully add support for Generating SSL Information or printing links for shodan, censys & zoomeye to make it even easier as a plug and play script so no one needs to read that terrible documentation.

to run: python3 MMH3.py 
Options are simple, Might add a translation to the top 10 Langauges so it's easier to plug and play globally.
