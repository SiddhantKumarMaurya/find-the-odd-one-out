# To make a choice of uncommon and common characters
import random
import variables


class choose:

    common = uncommon = ""


def choice(cmn=choose.common, uncmn=choose.uncommon):
    """To make the choice"""

    # To select the character set
    character_set = random.choice(range(48))

    while cmn == uncmn:

        # To choose the characters from the chosen character set
        cmn = random.choice(variables.data[character_set])
        uncmn = random.choice(variables.data[character_set])
    choose.common = cmn
    choose.uncommon = uncmn

choice()