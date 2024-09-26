def petStore(category, species, breed = "none"):
    """Display information about a pet."""
    print(f"\nYou have selected an animal from the (category) category.")
    if breed == "none":
        print(f"The {category} you selected is a {species}")
    else:
        print(f"The {category} you selected is a {species} {breed}")
    print(f"\nThe {category} would make a great pet!")

category = input("what animal category are you interested in?")
species = input("what species are they from (canine, feline, Scarlet Macaw, Blue and Gold Macaw ")
if category == "dog" or category == "cat":
    breed = input("what breed are you interested in?")
    petStore(category, species, breed)
else:
    petStore(category,species)
petStore(breed="Maltese",species="Canine", category="dog")
petStore("bird",species="Scarlet Macaw")