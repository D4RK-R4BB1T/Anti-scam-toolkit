# The Anti-Scam toolkit

This was orginally "Anti_Drainer" But I have since renamed the directory to be a bit more fitting.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What's included:

So far: 2 scripts which have their own usage but will be updated to make shit easier for script kiddies and technologically impaired folk to get into security with ease.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MMH3.py

This script is to simply allow you to Generate MMH3 Hashes for usage with https://shodan.io/ (http.html_hash: & hash:) These can be useful for tracking scammers who'll just move their files to another server to prevent an outage due to mass reporing or SpamHaus shutting them down quickly. We encounter this with Tech Support Scammers based out of India quite often when they use AWS, they just move their web application to another machine to avoid an abuse report from effecting them. We also noticed an NFT Pooh Cash move fail to update their old <title></title> HTML Tags so the webpage which was being moved presented a different TLD than the one I was currently on, Couldn't move fast enough I suppose.


The script also allows one to clone github repos to generate MMH3 Hashes from fav.ico and HTML documents allowing one to index pages via shodan easier. It also supports Generation offline.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SSL-gen.py

This script generates SSL hashes and exports prints via CLI, This can be used with https://search.censys.io/ under the drop  down menu with the option "Certificates (Legacy)" using the following usage: parsed.fingerprint_sha1:
example: parsed.fingerprint_sha1:a34ea38610da6cd18c7354abe68f7d21722cb4d5 = Google.com

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# About Future Updates:

Tor seems to be annoying due to how the script was written and how Debian 11 was installed so Until I figure out both, Not going to add it here. Second of all we'll add direct links to shodan & censys (ALL YOU HAVE TO DO IS LOGIN TO EACH SERVICE FIRST!)
