from random import randint

SYMBOLS = ['A', 'C', 'G', 'T']


# Procedura generuje losowa sekwencje dna i zwraca ja wraz z
# liczba poszczegolnych nukleotydow
# ORIGINAL
# def generate_sequence(seq_len: int):
# MODIFIED (Czytelnosc kodu: dodanie typow zwrotnych)
def generate_sequence(seq_len: int) -> (str, list):
    out = ""
    counts = [0, 0, 0, 0]
    for i in range(0, seq_len):
        a = randint(0, 3)
        out += SYMBOLS[a]
        counts[a] += 1
    return (out, counts)


# Losuje pozycje i wstawia imie do sekwencji
def insert_name(seq: str, name: str) -> str:
    i = randint(0, len(seq))
    return seq[:i] + name + seq[i:]


# funkcja "main"
if __name__ == "__main__":
    # Input uzytkownika
    seq_len = int(input("Podaj dlugosc sekwencji: "))
    id = input("Podaj ID sekwencji: ")
    opis = input("Podaj opis sekwencji: ")
    name = input("Podaj imie: ")
    (seq, counts) = generate_sequence(seq_len)
    seq = insert_name(seq, name)
    # print(seq)

    # Zapis do pliku w formacie fasta
    with open(id + ".fasta", "w") as f:
        # ORIGINAL
        # f.write(">")
        # f.write(id + " ")
        # f.write(opis + "\n")
        # f.write(seq)
        # MODIFIED (Zmiana w one-liner aby wykonywac mniej syscall'i)
        f.write(">" + id + " " + opis + "\n" + seq)
    print("Sekwencja zostala zapisana do pliku " + id + ".fasta")
    # Output statystyk
    print("Statystyki sekwencji:")
    # ORIGINAL
    # print("A: {:.2f}%".format(counts[0]/seq_len * 100))
    # print("C: {:.2f}%".format(counts[1]/seq_len * 100))
    # print("G: {:.2f}%".format(counts[2]/seq_len * 100))
    # print("T: {:.2f}%".format(counts[3]/seq_len * 100))
    #   MODIFIED (Zmiana ilosc liczb po przecinku dla ladniejszego outputu)
    print("A: {:.1f}%".format(counts[0]/seq_len * 100))
    print("C: {:.1f}%".format(counts[1]/seq_len * 100))
    print("G: {:.1f}%".format(counts[2]/seq_len * 100))
    print("T: {:.1f}%".format(counts[3]/seq_len * 100))
    print("%CG: {:.2f}".format((counts[1]+counts[2])/seq_len * 100))
