#!/usr/bin/env python3

#libs
import random
import os
import metadata_generator
import image_generator

RARECHANCES = 0.1
BLUECHANCES = 0.2
NFTCOUNT = 100

RARE_EXTRA = f"_rare"
BLUE_EXTRA = f"_blue"

# make the folders on .
if not os.path.isdir("numbers"):
    os.system("mkdir numbers")

if not os.path.isdir("./numbers/images"):
    os.system("mkdir ./numbers/images")

if not os.path.isdir("./numbers/metadatas"):
    os.system("mkdir ./numbers/metadatas")

# make our nfts
for token_id in range(NFTCOUNT):
    # generate atributes (just to be clear this could be true and true. two different attributes.)
    # just for this test
    israre = random.random() < RARECHANCES
    isblue = random.random() < BLUECHANCES

    # generate metadata
    metadata = metadata_generator.generate(token_id, israre, isblue)

    file = open(f"./numbers/metadatas/numft_{token_id}", "w")

    print(metadata, file = file)

    # generate image
    img = image_generator.generate(token_id, israre, isblue)

    # save as name...
    filepath = f"./numbers/images/numft_{token_id}{RARE_EXTRA if israre else ''}{BLUE_EXTRA if isblue else ''}.png"
    img.save(filepath)


print("done")
