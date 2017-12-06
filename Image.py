class Image:
    def __init__(self, data, x, y):
        self.size_x = x
        self.size_y = y
        self.pixels = []
        self.binary_pixels = []
        self.MAPs = {}

        i = 0
        for line in data:
            pixel_row = []
            for j in range(self.size_x):
                pixel_row.append(' ')

            j = 0
            for pixel in line:
                pixel_row[j] = pixel
                j += 1

            for pixel in pixel_row:
                self.pixels.append(pixel)
            i += 1

        for pixel in self.pixels:
            if pixel == ' ':
                self.binary_pixels.append(0)
            else:
                self.binary_pixels.append(1)

    def print_image(self):
        line = ''
        i = 0
        for pixel in self.pixels:
            line += (str(pixel))
            if (i+1) % self.size_x == 0:
                print(line)
                line = ''
            i += 1

    def print_binary_image(self):
        line = ''
        i = 0
        for pixel in self.binary_pixels:
            line += (str(pixel))
            if (i+1) % self.size_x == 0:
                print(line)
                line = ''
            i += 1

    def assign_MAPs(self, label, probability):
        self.MAPs[label] = probability

    def find_max_MAP(self):
        self.max_MAP = float("-inf")
        self.max_label = None
        for i in range(0, 2):
            if self.MAPs[str(i)] >= self.max_MAP:
                self.max_MAP = self.MAPs[str(i)]
                self.max_label = str(i)

    def convert_pixel_groups(self, x, y):
        self.grouped_pixels = []
        i = 0

        while i < len(self.binary_pixels):
            #print(i)
            pixel_array = []
            for j in range(i, i+self.size_x*y, self.size_x):
                for k in range(j, j+x):
                    #print(k)
                    pixel_array.append(self.binary_pixels[k])
            self.grouped_pixels.append(pixel_array)
            #print(pixel_array)
            #input()
            if (i+x) % (self.size_x) == 0:
                i += x + self.size_x * (y-1)
            else:
                i += x

    def convert_pixel_groups_overlap(self, x, y):
        self.grouped_pixels = []
        i = 0

        while i < len(self.binary_pixels) - self.size_x * (y - 1):
            #print(i)
            pixel_array = []
            for j in range(i, i+self.size_x*y, self.size_x):
                for k in range(j, j+x):
                    #print(k)
                    pixel_array.append(self.binary_pixels[k])
            self.grouped_pixels.append(pixel_array)
            #print(pixel_array)
            #input()
            if (i+x) % (self.size_x) == 0:
                i += x
            else:
                i += 1
