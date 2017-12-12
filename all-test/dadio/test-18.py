# 破解凯撒加密算法

chr_info_1 = [chr(i - 32) for i in range(97, 123)]
print(chr_info_1)
for item in chr_info_1:
    print(ord(item), end=' ')
print()

chr_info_2 = [chr(i) for i in range(97, 123)]
print(chr_info_2)
for item in chr_info_2:
    print(ord(item), end=' ')
print()
chr_info = chr_info_1 + chr_info_2


def caesar(message, le):
    print(chr_info)
    replace_str = ''
    for item in message:
        if item in chr_info or item == ' ':
            replace_str += item
    print(replace_str)

    change_str = ''
    for item in change_str:
        new_item = chr(ord(item) + le)
        change_str += new_item
    print(change_str)

WORDS={'triangle', 'tool', 'act', 'system', 'burn', 'please', 'branch', 'record', 'group', 'apple', 'am', 'south', 'jump', 'heat', 'equal', 'finger', 'dark', 'depend', 'slow', 'sharp', 'result', 'blow', 'wtf', 'cry', 'wrote', 'long', 'either', 'basic', 'self', 'original', 'would', 'question', 'pitch', 'study', 'can', 'whether', 'base', 'make', 'talk', 'language', 'sound', 'throw', 'forest', 'of', 'wash', 'control', 'anger', 'pick', 'sing', 'success', 'in', 'my', 'been', 'lady', 'pair', 'their', 'does', 'since', 'color', 'still', 'general', 'hope', 'family', 'came', 'always', 'hot', 'best', 'went', 'log', 'plane', 'find', 'while', 'hard', 'planet', 'star', 'scale', 'ship', 'they', 'drink', 'wife', 'beauty', 'measure', 'arrange', 'will', 'story', 'point', 'search', 'carry', 'support', 'differ', 'surprise', 'jumps', 'cow', 'section', 'double', 'change', 'your', 'method', 'match', 'twenty', "don't", 'receive', 'body', 'gave', 'ice', 'sign', 'race', 'woman', 'other', 'joy', 'neck', 'string', 'weather', 'most', 'event', 'buy', 'lift', 'life', 'atom', 'the', 'interest', 'boat', 'toward', 'speak', 'thought', 'glad', 'discuss', 'indicate', 'molecule', 'king', 'much', 'put', 'fill', 'village', 'own', 'heard', 'should', 'broke', 'his', 'step', 'hold', 'wood', 'trade', 'fire', 'are', 'earth', 'necessary', 'sell', 'exact', 'charge', 'on', 'nature', 'sea', 'huge', 'enemy', 'spend', 'mount', 'table', 'window', 'as', 'vowel', 'often', 'type', 'yard', 'hole', 'offer', 'sheet', 'him', 'shape', 'more', 'capital', 'rail', 'save', 'stick', 'dictionary', 'insect', 'expect', 'usual', 'eight', 'sleep', 'men', 'operate', 'think', 'thus', 'by', 'wait', 'populate', 'brown', 'cold', 'blue', 'hair', 'condition', 'lay', 'common', 'give', 'stretch', 'wave', 'total', 'well', 'square', 'young', 'crease', 'bed', 'least', 'also', 'start', 'black', 'front', 'teach', 'ran', 'rather', 'value', 'fit', 'practice', 'strong', 'ask', 'dead', 'again', 'once', 'together', 'noise', 'land', 'bad', 'gather', 'three', 'too', 'station', 'million', 'cool', 'clean', 'word', 'pretty', 'take', 'several', 'bone', 'repeat', 'have', 'fig', 'summer', 'hill', 'oxygen', 'a', 'song', 'or', 'thick', 'form', 'flower', 'light', 'iron', 'single', 'dear', 'shore', 'skill', 'cook', 'people', 'blood', 'stead', 'dollar', 'near', 'special', 'include', 'afraid', 'raise', 'surface', 'law', 'piece', 'use', 'bank', 'fear', 'certain', 'river', 'reason', 'half', 'warm', 'mine', 'tell', 'range', 'slave', 'began', 'those', 'brought', 'send', 'prepare', 'then', 'good', 'rise', 'middle', 'score', 'wind', 'swim', 'east', 'music', 'animal', 'human', 'reach', 'state', 'sight', 'favor', 'this', 'else', 'week', 'hear', 'both', 'answer', 'fine', 'ground', 'school', 'cloud', 'kind', 'nothing', 'you', 'company', 'happen', 'skin', 'happy', 'wing', 'locate', 'do', 'had', 'lazy', 'rich', 'card', 'new', 'mark', 'late', 'exercise', 'better', 'end', 'temperature', 'took', 'pose', 'solution', 'sun', 'simple', 'trip', 'figure', 'how', 'dog', 'prove', 'natural', 'each', 'off', 'print', 'ring', 'chick', 'continue', 'element', 'after', 'some', 'captain', 'clothe', 'tall', 'free', 'big', 'last', 'but', 'eat', 'block', 'flow', 'game', 'place', 'home', 'that', 'miss', 'consider', 'thing', 'band', 'way', 'map', 'silver', 'oh', 'electric', 'wild', 'was', 'grass', 'engine', 'hour', 'oil', 'women', 'little', 'help', 'paper', 'grew', 'bread', 'baby', 'born', 'go', 'plural', 'bear', 'equate', 'wrong', 'teeth', 'out', 'low', 'he', 'stand', 'thank', 'century', 'decide', 'spoke', 'try', 'move', 'especially', 'money', 'truck', 'play', 'set', 'two', 'where', 'doctor', 'touch', 'magnet', 'liquid', 'describe', 'show', 'gentle', 'got', 'believe', 'meat', 'glass', 'ocean', 'character', 'stood', 'safe', 'read', 'less', 'pull', 'through', 'chair', 'beat', 'watch', 'winter', 'yellow', 'cent', 'true', 'size', 'son', 'mountain', 'these', 'coast', 'govern', 'market', 'ease', 'bell', 'similar', 'particular', 'poem', 'four', 'quick', 'protect', 'sure', 'written', 'to', 'industry', 'reply', 'led', 'hunt', 'symbol', 'difficult', 'fact', 'third', 'property', 'see', 'stay', 'grow', 'for', 'want', 'could', 'correct', 'saw', 'matter', 'develop', 'just', 'tree', 'nose', 'soft', 'walk', 'come', 'length', 'hit', 'decimal', 'flat', 'write', 'climb', 'age', 'period', 'train', 'term', 'position', 'ago', 'quite', 'catch', 'like', 'fresh', 'there', 'remember', 'mouth', 'sent', 'fox', 'five', 'ride', 'opposite', 'them', 'sense', 'parent', 'war', 'center', 'old', 'care', 'what', 'wide', 'tire', 'draw', 'broad', 'silent', 'paragraph', 'add', 'room', 'agree', 'cover', 'shine', 'visit', 'side', 'possible', 'ever', 'bring', 'board', 'next', 'history', 'dry', 'key', 'able', 'chart', 'sail', 'works', 'numeral', 'tiny', 'sugar', 'above', 'great', 'view', 'mother', 'fat', 'distant', 'book', 'arm', 'connect', 'drive', 'region', 'open', 'force', 'under', 'with', 'she', 'even', 'cross', 'our', 'shout', 'behind', 'boy', 'back', 'seat', 'west', 'until', 'hand', 'close', 'be', 'object', 'bird', 'an', 'corner', 'bit', 'moment', 'lead', 'post', 'found', 'phrase', 'made', 'done', 'metal', 'cotton', 'box', 'first', 'column', 'team', 'past', 'shoe', 'who', 'bought', 'now', 'turn', 'fall', 'bottom', 'final', 'unit', 'busy', 'enter', 'probable', 'thin', 'same', 'straight', 'yes', 'head', 'number', 'run', 'bright', 'spread', 'part', 'break', 'very', 'lake', 'need', 'us', 'speed', 'direct', 'experiment', 'machine', 'said', 'pound', 'dance', 'any', 'coat', 'know', 'collect', 'dream', 'list', 'sat', 'many', 'brother', 'death', 'wheel', 'if', 'shop', 'master', 'hurry', 'when', 'bar', 'down', 'select', 'must', 'tail', 'imagine', 'process', 'example', 'noon', 'multiply', 'idea', 'instant', 'one', 'fast', 'floor', 'spot', 'clear', 'course', 'organ', 'poor', 'motion', 'heart', 'art', 'full', 'rub', 'lot', 'man', 'suffix', 'among', 'smell', 'vary', 'enough', 'nine', 'root', 'weight', 'lost', 'far', 'stone', 'excite', 'wire', 'year', 'ten', 'all', 'air', 'second', 'choose', 'fly', 'country', 'few', 'subject', 'fair', 'egg', 'sudden', 'perhaps', 'call', 'tone', 'space', 'valley', 'stop', 'seed', 'get', 'fun', 'shoulder', 'push', 'segment', 'feed', 'deep', 'plant', 'pass', 'main', 'colony', 'and', 'wonder', 'sand', 'plan', 'note', 'time', 'paint', 'never', 'during', 'we', 'hundred', 'problem', 'over', 'north', 'letter', 'rest', 'work', 'whose', 'cut', 'say', 'appear', 'claim', 'slip', 'soldier', 'children', 'held', 'tube', 'may', 'require', 'before', 'follow', 'moon', 'bat', 'store', 'guide', 'quart', 'high', 'wear', 'house', 'verb', 'sky', 'soil', 'why', 'material', 'supply', 'spell', 'look', 'minute', 'round', 'port', 'syllable', 'forward', 'hello', 'radio', 'every', 'strange', 'rain', 'test', 'ball', 'picture', 'produce', 'noun', 'mix', 'leg', 'morning', 'crop', 'shall', 'build', 'danger', 'red', 'smile', 'pay', 'real', 'fish', 'determine', 'gun', 'meant', 'mind', 'name', 'top', 'friend', 'did', 'me', 'chief', 'copy', 'separate', 'compare', 'invent', 'science', 'live', 'month', 'energy', 'speech', 'snow', 'about', 'edge', 'suit', 'share', 'evening', 'camp', 'large', 'gas', 'though', 'rule', 'dad', 'child', 'serve', 'modern', 'join', 'track', 'let', 'yet', 'day', 'girl', 'begin', 'told', 'guess', 'party', 'listen', 'so', 'melody', 'fight', 'felt', 'page', 'caught', 'person', 'occur', 'area', 'trouble', 'steel', 'garden', 'night', 'street', 'case', 'has', 'office', 'green', 'such', 'create', 'eye', 'island', 'knew', 'product', 'line', 'is', 'cost', 'against', 'travel', 'might', 'row', 'deal', 'laugh', 'job', 'fell', 'division', 'count', 'rock', 'class', 'at', 'rose', 'roll', 'shell', 'win', 'cell', 'pattern', 'quotient', 'which', 'duck', 'no', 'wall', 'chance', 'soon', 'learn', 'right', 'crowd', 'meet', 'quiet', 'subtract', 'nation', 'than', 'car', 'horse', 'whole', 'mass', 'drop', 'solve', 'loud', 'neighbor', 'seven', 'feet', 'gold', 'grand', 'desert', 'gone', 'ready', 'clock', 'it', 'early', 'observe', 'nor', 'between', 'path', 'level', 'from', 'except', 'leave', 'six', 'contain', 'die', 'ear', 'road', 'plain', 'provide', 'were', 'seem', 'thousand', 'check', "won't", 'city', 'small', 'feel', 'complete', 'only', 'up', 'lone', 'proper', 'lie', 'cause', 'fruit', 'left', 'field', 'water', 'cat', 'heavy', 'gray', 'effect', 'season', 'her', 'white', 'keep', 'present', 'sit', 'student', 'farm', 'door', 'town', 'suggest', 'represent', 'kept', 'world', 'order', 'foot', 'inch', 'steam', 'kill', 'salt', 'consonant', 'substance', 'press', 'here', 'wish', 'mean', 'hat', 'love', 'experience', 'sister', 'notice', 'settle', 'corn', 'famous', 'arrive', 'degree', 'design', 'continent', 'power', 'dress', 'chord', 'allow', 'food', 'rope', 'spring', 'finish', 'current', 'short', 'circle', 'father', 'mile', 'voice', 'stream', 'major', 'tie', 'sentence', 'instrument', 'divide', 'fraction', 'face', 'milk'}

def break_caesar(message):
    replace_str = ''
    for item in message:
        if item in chr_info or item == ' ':
            replace_str += item
    print(replace_str)
    print('------')

    for i in range(25):
        change_str = ''
        for item in replace_str:
            if item != ' ':
                new_item = ''
                if item in chr_info_1:
                    new_item = chr(ord(item) - i)
                    if ord(new_item) > 90:
                        new_item = chr(65 + ord(new_item) - 90)
                    if ord(new_item)<65:
                        new_item = chr(26 + ord(new_item))

                elif item in chr_info_2:
                    new_item = chr(ord(item) - i)
                    if ord(new_item) > 122:
                        new_item = chr(97+ ord(new_item) - 122)
                    if ord(new_item) < 97:
                        new_item = chr(26 + ord(new_item))
                change_str += new_item
            else:
                change_str += ' '
        print(i,end=' ')
        print(change_str)

        cnt=0
        for word in change_str.split(' '):
            # print(i,end=' ')
            # print(word)
            if str.lower(word) in WORDS:
                print(i)
                return i

# wtf
# caesar('Mjqqt, btwqi!', 2)
# break_caesar('Mjqqt, btwqi!')
break_caesar('DAM? DAM! DAM.')
# break_caesar('Gur dhvpx oebja sbk whzcf bire gur ynml qbt.')

