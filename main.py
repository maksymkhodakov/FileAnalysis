import math

import seaborn
from matplotlib import pyplot as plt

if __name__ == '__main__':
    filename = "analyticsRounded.txt"
    with open(filename) as f:
        res = [line.rstrip() for line in f]

    sizes = []
    freqs = []
    for line in res:
        size, freq = line.split(' ')
        sizes.append(size)
        freqs.append(int(freq))


    def autopct(pct):
        return ('%.2f%%' % pct) if pct > 5 else ''


    def get_labels():
        labels = []
        for i, size in enumerate(sizes):
            if freqs[i] > sum(freqs) * 0.05:
                labels.append(f">{size}b")
            else:
                labels.append('')
        return labels


    colors = seaborn.color_palette("pastel", n_colors=11, desat=0.9)
    pie = plt.pie(freqs, labels=get_labels(), autopct=autopct, colors=colors)

    plt.legend(pie[0], [f"size > {i}" for i in sizes], bbox_to_anchor=(0, 0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    plt.tight_layout()
    plt.show()

    log_sizes = []
    for size in sizes:
        if size == '0':
            log_sizes.append('')
        else:
            log = math.log10(int(size))
            log_sizes.append(f"10^{int(log)}")
    plt.plot([log for log in log_sizes], freqs)
    plt.xticks(rotation=45)
    plt.show()
