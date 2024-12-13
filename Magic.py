import json

# Open and load the JSON file
with open('./Magic.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
#print(data)
#print all cards that have '10E' in printings and Print all cards where the card is restricted in the Paupercommander format
for card in data['cards']:
    if card["printings"] and '10E' in card['printings']:
        print(f"{card['name']}\n{card['type']}\n\n{card['text']}\nContains 10E in printings\n")
    if card["legalities"]:
        for legality in card["legalities"]:
            if legality['format'] and legality['format'] == 'Paupercommander' and legality['legality'] and legality['legality'] == 'Restricted':
                if card["printings"] and '10E' in card['printings']:
                    print("Paupercommander format is restricted (10E present).")  
                else:
                     print(f"{card['name']}\n{card['type']}\n\n{card['text']}\nDoes not contain 10E. Papuercommander format is restricted.\n")
    else:
        print('MISSING DATA')


# Print all cards where the card is restricted in the Paupercommander format
