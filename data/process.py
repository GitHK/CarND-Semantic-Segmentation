from pprint import pprint
import numpy as np
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt


def test_box_plot(data_to_plot):
    # Create a figure instance
    fig = plt.figure(1, figsize=(16, 4))

    # Create an axes instance
    ax = fig.add_subplot(111)
    ax.set_xlabel('Training results')
    ax.set_ylabel('Losses')
    ax.set_title('Losses after each epoch')

    # Create the boxplot
    # ax.boxplot(data_to_plot)
    ax.violinplot(data_to_plot,
                  showmeans=False,
                  showmedians=True)

    # Save the figure
    fig.savefig('losses.png', )


def parse_train_results(file_name):
    with open(file_name, 'r') as data_file:
        data_holder = {}
        for line in data_file:
            if line.startswith('EPOCH '):
                list_index = int(line.split()[1].replace('#', ''))
                data_holder[list_index] = []
            if line.startswith('Loss: = '):
                data = float(line.split()[2])
                data_holder[list_index].append(data)

        pprint(data_holder)

        return data_holder


if __name__ == '__main__':
    data_holder = parse_train_results(file_name='last_run.txt')

    data_to_plot = []
    for i in sorted(data_holder.keys()):
        data_to_plot.append(data_holder[i])

    test_box_plot(data_to_plot)
