meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "OTW": "Saat seseorang di dalam perjalanan kesesuatu tempat",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("Makna kata", word, "adalah", meme_dict[word])
else:
    print("Makna kata tidak ditemukan")
