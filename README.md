# Find the Odd One Out
#### Video Demo:  <https://youtu.be/5m_UVUZb-1Q>
#### Description: "Find the Odd One Out" is a puzzle game in which players are required to find an odd entity among a group of common entities. Each level of the game is made in such a way that it's generated procedurally and the time allowed for the players to find the odd one reduces with every level. It's source code is written in python and python's tkinter module has been used for creation of the GUI.

##### At the moment the game has two modes:
> Normal Mode
> Hacked Mode

##### Normal Mode:
> In the normal mode, players are provided levels one after the other at some interval, during which the players are supposed to find the odd one, which reduces whith increasing level. The number of correct matches, incorrect matches and missed levels are counted and presented to the player at the end of the game.

##### Hacked Mode:
> In the hacked mode, players will encounter flashes of levels at a very high pace and the score meter will also begin to look bugged as it fails to show the current level and score of the user while flashing the levels, it shows some random numbers. This give the feels of hacking. This mode is an easy way out of the game. If the hack is successful then the player wins in less time, comparatively.

#### The .exe version of the game is available in the **game** directory and the source code is available in the **source_code** directory.

#### The Source Code has following .py files:
>**chosen.py**: This file has a function to choose the set of two characters of which one will be the odd one and the other will be the common one.
>**find_the_odd_one_out.py**: This file has all the necessary functions to create the GUI.
>**patterns.py**: This file generates the patterns, to present an uncommon character among a group of common characters.
>**variables.py**: This file has various sets of the characters from which one set will be chosen in chosen.py and from which two characters will be chosen, one for uncommon and one for common and after which they will be sent into patters.py which will return pattern in a list. This list will be used in Find the Odd One Out.py to generate the levels.

##### variables.py:
###### This file has finely created sets of characters which when chosen for the uncommon and common characters, players will face some difficulty in finding the odd one. For example:
> specialAlpha_set_G = "àâáäãå", If any two characters were to be chosen from this set at random, it would be difficult to find out the odd character
###### There are sets of emojis as well:
> emoji_less = "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚☺🙂🤗🤔😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩" \
                "😬😰😱😳😵😠😡😷🤒🤕🤢🤧😇🤠🤡🤥🤓"
emoji_more ="🥰🤩🤨🥱🤯🥵🥶🤪🥴🤬🤮🥳🥺🤫🤭🧐"
advanced_less = "😈👿👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🐱👤🐱🏍🐱💻🐱🐉🐱👓🐱" \
                "🚀🙈🙉🙊🐵🐶🐺🐱🦁🐯🦊🐮🐷🐗🐭🐹🐰🐻🐨🐸🐴🦄🐔🐲🐽🐾🐒🦍🐕🐩🐕🐈🐅🐆🐎🦌🦏🐂🐃🐄🐖🐏🐑🐐🐪🐫🐘" \
                "🐁🐀🐇🐿🦎🐊🐢🐍🐉🦈🐬🐳🐋🐟🐠🐡🦐🦑🐙🦀🐚🦆🐓🦃🦅🕊🦉🐦🐧🐥🐤🐣🦇🦋🐌🐛🐜🐝🐞🦂🕷🕸🗣👤" \
                "👥👁👀👅👄👣🤺⛷🤼‍"
advanced_more ="🦒🦝🦓🦧🦮🦺🦛🦙🦘🦥🦨🦡🦔🦕🦖🦦🦞🦢🦜🦩🦚🦟🦗🦠🧠🦾🦿🦴🦷"