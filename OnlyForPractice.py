Pa = float(input("P(A): "))
Pb_a =float(input("P(B|A): "))
Pb = float(input("P(B): "))

Pa_b = Pb_a * Pa / Pb
print(f"P(A|B) = {Pa_b}")
