# -*- coding: utf-8 -*-
# wersja/version 1.9.6

"""Prosty modul do nauki filtrowania oraz transformowania sygnalu.
Simple module for signal filtering and fast Fourier transform.
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt


def gornoprzepustowy(sygnal, czestProbkowania, czestOdciecia):
    """Filtr gornoprzepustowy  (high-pass filter).
    Notes
    -----
    Polish: zauwaz, iz rzad filtra jest z gory narzucony (4).
    English: note that filter order is fixed (4).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    czestProbkowania : int
        Polish: czestotliwosc probkowania, ile razy na sekunde sygnal byl
        pobierany (w herzach).
        English: sampling frequency, how many samples are there acquires per
        second (in herz).
    czestOdciecia : int
        Polish: czestotliwosc odciecia. Powyzej ktorej czestotliwosci
        przepuscic sygnal.
        English: cut-off frequency. Only frequencies above this value will be
        passed.
    Returns
    -------
    array_like
        Polish: wektor z przefiltrowanym sygnalem.
        English: vector containing filtered signal.
    """
    rzad = 4
    czestOdciecia = czestOdciecia/(czestProbkowania*0.5)
    [b, a] = sig.butter(rzad, czestOdciecia, 'high')
    wynik = sig.filtfilt(b, a, sygnal)
    return wynik


def dolnoprzepustowy(sygnal, czestProbkowania, czestOdciecia):
    """Filtr dolnoprzepustowy  (low-pass filter).
    Notes
    -----
    Polish: zauwaz, iz rzad filtra jest z gory narzucony (4).
    English: note that filter order is fixed (4).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    czestProbkowania : int
        Polish: czestotliwosc probkowania, ile razy na sekunde sygnal byl
        pobierany (w herzach).
        English: sampling frequency, how many samples are there acquires per
        second (in herz).
    czestOdciecia : int
        Polish: czestotliwosc odciecia. Ponizej ktorej czestotliwosci
        przepuscic sygnal.
        English: cut-off frequency. Only frequencies below this value will be
        passed.
    Returns
    -------
    array_like
        Polish: wektor z przefiltrowanym sygnalem.
        English: vector containing filtered signal.
    """
    rzad = 4
    czestOdciecia = czestOdciecia/(czestProbkowania*0.5)
    [b, a] = sig.butter(rzad, czestOdciecia, 'low')
    wynik = sig.filtfilt(b, a, sygnal)
    return wynik


def pasmowoprzepustowy(sygnal, czestProbkowania,
                       czestOdciecia1, czestOdciecia2):
    """Filtr pasmowoprzepustowy  (band-pass filter).
    Notes
    -----
    Polish: zauwaz, iz rzad filtra jest z gory narzucony (4).
    English: note that filter order is fixed (4).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    czestProbkowania : int
        Polish: czestotliwosc probkowania, ile razy na sekunde sygnal byl
        pobierany (w herzach).
        English: sampling frequency, how many samples are there acquires per
        second (in herz).
    czestOdciecia1 : int
        Polish: dolna granica filtra.
        English: lower filter cut-off frequency.
    czestOdciecia2 : int
        Polish: gorna granica filtra.
        English: upper filter cut-off frequency.
    Returns
    -------
    array_like
        Polish: wektor z przefiltrowanym sygnalem.
        English: vector containing filtered signal.
    """
    rzad = 4
    czestOdciecia1 = czestOdciecia1/(czestProbkowania*0.5)
    czestOdciecia2 = czestOdciecia2/(czestProbkowania*0.5)
    [b, a] = sig.butter(rzad, [czestOdciecia1, czestOdciecia2], 'bandpass')
    wynik = sig.filtfilt(b, a, sygnal)
    return wynik


def pasmowozaporowy(sygnal, czestProbkowania, czestOdciecia1, czestOdciecia2):
    """Filtr pasmowozaporowy  (band-stop filter).
    Notes
    -----
    Polish: zauwaz, iz rzad filtra jest z gory narzucony (4).
    English: note that filter order is fixed (4).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    czestProbkowania : int
        Polish: czestotliwosc probkowania, ile razy na sekunde sygnal byl
        pobierany (w herzach).
        English: sampling frequency, how many samples are there acquires per
        second (in herz).
    czestOdciecia1 : int
        Polish: dolna granica filtra.
        English: lower filter cut-off frequency.
    czestOdciecia2 : int
        Polish: gorna granica filtra.
        English: upper filter cut-off frequency.
    Returns
    -------
    array_like
        Polish: wektor z przefiltrowanym sygnalem.
        English: vector containing filtered signal.
    """
    rzad = 4
    czestOdciecia1 = czestOdciecia1/(czestProbkowania*0.5)
    czestOdciecia2 = czestOdciecia2/(czestProbkowania*0.5)
    [b, a] = sig.butter(rzad, [czestOdciecia1, czestOdciecia2], 'bandstop')
    wynik = sig.filtfilt(b, a, sygnal)
    return wynik


def FFT(sygnal):
    """Szybka transformacja Fouriera (fast Fourier transform).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    Returns
    -------
    array_like
        Polish: przetransformowany sygnal.
        English: transformed signal.
    """
    wynik = 2*abs(np.fft.fft(sygnal))/len(sygnal)
    return wynik


def rysujFFT(sygnal, show_plot=True):
    """Rysuj FFT (plot FFT).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    show_plot : bool, optional
        Polish: pokaz wygenerowany wykres lub tego nie rob. Ta druga opcja jest
        przydatna gdy chcemy nalozyc na siebie kilka funkcji.
        English: show graph. If it remains unplotted one can overlay a couple
        of functions on the same canvas.
    """
    wynik = 2*abs(np.fft.fft(sygnal))/len(sygnal)
    if len(sygnal) % 256 == 0:
        f = np.linspace(0, 256, len(sygnal))
    else:
        f = np.linspace(0, 200, len(sygnal))
    plt.figure()
    plt.plot(f, wynik)
    plt.xlim([0, 50])
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel(r'U [$\mu V$]')
    if show_plot:
        plt.show()


def rysujPSD(sygnal, show_plot=True):
    """Rysuj PSD (plot PSD).
    Parameters
    ----------
    sygnal : array_like
        Polish: wektor z wartosciami sygnalu w jednostce czasu.
        English: signal -- vector of values acquired in given timepoints).
        May be array (or list) of: ints, floats, doubles.
    show_plot : bool, optional
        Polish: pokaz wygenerowany wykres lub tego nie rob. Ta druga opcja jest
        przydatna gdy chcemy nalozyc na siebie kilka funkcji.
        English: show graph. If it remains unplotted one can overlay a couple
        of functions on the same canvas.
    """
    wynik = 2*abs(np.fft.fft(sygnal))/len(sygnal)
    wynik = np.conjugate(wynik)*wynik
    if len(sygnal) % 256 == 0:
        f = np.linspace(0, 256, len(sygnal))
    else:
        f = np.linspace(0, 200, len(sygnal))
    plt.figure()
    plt.plot(f, wynik)
    plt.xlim([0, 50])
    plt.xlabel("czestotliwosc [Hz]")
    plt.ylabel(r'PSD [$\mu V^2$/Hz]')
    if show_plot:
        plt.show()


def spektrogram(data, Fs, colormap=plt.cm.Accent, show_plot=True, ylim=50):
    """Generowanie spektrogramu (plotting spectrogram).
    Polish: wykres zaleznosci rozkladu czestotliwosci od czasu.
    English: plotting frequencies versus time.
    Parameters
    ----------
    data : array_like
        Polish: wektor z danymi.
        English: vector containing data.
    Fs : int
        Polish: czestotliwosc probkowania, ile razy na sekunde sygnal byl
        pobierany (w herzach).
        English: sampling frequency, how many samples are there acquires per
        second (in herz).
    colormap : mpl_object, optional
        https://matplotlib.org/examples/color/colormaps_reference.html
        Polish: mapa kolorow, obiekt biblioteki matplotlib.
        English: matplotlib colormap.
    show_plot : bool, optional
        Polish: pokaz wygenerowany wykres lub tego nie rob. Ta druga opcja jest
        przydatna gdy chcemy nalozyc na siebie kilka funkcji.
        English: show graph. If it remains unplotted one can overlay a couple
        of functions on the same canvas.
    ylim : int, optional
        Polish: do ktorego punktu osi OX pokazac wykres.
        English: to which value at X axis show the plot.
    """
    plt.figure()
    data_padded = (np.concatenate((np.zeros(200), data, np.zeros(200))))
    Pxx, freqs, bins, im = plt.specgram(data_padded, NFFT=512, Fs=Fs,
                                        window=sig.hamming(512),
                                        noverlap=2*Fs-1,
                                        # noverlap = Fs-1,
                                        cmap=plt.cm.jet)

    plt.ylim(0, ylim)
    plt.xlim(0, len(data)/Fs)

    if show_plot:
        plt.show()


def formatujPlik(sciezka):
    """Formatuj plik CSV (format CSV file).
    Notes
    -----
    Polish: zauwaz, iz operacja nadpisuje plik.
    English: note that this function overwrites the file.
    Parameters
    ----------
    sciezka : str
        Polish: sciezka dostepu do pliku.
        English: file path.
    """
    from sys import platform
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        nazwapliku = ''.join(["////" if i == "//" else i for i in sciezka])
    elif platform == "win32":
        nazwapliku = ''.join(["\\\\" if i == "\\" else i for i in sciezka])

    with open(nazwapliku, 'r') as plikWejsciowy:
        dane = plikWejsciowy.read().splitlines(True)

    samplingRate = dane[2][15:18]
    daneTemp = [linia for linia in dane if not linia[0] == "%"]
    if samplingRate == '200':
        daneTemp.insert(0, "lp, e1, e2, e3, e4, trigger, a2, a3, time\n")
        with open(nazwapliku, 'w') as plikWyjsciowy:
            [plikWyjsciowy.writelines(linia.replace(',', '.').replace('. ', ', '))
             for linia in daneTemp]
    elif samplingRate == '250':
        daneTemp.insert(0, "lp, e1, e2, e3, e4, e5, e6, e7, e8, a1, a2, a3\n")
        with open(nazwapliku, 'w') as plikWyjsciowy:
            [plikWyjsciowy.writelines(linia.replace(',', '.').replace('. ', ', '))
             for linia in daneTemp]
    elif dane[0][0:4] == "0,0." or dane[0][0:5] == "0,-0.":
        daneTemp.insert(0, "lp,e1,e2,e3,e4,trigger\n")
        with open(nazwapliku, 'w') as plikWyjsciowy:
            [plikWyjsciowy.writelines(linia.replace(',', ', '))
             for linia in daneTemp]
