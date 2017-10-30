import time
import progressbar


def custom_len(value):
    # These characters take up more space
    characters = {
        '进': 2,
        '度': 2,
    }

    total = 0
    for c in value:
        total += characters.get(c, 1)

    return total


bar = progressbar.ProgressBar(
    widgets=[
        '进度: ',
        progressbar.Bar(),
        ' ',
        progressbar.Counter(format='%(value)02d/%(max_value)d'),
    ],
    len_func=custom_len,
)
for i in bar(range(10)):
    time.sleep(0.1)