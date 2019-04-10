class Distribution():

    def __init__(self, mean=0, std = 0):
        """
        Generic Distribution class for calculating and visualizating a probability distribution

        :param mean: representing the mean value of the distribution
        :param std: representing the standard deviation value of the distribution
        """
        self.mean = mean
        self.std = std
        self.data = []

    def read_data_file(self, file_name):
        """
        Method to read in data from a txt file. The txt file should have one number (float)
        per line. The numbers are stored in the data attribute

        :param file_name: name of a file to read from
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