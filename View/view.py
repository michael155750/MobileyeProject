import matplotlib.pyplot as plt
import numpy as np


class View:
    plt1, plt2, plt3 = plt.subplot(311), plt.subplot(312), plt.subplot(313)

    @classmethod
    def draw_candidates(cls, candidates, auxiliary):
        make_plots(cls.plt1, candidates, auxiliary)

    @classmethod
    def draw_traffic_lights(cls, candidates, auxiliary):
        make_plots(cls.plt2, candidates, auxiliary)

    @classmethod
    def write_lengths(cls, candidates, auxiliary, lengths):
        make_plots(cls.plt3, candidates, auxiliary)
        add_length(cls.plt3, candidates, lengths)

    @classmethod
    def show(cls, image):
        cls.plt1.imshow(image)
        cls.plt2.imshow(image)
        cls.plt3.imshow(image)
        plt.show()


def make_plots(subplot, candidates, auxiliary):
    red_candidates = np.array(list(filter(lambda p: auxiliary[candidates.index(p)] == "red", candidates)))
    green_candidates = np.array(list(filter(lambda p: auxiliary[candidates.index(p)] == "green", candidates)))

    subplot.plot(red_candidates[:, 0], red_candidates[:, 1], 'rx', markersize=4)
    subplot.plot(green_candidates[:, 0], green_candidates[:, 1], 'g+', markersize=4)


def add_length(subplot, candidates, lengths):
    for i in range(len(candidates)):
        subplot.text(candidates[i][0], candidates[i][1], r'{0:.1f}'.format(lengths[i]), color='y')
