from PIL import Image
from PIL import ImageDraw


def make_regalur_image(img, size=(256, 256)):
    return img.resize(size).convert('RGB')


def split_image(img, part_size=(64, 64)):
    w, h = img.size
    pw, ph = part_size
    assert w % pw == h % ph == 0
    return [img.crop((i, j, i + pw, j + ph)).copy() for i in range(0, w, pw) for j in range(0, h, ph)]


def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)


def calc_similar(li, ri):
    return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0


def calc_similar_by_path(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    return calc_similar(li, ri)


def make_doc_data(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    li.save(lf + '_regalur.png')
    ri.save(rf + '_regalur.png')
    fd = open('stat.csv', 'w')
    fd.write('\n'.join(l + ',' + r for l, r in zip(map(str, li.histogram()), map(str, ri.histogram()))))
    fd.close()
    li = li.convert('RGB')
    draw = ImageDraw.Draw(li)
    for i in range(0, 256, 64):
        draw.line((0, i, 256, i), fill='#ff0000')
        draw.line((i, 0, i, 256), fill='#ff0000')
    li.save(lf + '_lines.png')


if __name__ == '__main__':
    path = r'test/TEST%d/%d.JPG'
    for i in range(1, 8):
        print('test_case_%d: %.3f%%' % (i, calc_similar_by_path('test/TEST%d/%d.JPG' % (i, 1),
                                                                'test/TEST%d/%d.JPG' % (i, 2)) * 100))
