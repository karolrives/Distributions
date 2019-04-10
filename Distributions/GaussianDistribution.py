import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics as stats
from .GeneralDistribution import Distribution


class Gaussian (Distribution):
    """ Gaussian distribution class for calculating and visualizating a
        gaussian distribution.

    """
    def __init__(self, mean, std):
        Distribution.__init__(self, mean, std)

    def calculate_mean(self):
        """
        Method to calculate the mean of the data set

        :return: float : mean of the data set
        """
        self.mean = np.array(self.data).mean()
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Method to calculate the standard deviation of the data set

        :param sample: (bool) whether the data represents a sample or population
        :return: (float) standard deviation of the data set
        """
        if sample:
            self.std = stats.stdev(self.data)
        else:
            self.std = stats.pstdev(self.data)

        return self.std

    def read_data_file(self, file_name, sample=True):
        """
        Overwritten method from Distribution class, to read in data from a txt file
        After reading the file, the mean and std are calculated.

        :param file_name: (string) name of a file to read from
        :param sample: (bool) whether or not the data represents a sample or population
        :return: None
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.std = self.calculate_stdev(sample)

    def plot_histogram(self):
        """
        Method to  output a histogram of the instance variable data  using matplotlib
        pyplot library

        :return:None
        """
        plt.hist(self.data)
        plt.set_title('Histogram')
        plt.set_ylabel('Counts')
        plt.set_xlabel('Data')
        plt.show()

    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution

        :param: x : (float) point for calculating the probability density function
        :return:None
        """
        pdf = norm.pdf(x, self.mean, self.std)

        return pdf

    def plot_histogram_pdf(self, n_spaces=50):

        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        :param
        n_spaces (int): number of data points

        :return
        list: x values for the pdf plot
        list: y values for the pdf plot

        """
        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):

        """Magic method to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """

        # create a new Gaussian object
        result = Gaussian()

        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(math.pow(self.std, 2) + math.pow(other.std, 2))
        return result

    def __repr__(self):

        """Magic method to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """
        return "mean {}, standard deviation {}".format(self.mean, self.std)