import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


class Univariate:
    """
    Useful Resources: https://www.andrews.edu/~calkins/math/webtexts/statall.pdf

    from argali import descriptive_statistics
    x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1]
    x_summary = descriptive_statistics.Univariate(data=x)
    x_summary.descriptive_summary()

    """

    def __init__(self, data):
        self.data = data

    def mean(self):
        mean = sum(self.data) / len(self.data)
        return mean

    def geometric_mean(self):
        product = 1
        for x in self.data:
            product = product * x

        geometric_mean = product ** (1 / len(self.data))

        return geometric_mean

    def harmonic_mean(self):
        reciprocal = []
        for i in self.data:
            reciprocal.append(i ** -1)
        harmonic_mean = sum(reciprocal) / len(reciprocal)

        return harmonic_mean

    def quadratic_mean(self):
        squared = []
        for i in self.data:
            squared.append(i ** 2)
        quadratic_mean = ((1 / len(squared)) * sum(squared)) ** 0.5
        return quadratic_mean

    def trimmed_mean_01(self):

        trim_index = round(len(self.data) / 100)

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_05(self):

        trim_index = round(len(self.data) / 100) * 5

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_10(self):

        trim_index = round(len(self.data) / 100) * 10

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_custom(self, trim_percentage):

        trim_index = round(len(self.data) / 100) * trim_percentage

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def median(self):
        sorted_ = sorted(self.data)
        if len(sorted_) % 2 == 0:
            median_index = (len(sorted_) / 2) - 1
            median = sorted_[int(median_index)]
        else:
            median_index_top = round(len(sorted_) / 2)
            median_index_bottom = round(len(sorted_) / 2) - 1
            median = (sorted_[median_index_bottom] + sorted_[median_index_top]) / 2

        return median

    def percentile_30(self):
        rank = round(30 / 100 * (len(sorted(self.data))))
        rank += 1
        sorted_ = sorted(self.data)
        rank = sorted_[rank]
        return rank

    def percentile_70(self):
        rank = round(70 / 100 * (len(sorted(self.data))))
        rank += 1
        sorted_ = sorted(self.data)
        rank = sorted_[rank]

        return rank

    def interquartile_range(self):
        iqr = self.percentile_70() - self.percentile_30()
        return iqr

    def unique_value_list(self):
        unique_values = []
        for i in sorted(self.data):
            if i not in unique_values:
                unique_values.append(i)

        return unique_values

    def unique_value_count(self):
        return len(self.unique_value_list())

    def unique_value_frequency(self):
        unique_values = self.unique_value_list()

        value_count_list = []
        for x in unique_values:
            value_count = 0
            for i in sorted(self.data):
                if x == i:
                    value_count += 1
            value_count_list.append(value_count)

        return value_count_list

    def range(self):
        return max(self.data) - min(self.data)

    def deviation_from_mean_list(self):
        mean = self.mean()
        deviation_from_mean_list = []
        for i in sorted(self.data):
            deviation_from_mean_list.append(i - mean)

        return deviation_from_mean_list

    def deviation_squared_list(self):
        deviation_squared = []
        for i in self.deviation_from_mean_list():
            deviation_squared.append(i ** 2)

        return deviation_squared

    def variance(self):
        sum_deviations = sum(self.deviation_squared_list())
        variance = sum_deviations / len(self.deviation_squared_list())

        return variance

    def standard_deviation(self):
        sqrt = self.variance() ** 0.5

        return sqrt

    def skew(self):
        skew = (self.variance() ** 3) / ((len(self.data) * self.standard_deviation()) ** 3)

        return skew

    def kurtosis(self):
        kurtosis = ((self.variance() ** 4) / ((len(self.data) * self.standard_deviation()) ** 4)) - 3

        return kurtosis

    def unique_value_distribution(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)

        f2_ax1 = fig2.add_subplot(spec2[0, 0])
        plt.hist(sorted(self.data))
        plt.plot(self.unique_value_list(),
                 self.unique_value_frequency(),
                 label='Occurrence Count', marker='o')
        plt.xlabel('Unique Value')
        plt.ylabel('Frequency')
        plt.title("Unique Value Frequency Distribution")

        f2_ax2 = fig2.add_subplot(spec2[0, 1])
        plt.boxplot(self.data, notch=True, vert=False)
        plt.xlabel('Unique Value')
        plt.title("Box Plot")

        f2_ax3 = fig2.add_subplot(spec2[1, 0])
        num_bins = round(self.unique_value_count() / 3)
        sigma = self.standard_deviation()
        mu = self.mean()
        n, bins, patches = plt.hist(self.data, num_bins, density=1)
        y = ((1 / (((2 * np.pi) ** 0.5) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
        plt.plot(bins, y, '--')
        plt.xlabel('Bin')
        plt.ylabel('Frequency')
        plt.title("Frequency Distribution")

        f2_ax4 = fig2.add_subplot(spec2[1, 1])
        plt.plot(self.deviation_squared_list())
        plt.xlabel('Unique Value')
        plt.ylabel('Squared Difference')
        plt.title("Squared Difference Plot")

        return fig2

    def descriptive_summary(self):
        '''
        Arithmetic Mean Interpretation
        https://en.wikipedia.org/wiki/Arithmetic_mean#Motivating_properties

        Geometric Mean Interpretation
        https://en.wikipedia.org/wiki/Geometric_mean

        Quadratic Mean (RSM)
        http://www.analytictech.com/mb313/rootmean.htm

        Median, Mode
        http://davidmlane.com/hyperstat/desc_univ.html

        Percentiles
        http://onlinestatbook.com/chapter1/percentiles.html
        http://davidmlane.com/hyperstat/desc_univ.html

        Interquartile Range
        http://davidmlane.com/hyperstat/desc_univ.html

        Skew & Kurtosis
        http://davidmlane.com/hyperstat/desc_univ.html

        :return:
        '''
        print("----------------- \n Descriptive Summary \n -----------------")
        print("Number of Unique Values: ", self.unique_value_count(), "\n")

        print("Arithmetic Mean: ")
        print("The mean is the only single number for which the residuals (deviations from the estimate) sum to "
              "zero. If it is required to use a single number as a typical value for a set of known numbers. The "
              "arithmetic mean of this variable is: ", round(self.mean(), 3))

        print("\nGeometric Mean: \n  indicates the central tendency or typical value of a set of numbers by using the "
              "product of their values. The geometric mean applies only to positive numbers. the geometric mean is "
              "only correct mean when averaging normalized results; that is, results that are presented as ratios to "
              "reference values. The geometric mean of this variable is: ", self.geometric_mean())

        print("\nHarmonic Mean: \n The harmonic mean can be expressed as the reciprocal of the arithmetic mean of "
              "the reciprocals of the given set of observations. For all positive data sets containing at least one "
              "pair of nonequal values, the harmonic mean is always the least of the three means,[1] while the "
              "arithmetic mean is always the greatest of the three and the geometric mean is always in between. Since "
              "the harmonic mean of a list of numbers tends strongly toward the least elements of the list, "
              "it tends (compared to the arithmetic mean) to mitigate the impact of large outliers and aggravate the "
              "impact of small ones. The harmonic mean of this variable is: ", self.harmonic_mean())

        print("\nQuadratic Mean:  \n the square root of the mean of the squares of the numbers in the set. The root "
              "mean square is a measure of the magnitude of a set of numbers. It gives a sense for the typical size "
              "of the numbers. The quadratic mean of this variable is: ", self.quadratic_mean())

        print("\nA trimmed mean is less susceptible to the effects of extreme scores than is the arithmetic mean. It "
              "is therefore less susceptible to sampling fluctuation than the mean for extremely skewed distributions. "
              "It is less efficient than the mean for normal distributions.")

        print("\nTrimmed Mean (+- 1%): ", self.trimmed_mean_01())
        print("Trimmed Mean (+- 5%): ", self.trimmed_mean_05())
        print("Trimmed Mean (+- 10%): ", self.trimmed_mean_10())

        print("\nMedian: \n The median is less sensitive to extreme scores than the mean and this makes it a better "
              "measure than the mean for highly skewed distributions. ", self.median())

        # self.unique_value_distribution()
        # plt.show()

        print("Mean, Median & Mode Comparison \n The mean, median, and mode are equal in symmetric distributions. The "
              "mean is typically higher than the median in positively skewed distributions and lower than the median "
              "in negatively skewed distributions.")

        print("\nRange: The range is the simplest measure of spread or dispersion: It is equal to the difference "
              "between the largest and the smallest values. The range of this variable is: ", self.range())

        print("\nThe value at the 30th percentile is: ", self.percentile_30())
        print("The value at the 70th percentile is: ", self.percentile_70())
        print("The interquartile range is ", self.interquartile_range())

        print("\nThe variance is computed as the average squared deviation of each number from its mean. The variance "
              "for this variable is: ", self.variance())

        print("\nThe standard deviation is the square root of the variance. This variable has a standard deviation of ",
              self.standard_deviation())

        print("\nSkew: \nA distribution is skewed if one of its tails is longer than the other. The skew of the "
              "variable is: ", self.skew())
        print("\nKertosis: \nKurtosis is based on the size of a distribution's tails. Distributions with relatively "
              "large tails are called leptokurtic; those with small tails are called platykurtic. A distribution with "
              "the same kurtosis as the normal distribution is called mesokurtic. Variable kurtosis is: ",
              self.kurtosis())

        print("-----------------")


class Bivariate:
    pass


class Multivariate:
    pass


x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1, 1, 2, 3, 4, 5, 6, 7, 8,
     9, 1, 9, 8, 9, 8, 9, 8, 9, 8, 7, 6, 5, 6, 7, 6, 8, 7, 6, 5, 5, 6, 7, 6, 5, 3, 2, 22, 22, 22, 3, 3, 34, 34, 35, 36,
     37, 38, 1, 10, 10, 10, 10, 10, 10, 10]

x_summary = Univariate(data=x)
x_summary.descriptive_summary()
