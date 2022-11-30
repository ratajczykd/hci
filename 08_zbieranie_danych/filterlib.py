from scipy.signal import butter, lfilter
import numpy as np

'''
    Filtering library.
    It consists of two types of filtering:
        * offline - butter_band*_filter() functions
        * online - FltRealTime() class
'''


############################################
#                                          #
#       Butterworth bandpass filter        #
#                                          #
############################################

# Numerator (b) and denominator (a) polynomials of the IIR filter
def butter_bandpass(lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


# Linear filter application
def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


############################################
#                                          #
#       Butterworth bandstop filter        #
#                                          #
############################################

# Numerator (b) and denominator (a) polynomials of the IIR filter
def butter_bandstop(lowstop, highstop, fs, order=2):
    nyq = 0.5 * fs
    low = lowstop / nyq
    high = highstop / nyq
    b, a = butter(order, [low, high], btype='bandstop')
    return b, a


# Linear filter application
def butter_bandstop_filter(data, lowstop, highstop, fs, order=2):
    b, a = butter_bandstop(lowstop, highstop, fs, order=order)
    y = lfilter(b, a, data)
    return y


# double filter function: first stop, then pass
def filter_eeg(data, fs, bandstop=None, bandpass=None, order=2):
    import numpy as np
    if bandstop:
        lowstop, highstop = bandstop
        data = butter_bandstop_filter(data, lowstop, highstop, fs, order)
        print('After bandstop: %s' % np.mean(data))
    if bandpass:
        lowpass, highpass = bandpass
        data = butter_bandpass_filter(data, lowpass, highpass, fs, order)
        print('After bandpass: %s' % np.mean(data))
    return data

############################################
#                                          #
#        Real time filtering class         #
#                                          #
############################################

'''
    Class for real time filtering.
    The filter type can be changed by changing flt_type variable.

    Example use (can be found also in examples directory):

    # go to the main directory of the repo
    import
    raw_data =
'''


class FltRealTime(object):
    def __init__(self, flt_type='4A'):
        self.prev_x = np.zeros((8, 5))
        self.prev_y = np.zeros((8, 5))
        self.prev_x2 = np.zeros((8, 5))
        self.prev_y2 = np.zeros((8, 5))

        self.flt_type = flt_type

    def filterIIR(self, data, nrk):
        # b = 0.0
        # a = 0.0
        # b2 = 0.0
        # a2 = 0.0

        b = np.array([1, 1, 1, 1, 1])
        a = np.array([1, 1, 1, 1, 1])

        b2 = np.array([1, 1, 1, 1, 1])
        a2 = np.array([1, 1, 1, 1, 1])

        j = 5 - 1
        while j > 0:
            self.prev_x[nrk, j] = self.prev_x[nrk, j - 1]
            self.prev_y[nrk, j] = self.prev_y[nrk, j - 1]
            self.prev_x2[nrk, j] = self.prev_x2[nrk, j - 1]
            self.prev_y2[nrk, j] = self.prev_y2[nrk, j - 1]
            j -= 1

        self.prev_x[nrk, 0] = data

        # 1-50Hz
        if ('1' in self.flt_type):
            b = np.array([
                0.2001387256580675,
                0,
                -0.4002774513161350,
                0,
                0.2001387256580675
                ])
            a = np.array([
                1,
                -2.355934631131582,
                1.941257088655214,
                -0.7847063755334187,
                0.1999076052968340
                ])
        # 7-13Hz
        if ('2' in self.flt_type):
            b = np.array([
                0.005129268366104263,
                0,
                -0.01025853673220853,
                0,
                0.005129268366104263
                ])
            a = np.array([
                1, -3.678895469764040,
                5.179700413522124,
                -3.305801890016702,
                0.8079495914209149
                ])

        # 15-50Hz
        if ('3' in self.flt_type):
            b = np.array([
                0.1173510367246093,
                0,
                -0.2347020734492186,
                0,
                0.1173510367246093
                ])
            a = np.array([
                1,
                -2.137430180172061,
                2.038578008108517,
                -1.070144399200925,
                0.2946365275879138
                ])

        # 5-50Hz
        if ('4' in self.flt_type):
            b = np.array([
                0.1750876436721012,
                0,
                -0.3501752873442023,
                0,
                0.1750876436721012
                ])
            a = np.array([
                1,
                -2.299055356038497,
                1.967497759984450,
                -0.8748055564494800,
                0.2196539839136946
                ])

        # none
        if ('5' in self.flt_type):
            b = np.array([1, 1, 1, 1, 1])
            a = np.array([1, 1, 1, 1, 1])

        # 50 Hz
        if ('A' in self.flt_type):
            b2 = np.array([
                0.96508099,
                -1.19328255,
                2.29902305,
                -1.19328255,
                0.96508099
                ])
            a2 = np.array([
                1,
                -1.21449347931898,
                2.29780334191380,
                -1.17207162934772,
                0.931381682126902
                ])

        # 60 Hz
        if ('B' in self.flt_type):
            b2 = np.array([
                0.9650809863447347,
                -0.2424683201757643,
                1.945391494128786,
                -0.2424683201757643,
                0.9650809863447347
                ])
            a2 = np.array([
                1,
                -0.2467782611297853,
                1.944171784691352,
                -0.2381583792217435,
                0.9313816821269039
                ])

        # none
        if ('C' in self.flt_type):
            b2 = np.array([1, 1, 1, 1, 1])
            a2 = np.array([1, 1, 1, 1, 1])

        filtered = self.filter_data(b2, a2, b, a, nrk)
        return filtered

    def filter_data(self, b2, a2, b, a, nrk):
        wynik = 0.0
        for j in range(5):
            wynik += b2[j] * self.prev_x[nrk, j]
            if j > 0:
                wynik -= a2[j] * self.prev_y[nrk, j]
        self.prev_y[nrk, 0] = wynik
        self.prev_x2[nrk, 0] = wynik
        wynik = 0.0
        for j in range(5):
            wynik += b[j] * self.prev_x2[nrk, j]
            if j > 0:
                wynik -= a[j] * self.prev_y2[nrk, j]
        self.prev_y2[nrk, 0] = wynik
        return wynik
