import re

def ekstrak_kata_dasar(kata):

  pola_awal = r"^(di|me|se|ter|be|pe|meng|peng|per|ber|ke)(.*)"
  pola_akhir = r"(kan|kanlah|lah|pun|nya|kah|ku|mu|nya|si)$"

  awalan = re.match(pola_awal, kata)
  if awalan:
    kata = awalan.group(2)

  akhiran = re.search(pola_akhir, kata)
  if akhiran:
    kata = kata[:-len(akhiran.group(0))]

  return kata


kata = input ("Masukkan Kata = ")
kata_dasar = ekstrak_kata_dasar(kata)
print(f"Kata dasar dari '{kata}' adalah '{kata_dasar}'")
