from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from datetime import datetime
import time

# USTAW SWÓJ PORT COM:
COM_PORT = 'COM9'   # zmień jeśli u Ciebie jest inny

def main():
    BoardShim.enable_dev_board_logger()  # opcjonalnie: logi BrainFlow

    params = BrainFlowInputParams()
    params.serial_port = COM_PORT

    board_id = BoardIds.GANGLION_BOARD
    board = BoardShim(board_id, params)

    # przygotowanie sesji
    board.prepare_session()

    # częstotliwość próbkowania (np. 200 Hz)
    fs = BoardShim.get_sampling_rate(board_id)

    # jakie wiersze w macierzy danych odpowiadają EEG
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    print("EEG channels rows:", eeg_channels)

    # start strumienia
    board.start_stream()
    print("Zbieram dane z 4 kanałów (Ctrl+C żeby zakończyć).")

    # nazwa pliku z datą
    file_name = "ganglion_4ch_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"

    # licznik próbek, do wyliczania czasu
    sample_counter = 0
    t0 = time.time()

    with open(file_name, "w") as f:
        # nagłówek
        f.write("time,ch1,ch2,ch3,ch4\n")

        try:
            while True:
                data = board.get_board_data()  # [channels x n_samples]
                if data.size == 0:
                    time.sleep(0.01)
                    continue

                # tylko EEG (Ganglion ma 4 kanały EEG)
                eeg = data[eeg_channels, :]      # kształt: (4, n_samples)
                n_samples = eeg.shape[1]

                for i in range(n_samples):
                    # czas próbki od startu nagrania
                    t = t0 + sample_counter / fs
                    sample_counter += 1

                    ch_vals = eeg[:, i]
                    line = f"{t},{ch_vals[0]},{ch_vals[1]},{ch_vals[2]},{ch_vals[3]}\n"
                    f.write(line)

        except KeyboardInterrupt:
            print("\nPrzerwano przez użytkownika (Ctrl+C).")
        finally:
            board.stop_stream()
            board.release_session()
            print("Sesja zakończona. Dane zapisane w pliku:", file_name)


if __name__ == "__main__":
    main()
