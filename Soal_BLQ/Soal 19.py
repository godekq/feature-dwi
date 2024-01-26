def adalah_pangram(kalimat):
    abjad = set("abcdefghijklmnopqrstuvwxyz")
    kalimat_lower = kalimat.lower()

    for huruf in abjad:
        if huruf not in kalimat_lower:
            return False

    return True

if __name__ == "__main__":
    kalimat1 = "Sphinx of black quartz, judge my vow"
    kalimat2 = "Brawny gods just flocked up to quiz and vex him"
    kalimat3 = "Check back tomorrow; I will see if the book has arrived."

    pangram1 = adalah_pangram(kalimat1)
    pangram2 = adalah_pangram(kalimat2)
    pangram3 = adalah_pangram(kalimat3)

    print(f"Kalimat 1{' '*(len('Check back tomorrow; I will see if the book has arrived.')-len('Sphinx of black quartz, judge my vow'))}: {pangram1}")
    print(f"Kalimat 2                    : {pangram2}")
    print(f"Kalimat 3                    : {pangram3}")
