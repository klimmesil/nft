#!/usr/bin/env python3
def generate(token_id, rare, blue):


    # make attributes
    attributes = "{\n"

    # rare
    rarestring = "Rare" if rare else "Common"
    attributes+= " "*6 + "{\n"
    attributes+= " "*8 + '"trait_type" : "Rarity"\n'
    attributes+= " "*8 + f'"value" : "{rarestring}"\n'
    attributes+= " "*6 + "}\n"

    # color
    colorstring = "Blue" if blue else "White"
    attributes+= " "*6 + "{\n"
    attributes+= " "*8 + '"trait_type" : "Color"\n'
    attributes+= " "*8 + f'"value" : "{colorstring}"\n'
    attributes+= " "*6 + "}\n"

    attributes+= "    }"


    # make metadata
    balise = '{\n'
    balise+= f'    "description": "Just a number... Could be a rare one tho",\n'
    balise+= f'    "external_url": "https://bitburgers.io/{token_id}",\n'
    balise+= f'    "image": "https://data.bitburgers.io/nftimages/{token_id}.png",\n'
    balise+= f'    "name": "number {token_id}",\n'
    balise+= f'    "attributes":{attributes}\n'
    balise+= '}'

    return balise
