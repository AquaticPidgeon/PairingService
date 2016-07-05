from utils.manipulate import *
from utils.Dijkstras import *  # or if that doesn't work, try from utils import Dijkstras
import pandas as pd
import json

# store = pd.HDFStore('store.h5')

''' ingredients list to which recipe ingredients will be parsed against '''
ingredients_list = ['abalone', 'absinthe', 'achar', 'ackee', 'acorn squash', 'adobo', 'advieh', 'african birdseye pepper', 'african birdseye peppers', 'agar', 'aioli', 'ajowan', 'ale', 'aleppo pepper', 'aleppo peppers', 'alfalfa sprout', 'alfalfa sprouts', 'alfredo', 'alitame', 'alligator', 'allspice', 'almond', 'almond bark', 'almond butter', 'almond extract', 'almond paste', 'almonds', 'alum', 'amaranth', 'amarena cherries', 'amarena cherry', 'amaretti', 'amaretto', 'amarula', 'amchoor powder', 'amla', 'ancho chile', 'anchovette', 'anchovies', 'anchovy', 'anchovy paste', 'andouille sausage', 'angelica', 'anise', 'annatto seed', 'annatto seeds', 'apple', 'apple butter', 'apple cider vinegar', 'apple jelly', 'apple pie spice', 'apples', 'applesauce', 'apricot', 'apricot jam', 'apricot jelly', 'apricots', 'aquavit', 'arak', 'arborio rice', 'argan oil', 'arrowroot', 'artichoke', 'arugula', 'asadero', 'asafetida', 'asiago cheese', 'asparagus', 'aspic', 'avocado', 'avocados', 'azuki bean', 'azuki beans', 'baba', 'baba ghanoush', 'babaco', 'babka', 'bacon', 'bacon grease', 'bagel', 'bagels', 'bagna cauda', 'bagoong', 'baguette', 'baguettes', 'baharat', 'baking powder', 'baking soda', 'baklava', 'balsamic vinegar', 'bamboo shoot', 'bamboo shoots', 'banana', 'bananas', 'banger', 'banon cheese', 'barbecue sauce', 'bard', 'barley', 'barley sugar', 'baron', 'basil', 'basket cheese', 'basmati rice', 'bass', 'bay leaf', 'bean', 'bean sauce', 'bean sprout', 'bean sprouts', 'bean thread', 'bean threads', 'beans', 'beat', 'bechamel', 'beef', 'beer', 'beer cheese', 'beet', 'beets', 'bento', 'berbere', 'berries', 'berry', 'beurre blanc', 'beurre manie', 'biltong', 'bisque', 'bisquik', 'bitter melon', 'bitter melons', 'black bean', 'black beans', 'black kale', 'black olive', 'black olives', 'black-eyed pea', 'black-eyed peas', 'blackberries', 'blackberry', 'blue cheese', 'blueberries', 'blueberry', 'boerewors', 'bok choy', 'bombay duck', 'borage', 'borscht', 'bottarga', 'bouillon', 'bouquet garni', 'bourbon', 'boursin cheese', 'braai', 'brandy', 'bratwurst', 'brazil nut', 'brazil nuts', 'bread', 'breadcrumb', 'breadcrumbs', 'breadfruit', 'bresaola', "brewer's yeast", 'brick cheese', 'broccoli', 'broccoli raab', 'broth', 'brown rice', 'brown sugar', 'brunoise', 'bruschetta', 'brussels sprout', 'brussels sprouts', 'buckwheat', 'buckwheat groat', 'bulgur', 'butter', 'buttermilk', 'buxton blue cheese', 'cabbage', 'cacao', 'cachaca', 'cactus', 'caerphilly', 'calabaza', 'callaloo', 'calvados', 'canadian bacon', 'cannelini bean', 'cannelini beans', 'canola oil', 'cantaloupe', 'cantaloupes', 'caper', 'capers', 'capsicum', 'carambola', 'caraway seeds', 'carbalose', 'carboy', 'carbquik', 'cardamom', 'carob', 'carrageen', 'carrot', 'carrots', 'cashew', 'cashews', 'cassava', 'casserole', 'catfish', 'caul fat', 'cauliflower', 'caviar', 'cayenne pepper', 'celeriac', 'celery', 'celery seeds', 'chai', 'chambord', 'champagne vinegar', 'champagne yeast', 'chard', 'chaurice sausage', 'chayote', 'cheddar cheese', 'cheese', 'cheeses', 'chendol', 'cherimoya', 'cherries', 'cherry', 'chervil', 'cheshire cheese', 'chestnut', 'chicken', 'chicken breast', 'chicken liver', 'chicken thigh', 'chickpea', 'chicory', 'chile', 'chiles', 'chili', 'chili oil', 'chili powder', 'chili sauce', 'chinese cabbage', 'chinese date', 'chinese five-spice powder', 'chipotle', 'chipotles', 'chives', 'chocolate', 'chowder', 'chutney', 'cider', 'cilantro', 'cinnamon', 'citron', 'citrus oil', 'clafouti', 'clam', 'clams', 'clarified butter', 'clove', 'cloves', 'cocoa', 'cocoa powder', 'coconut', 'coconut oil', 'coconuts', 'cod', 'coffee', 'colby', 'condensed milk', 'confit', 'cookie', 'cookies', 'cool whip', 'copha', 'coriander', 'corn', 'corn flour', 'corn syrup', 'corned beef', 'cornichon', 'cornish yarg cheese', 'cornmeal', 'cornstarch', 'cottage cheese', 'coulis', 'couscous', 'crab', 'crabs', 'craisin', 'cranberries', 'cranberry', 'cranberry bean', 'cranberry beans', 'crayfish', 'cream', 'cream cheese', 'cream of coconut', 'cream of tartar', 'cream of wheat', 'crema de leche', 'creme brulee', 'creme de cacao', 'creme de cassis', 'creme de menthe', 'creme fraiche', 'cremini mushroom', 'cremini mushrooms', 'creole sausage', 'crostini', 'crouton', 'crozzled', 'crystalized ginger', 'cucumber', 'cucumbers', 'cucuzza', 'cumin', 'curacao', 'currant', 'currants', 'curry leaf', 'curry paste', 'curry powder', 'custard', 'date', 'date paste', 'date sugar', 'demi-glace', 'derby cheese', 'dhania-jeera powder', 'dijon mustard', 'dill', 'dovedale cheese', 'dragee', 'duck', 'duck breast', 'duck leg', 'ducks', 'dumpling', 'durian', 'eclair', 'edam', 'edamame', 'eel', 'eels', 'egg', 'egg substitute', 'egg white', 'egg whites', 'egg yolk', 'egg yolks', 'eggplant', 'eggplants', 'eggs', 'elderberries', 'elderberry', 'endive', 'endives', 'english muffin', 'english muffins', 'epazote', 'escalope', 'espresso', 'evaporated milk', 'falafel', 'falernum', 'farina', 'farmer cheese', 'fava bean', 'fava beans', 'feet', 'feijoa', 'fennel', 'fennel seeds', 'fenugreek', 'feta', 'fig', 'file powder', 'fish sauce', 'flax seed', 'flax seeds', 'flounder', 'flour', 'focaccia', 'foie gras', 'fontina cheese', 'frangipane', 'french fries', 'french fry', 'frisee', 'galangal', 'ganache', 'garam masala', 'garlic', 'garlic powder', 'geese', 'gelatin', 'ghee', 'ginger', 'ginger ale', 'ginger beer', 'ginger syrup', 'gingko nut', 'gingko nuts', 'gochujang', 'goji berry', 'golden syrup', 'goose', 'gooseberries', 'gooseberry', 'gorgonzola', 'gouda', 'graham cracker', 'graham crackers', 'gram flour', 'grand marnier', 'granola', 'grape', 'grapefruit', 'grapefruits', 'grapes', 'great northern bean', 'great northern beans', 'green bean', 'green beans', 'green kern', 'green onion', 'green onions', 'greens', 'grits', 'ground beef', 'ground pork', 'ground turkey', 'ground veal', 'grouper', 'gruyere', 'guanbana', 'guava', 'guavas', 'habanero', 'haddock', 'half-and-half', 'halibut', 'ham', 'ham hock', 'hamachi', 'hamburger', 'hamburgers', 'hard cheese', 'haricot verts', 'harissa', 'hash browns', 'havarti', 'hawaij', 'hazelnut', 'hearts of palm', 'heavy cream', 'herbsaint', 'herring', 'hoisin', 'hoki', 'hominy', 'honey', 'honeydew melon', 'honeydew melons', 'horseradish', 'hot sauce', 'huckleberry', 'hundred-year egg', 'hungarian wax chile', 'hungarian wax chiles', 'hungarian wax pepper', 'hungarian wax peppers', 'hyssop', 'ice cream', 'ice wine', 'icing sugar', 'irish cream', 'jack cheese', 'jaggery', 'jamun', 'jasmine rice', 'jelly bean', 'jelly beans', 'jerusalem artichoke', 'jicama', 'kaffir lime', 'kaffir limes', 'kahlua', 'kalamata olive', 'kalamata olives', 'kale', 'kamaboko', 'kasha', 'kashk', 'ketchup', 'ketjab manis', 'kewra essence', 'kewra water', 'khus essence', 'kidney bean', 'kidney beans', 'kielbasa', 'kirsch', 'kiwi', 'kiwis', 'knockwurst', 'kohlrabi', 'kolsch', 'kugel', 'kumquat', 'ladyfingers', 'lamb', 'lancashire cheese', 'lardon', 'lardons', 'latte', 'lavender', 'lecithin', 'leek', 'leeks', 'lefse', 'lemon', 'lemon balm', 'lemon grass', 'lemon juice', 'lemon peel', 'lemon peels', 'lemongrass', 'lemons', 'lentil', 'lentils', 'lettuce', 'li hing mui', 'light cream', 'lima bean', 'lima beans', 'lime', 'lime juice', 'limes', 'liquid smoke', 'liver', 'liverwurst', 'lobster', 'lobsters', 'longan', 'loquat', 'loquats', 'lotus', 'lovage', 'lumpia', 'lycees', 'lychee', 'macadamia nut', 'macadamia nuts', 'macaroni', 'mace', 'mackerel', 'madeira', 'mahi mahi', 'mahleb', 'malt vinegar', 'mandarin orange', 'mandarin oranges', 'mango', 'mangoes', 'mangos', 'mangosteen', 'manzanilla olive', 'manzanilla olives', 'maple syrup', 'maraschino', 'margarine', 'marjoram', 'marmalade', 'marmite', 'marrow', 'marshmallow', 'marshmallows', 'marula', 'marzipan', 'masa', 'masala', 'masarepa', 'mascarpone', 'matzo', 'mayo', 'mayonnaise', 'melon', 'melons', 'meringue powder', 'mesclun', 'mettwurst', 'milk', 'mint', 'miracle whip', 'mirepoix', 'miso', 'moambe sauce', 'molasses', 'monkfish', 'monosodium glutamate', 'morel', 'moringa', 'mortadella', 'mostaccioli', 'moth bean', 'moth beans', 'mozzarella', 'mrs dash', 'muffin', 'muffins', 'mugwort', 'mung bean', 'mung beans', 'muscadine', 'muscovado sugar', 'muscovy duck', 'mushroom', 'mushrooms', 'mushu', 'muskmelon', 'muskmelons', 'mussel', 'mussels', 'mustard', 'mustard powder', 'mustard seeds', 'nasturtium', 'navy bean', 'navy beans', 'nectarine', 'nectarines', 'nigella seed', 'nigella seeds', 'nopale', 'nori', 'nutmeg', 'oatmeal', 'octopus', 'offal', 'okra', 'olive', 'olive oil', 'olives', 'onion', 'onion powder', 'onions', 'orange', 'orange flower water', 'orange peel', 'orange peels', 'oranges', 'oregano', 'orgeat syrup', 'oyster sauce', 'palm oil', 'palm sugar', 'pancetta', 'paneer', 'panir', 'panko', 'panna cotta', 'papaya', 'papayas', 'paprika', 'parmesan cheese', 'parsley', 'parsnip', 'parsnips', 'passion fruit', 'passion fruits', 'pasta', 'pasta filata', 'pastas', 'pastis', 'paysanne', 'pea', 'pea bean', 'pea beans', 'peach', 'peaches', 'peanut', 'peanut butter', 'peanuts', 'pear', 'pears', 'peas', 'pecan', 'pecans', 'pectin', 'peppadew pepper', 'peppadew peppers', 'pepper', 'peppers', 'perch', 'periwinkle', 'persimmon', 'persimmons', 'pesto', 'pheasant', 'pheasants', 'phyllo', 'pickle', 'pico de gallo', 'pie melon', 'pierogi', "pig's cheek", "pig's feet", 'pike', 'piloncillo', 'pimiento', 'pine nut', 'pine nuts', 'pineapple', 'pineapples', 'pink bean', 'pink beans', 'pinto bean', 'pinto beans', 'pistachio', 'pistachios', 'plantain', 'plantains', 'plum', 'plum tomato', 'plum tomatoes', 'plumcot', 'plumcots', 'plums', 'poblano', 'poblano pepper', 'poblano peppers', 'poblanos', 'polenta', 'pomegranate', 'pomegranate molasses', 'pomegranates', 'pomelo', 'pomelos', 'ponzu', 'poppy seed', 'poppy seeds', 'porcini', 'pork', 'portabella', 'potato', 'potato chips', 'potato starch', 'poultry seasoning', 'powdered sugar', 'prawn', 'prawns', 'preserved lemon', 'preserves', 'processed cheese', 'prosciutto', 'provel rope cheese', 'provolone', 'prune', 'prunes', 'pudding', 'puddings', 'puff pastry', 'pumpkin', 'pumpkin pie spice', 'pumpkin seed', 'pumpkin seeds', 'purslane', 'quail', 'quails', 'quenelle', 'queso', 'quince', 'quinces', 'rabbit', 'rabbits', 'radicchio', 'radish', 'radishes', 'raisin', 'raisins', 'rambutan', 'ramp', 'ramps', 'ras el hanout', 'raspberries', 'raspberry', 'raw sugar', 'red bean', 'red beans', 'red cabbage', 'red cabbages', 'red chile powder', 'red onion', 'red onions', 'red pepper', 'red pepper flakes', 'red snapper', 'red wine', 'red wine vinegar', 'rhubarb', 'rice', 'rice paper', 'rice stick', 'rice vermicelli', 'rice vinegar', 'rice wine', 'ricotta cheese', 'romaine lettuce', 'romano cheese', 'rookwurst', 'rose essence', 'rose water', 'rosemary', 'rotel tomatoes', 'rotisserie', 'rum', 'rusk', 'rutabaga', 'saffron', 'sage', 'sago', 'salmon', 'salsa', 'salsify', 'salt', 'salt pork', 'saltines', 'sambal', 'sand dab', 'sardine', 'sardines', 'sauerkraut', 'saunf', 'sausage', 'sausages', 'savory', 'scallop', 'scallops', 'scotch bonnet', 'scrapple', 'sea cucumber', 'seed', 'seeds', 'seitan', 'semi-hard cheese', 'semisweet chocolate', 'semolina', 'serrano ham', 'sesame seed', 'sesame seeds', 'seville orange', 'seville oranges', 'shallot', 'shallots', 'sherry', 'shitake', 'shortening', 'shrimp', 'shrimp paste', 'simple syrup', 'smelt', 'smoke seasoning', 'smoked salmon', 'snap pea', 'snap peas', 'snapper', 'snoek', 'snow pea', 'snow peas', 'soba', 'soda crackers', 'sodium citrate', 'soft cheese', 'soft-shell crab', 'sole', 'somen', 'sorghum', 'sorrel', 'sour cream', 'soy milk', 'soy sauce', 'soybean', 'spaetzle', 'spaghetti squash', 'spanish cheese', 'spearmint', 'spinach', 'split pea', 'split peas', 'squash', 'squid', 'star anise', 'steak', 'stevia', 'stilton', 'strawberries', 'strawberry', 'stuffing', 'sturgeon', 'sucanat', 'sucralose', 'suet', 'sugar', 'sultana', 'sumac', 'summer squash', 'sushi rice', 'sweet chili sauce', 'sweet onion', 'sweet onions', 'sweet pepper', 'sweet peppers', 'sweet potato', 'sweet potatoes', 'sweetbreads', 'sweetened condensed milk', 'swiss cheese', 'swordfish', 'szechuan peppercorn', 'tabasco sauce', 'tahini', 'tamarillo', 'tamarind', 'tamarind paste', 'tandoori paste', 'tapioca', 'tarragon', 'tartar sauce', 'tasso', 'tatsoi', 'tea', 'teff', 'tempeh', 'terrapin', 'thyme', 'tofu', 'togarashi', 'tomato', 'tomato paste', 'tomato puree', 'tomato sauce', 'tomatoes', 'tortilla', 'tortillas', 'trappist cheese', 'tripe', 'trout', 'truffle', 'truffle oil', 'trumpet mushroom', 'trumpet mushrooms', 'tuna', 'turbinado sugar', 'turkey', 'turkey breast', 'turkey kielbasa', 'turkey leg', 'turkey thigh', 'turmeric', 'turnip', 'turnips', 'turtle', 'udon', 'ugli fruit', 'umeboshi', 'unsweetened chocolate', 'vanilla', 'vanilla bean', 'vanilla beans', 'vanilla extract', 'veal', 'vegemite', 'velveeta', 'venison', 'vermicelli', 'vermouth', 'vidalia onion', 'vincotto', 'vinegar', 'vodka', 'walnut', 'walnuts', 'wasabi', 'water', 'water chestnut', 'watercress', 'watermelon', 'watermelon radish', 'watermelon radishes', 'watermelons', 'wattleseed', 'weetabix', 'weisswurst', 'welsh rarebit', 'wensleydale cheese', 'wheat', 'wheat berries', 'wheat berry', 'wheat germ', 'wheat gluten', 'wheat thins', 'whelk', 'whelks', 'white bean', 'white beans', 'white chocolate', 'white vinegar', 'white whine vinegar', 'white wine', 'wild rice', 'wine', 'won ton', 'worcestershire sauce', 'xanthan gum', 'yeast']


''' user enters json or file path '''
recipes_ingredients = get_recipes_ingredients('/Users/alberthahn/HACK_REACTOR/PairingService/combinedRecipes.JSON')


''' representing the ingredients in an initial data frame / adjacency matrix '''
# adj_mat = ingredients_to_df(ingredients_list, recipes_ingredients)
# adj_mat.to_hdf('store_dirty.h5', 'table') # "memoize" by writing to hd5 file

'''
Clean up and format the adjacency matrix by:
#   1. removing rows and columns with zeros
#   2. converting values to probabilities
# It will return an object with two key-value pairs.
# One is the new shortened list of ingredients, and the other is the new matrix
'''
# df_obj = format_df(adj_mat)
# adj_mat = df_obj['df']
# adj_mat.to_hdf('store_clean.h5', 'table') # "memoizes" by writing to hd5 file
# col_names = df_obj['cols']
clean = pd.read_hdf('store_clean.h5', 'table')
col_names = ['absinthe', 'adobo', 'ale', 'allspice', 'almond', 'almond butter', 'almond extract', 'almonds', 'anchovy', 'apple', 'apple cider vinegar', 'apple pie spice', 'apples', 'applesauce', 'apricot', 'apricots', 'arrowroot', 'artichoke', 'arugula', 'asparagus', 'avocado', 'avocados', 'bacon', 'bacon grease', 'baking powder', 'baking soda', 'balsamic vinegar', 'banana', 'bananas', 'barley', 'basil', 'bay leaf', 'bean', 'beans', 'beef', 'beer', 'berries', 'berry', 'black beans', 'black olives', 'blackberries', 'blue cheese', 'blueberries', 'bok choy', 'bouillon', 'bouquet garni', 'bourbon', 'brandy', 'bratwurst', 'bread', 'breadcrumbs', 'broccoli', 'broccoli raab', 'broth', 'brown rice', 'brown sugar', 'butter', 'buttermilk', 'cabbage', 'cacao', 'canola oil', 'capers', 'cardamom', 'carrot', 'carrots', 'cashew', 'cashews', 'casserole', 'cauliflower', 'cayenne pepper', 'celery', 'celery seeds', 'chard', 'cheddar cheese', 'cheese', 'cheeses', 'cherries', 'cherry', 'chervil', 'chicken', 'chicken breast', 'chile', 'chiles', 'chili', 'chili powder', 'chili sauce', 'chipotle', 'chives', 'chocolate', 'cider', 'cilantro', 'cinnamon', 'clarified butter', 'clove', 'cloves', 'cocoa', 'cocoa powder', 'coconut', 'coconut oil', 'cod', 'coffee', 'condensed milk', 'cool whip', 'coriander', 'corn', 'corn flour', 'corn syrup', 'corned beef', 'cornmeal', 'cornstarch', 'cottage cheese', 'couscous', 'crab', 'cranberries', 'cranberry', 'cream', 'cream cheese', 'cream of tartar', 'crouton', 'cucumber', 'cumin', 'currants', 'curry paste', 'curry powder', 'dijon mustard', 'dill', 'egg', 'egg substitute', 'egg whites', 'egg yolk', 'egg yolks', 'eggplant', 'eggplants', 'eggs', 'epazote', 'espresso', 'evaporated milk', 'fava bean', 'fava beans', 'fennel', 'feta', 'fish sauce', 'flour', 'garlic', 'garlic powder', 'gelatin', 'ghee', 'ginger', 'ginger ale', 'goose', 'graham cracker', 'graham crackers', 'granola', 'grape', 'grapefruit', 'green beans', 'green onion', 'green onions', 'greens', 'grits', 'ground beef', 'ground pork', 'ground turkey', 'grouper', 'habanero', 'halibut', 'ham', 'hamachi', 'hamburger', 'hash browns', 'heavy cream', 'hoisin', 'honey', 'honeydew melon', 'horseradish', 'hot sauce', 'hungarian wax pepper', 'ice cream', 'jack cheese', 'jasmine rice', 'jicama', 'kalamata olives', 'kale', 'ketchup', 'kidney beans', 'kielbasa', 'kiwi', 'lamb', 'lardons', 'leek', 'leeks', 'lemon', 'lemon juice', 'lemon peel', 'lemons', 'lettuce', 'light cream', 'lima beans', 'lime', 'lime juice', 'limes', 'liquid smoke', 'macadamia nuts', 'macaroni', 'mace', 'mandarin oranges', 'mango', 'mangos', 'maple syrup', 'maraschino', 'margarine', 'marjoram', 'marshmallow', 'marshmallows', 'masa', 'mascarpone', 'matzo', 'mayo', 'mayonnaise', 'melon', 'milk', 'mint', 'miracle whip', 'molasses', 'morel', 'mortadella', 'mozzarella', 'muffin', 'mushroom', 'mushrooms', 'mussels', 'mustard', 'mustard seeds', 'navy beans', 'nori', 'nutmeg', 'oatmeal', 'octopus', 'olive', 'olive oil', 'olives', 'onion', 'onion powder', 'onions', 'orange', 'orange peel', 'oranges', 'oregano', 'pancetta', 'panko', 'paprika', 'parmesan cheese', 'parsley', 'parsnip', 'parsnips', 'pasta', 'pea', 'peaches', 'peanut', 'peanut butter', 'peanuts', 'pear', 'pears', 'peas', 'pecan', 'pecans', 'pepper', 'peppers', 'pesto', 'pickle', 'pico de gallo', 'pimiento', 'pine nuts', 'pineapple', 'pinto beans', 'pistachio', 'plum', 'plum tomatoes', 'poblano', 'poblano pepper', 'ponzu', 'poppy seeds', 'pork', 'potato', 'poultry seasoning', 'powdered sugar', 'prosciutto', 'pudding', 'pumpkin', 'pumpkin pie spice', 'pumpkin seeds', 'queso', 'radish', 'radishes', 'raisins', 'ramps', 'raspberries', 'raspberry', 'red cabbage', 'red onion', 'red onions', 'red pepper', 'red pepper flakes', 'red wine', 'red wine vinegar', 'rhubarb', 'rice', 'rice vinegar', 'rice wine', 'ricotta cheese', 'romaine lettuce', 'romano cheese', 'rosemary', 'rotisserie', 'rum', 'saffron', 'sage', 'salmon', 'salsa', 'salt', 'salt pork', 'sambal', 'sauerkraut', 'sausage', 'sausages', 'scallops', 'seed', 'seeds', 'semisweet chocolate', 'semolina', 'sesame seeds', 'seville orange', 'shallot', 'shallots', 'sherry', 'shortening', 'shrimp', 'snap peas', 'snow peas', 'sour cream', 'soy sauce', 'spaetzle', 'spinach', 'split peas', 'squash', 'squid', 'steak', 'strawberries', 'strawberry', 'stuffing', 'sugar', 'summer squash', 'sushi rice', 'sweet onion', 'sweet potato', 'sweet potatoes', 'sweetened condensed milk', 'swiss cheese', 'tabasco sauce', 'tahini', 'tapioca', 'tarragon', 'tea', 'thyme', 'tofu', 'tomato', 'tomato paste', 'tomato sauce', 'tomatoes', 'tortilla', 'tortillas', 'tuna', 'turkey', 'turkey breast', 'turmeric', 'turnip', 'turnips', 'unsweetened chocolate', 'vanilla', 'vanilla extract', 'veal', 'venison', 'vermouth', 'vidalia onion', 'vinegar', 'walnuts', 'wasabi', 'water', 'watercress', 'watermelon', 'wheat', 'wheat germ', 'white bean', 'white beans', 'white chocolate', 'white vinegar', 'white wine', 'wild rice', 'wine', 'worcestershire sauce', 'yeast']

# print(adj_mat)

''' sanity check '''
# sanity_check(clean) # -> passed

''' Dijkstras '''
# dijkstras_paths = dijkstras(clean, 'absinthe')['prev'] # works
# print(dijkstras_paths)

'''get path'''
# table = {}
# for source in ['absinthe']:  # perform dijkstras on every single node
#     temp = {}  # will store all paths from an ingredient to the source
#     paths_to_source = dijkstras(clean, source)['prev']  # finds all shortest paths going to source node
#     for i in paths_to_source:
#         temp[i] = get_path(i, source, paths_to_source)['path']
#     table[source] = temp
#     print('TABLE:', table)
#
# print(table)
# oct_apl = get_path('ginger ale', 'absinthe', dijkstras_paths)
# 'apple' is the source. In `oct_apl`, no keys are 'apple'.
# print(oct_apl) # correct


pairings_table = all_shortest_paths(clean, col_names)

# json_pairings_table = json.dumps(pairings_table, indent=2, sort_keys=True, )
# print(json_pairings_table)
# print(type(json_pairings_table))
#
with open('data.json', 'w') as outfile:
    json.dump(pairings_table, outfile, sort_keys=True, indent=2)


''' write k shortest paths table to pickle file'''
# with open('full_test_write.pickle', 'wb') as file:
#     Pickle the 'data' dictionary using the highest protocol available.
#     pickle.dump(pairings_table, file, pickle.HIGHEST_PROTOCOL)
#