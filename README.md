# The Anti-Scam toolkit

This was orginally "Anti_Drainer" But I have since renamed the directory to be a bit more fitting.

This toolkit focuses on sniffing out lazy scammers webpages or anything for that matter by focusing on fav.ico & .html MMH3 Hashes & SSL Cert Hash fingerprints, It should allow you to easily use 2 IoT & Certicate Browsers more efficiantly and is user friendly. It's plug and play for those who have installed Python3. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What's included:

So far: 2 scripts which have their own usage but will be updated to make shit easier for script kiddies and technologically impaired folk to get into security with ease.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MMH3.py

This script is to simply allow you to Generate MMH3 Hashes for usage with https://shodan.io/ (http.html_hash: & hash:) These can be useful for tracking scammers who'll just move their files to another server to prevent an outage due to mass reporing or SpamHaus shutting them down quickly. We encounter this with Tech Support Scammers based out of India quite often when they use AWS, they just move their web application to another machine to avoid an abuse report from effecting them. We also noticed an NFT Pooh Cash move fail to update their old <title></title> HTML Tags so the webpage which was being moved presented a different TLD than the one I was currently on, Couldn't move fast enough I suppose.


The script also allows one to clone github repos to generate MMH3 Hashes from fav.ico and HTML documents allowing one to index pages via shodan easier. It also supports Generation offline.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SSL-gen.py

This script generates SSL hashes and exports prints via CLI, This can be used with https://search.censys.io/ under the drop  down menu with the option "Certificates (Legacy)" using the following usage: parsed.fingerprint_sha1:
example: parsed.fingerprint_sha1:a34ea38610da6cd18c7354abe68f7d21722cb4d5 = Google.com

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tor Support Officially released

Despite their being a bug with the .fav ico missprinting a direct shodan link, Tor is now supported but the proxy it uses shouldn't be trusted for everything. I Highly recommend avoiding sites dealing with Pedophila, Beastiality & Etc as this will download an .html or .fav ico & That can get messy quickly. to add Tor Support just apperhend the domain with .ly (.onion.ly) this allows the bypassing of those who'd otherwise not be able to use Tor Browser but since it's a clear-net proxy I wouldn't trust it with my Privacy & thus should only be used for easily accessing otherwise hard to each services. This also means other programs such as Dirsearch are now able to also storm the heavens & take down the gods.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# About Future Updates:

1. ~~Tor seems to be annoying due to how the script was written and how Debian 11 was installed so Until I figure out both, Not going to add it here.~~ Just change .onion to onion.ly for now. Tor is now I'll say officially supported. 

2. ~~we'll add direct links to shodan & censys~~ You will now have a direct link to shodan but not censys (ALL YOU HAVE TO DO IS LOGIN TO EACH SERVICE FIRST!)

3. We'll create a script which will make it easier to use shodan for those whom have already logged in by allowing you to just enter keywords or batch keywords than export/print a direct link using the search operator. For instance if you wanted to use http.html:"Carding" the script will generate the direct link for you i.e. https://www.shodan.io/search?query=http.html%3A%22carding%22 when you only typed Carding, allowing you to be fucking lazy. The script will also allow you to batch keywords from a text file as I seriously hate the daily limit and It's just easier to pickup from a exported .txt file. You'll also be able to generate 20 pages by allowing you to just browse without having to manually click NEXT instead of go to page XX or god forbid add the damn page number to the URL because good lord I'd rather just be able to gen my 20 pages and pick what one I want to go to without having to blow through my daily limit. (There's no go-to page button so I'm semi-fixing that).

Will find a way to add Network Header Collections so potential leaks can be observered

Will add some feature to see technology used such as Programming Langauge, Security, Analytics and etc.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# end goal:

The end goal here is simple, Make an open-source user friendly tool kit that's going to make shit easier, lazier & faster all without having to install browser addons or additional scripts/programs whist keeping this as error-free & Simple. All you need is python3, An Internet connection and 2-3 brain cells. 
