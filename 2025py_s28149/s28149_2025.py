from random import randint

SYMBOLS = ['A', 'C', 'G', 'T']


def generate_sequence(seq_len: int):
    out = ""
    counts = [0, 0, 0, 0]
    for i in range(0, seq_len):
        a = randint(0, 3)
        out += SYMBOLS[a]
        counts[a] += 1
    return (out, counts)


def insert_name(seq: str, name: str) -> str:
    i = randint(0, len(seq))
    return seq[:i] + name + seq[i:]


if __name__ == "__main__":
    seq_len = int(input("Podaj dlugosc sekwencji: "))
    id = input("Podaj ID sekwencji: ")
    opis = input("Podaj opis sekwencji: ")
    name = input("Podaj imie: ")
    (seq, counts) = generate_sequence(seq_len)
    seq = insert_name(seq, name)
    # print(seq)

    with open(id + ".fasta", "w") as f:
        f.write(">")
        f.write(id + " ")
        f.write(opis + "\n")
        f.write(seq)
    print("Sekwencja zostala zapisana do pliku " + id + ".fasta")
    print("Statystyki sekwencji:")
    print("A: {:.2f}%".format(counts[0]/seq_len * 100))
    print("C: {:.2f}%".format(counts[1]/seq_len * 100))
    print("G: {:.2f}%".format(counts[2]/seq_len * 100))
    print("T: {:.2f}%".format(counts[3]/seq_len * 100))
    print("%CG: {:.2f}".format((counts[1]+counts[2])/seq_len * 100))
