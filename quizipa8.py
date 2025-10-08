import streamlit as st
import random

# Data soal
soal_ipa = [
    {
        "soal": "Apa nama planet terdekat dengan matahari?",
        "pilihan": ["Mars", "Venus", "Merkurius", "Bumi"],
        "jawaban": "Merkurius",
        "materi": "Astronomi"
    },
    {
        "soal": "Bagian tumbuhan yang berfungsi sebagai tempat fotosintesis adalah...",
        "pilihan": ["Akar", "Batang", "Daun", "Bunga"],
        "jawaban": "Daun",
        "materi": "Biologi Tumbuhan"
    },
    {
        "soal": "Zat cair yang digunakan untuk mengukur suhu adalah...",
        "pilihan": ["Air", "Alkohol", "Minyak", "Air Raksa"],
        "jawaban": "Air Raksa",
        "materi": "Fisika"
    },
    {
        "soal": "Proses perubahan wujud benda dari cair menjadi gas disebut...",
        "pilihan": ["Menguap", "Mencair", "Membeku", "Menyublim"],
        "jawaban": "Menguap",
        "materi": "Kimia"
    },
    {
        "soal": "Organ pernapasan utama pada manusia adalah...",
        "pilihan": ["Jantung", "Ginjal", "Paru-paru", "Hati"],
        "jawaban": "Paru-paru",
        "materi": "Biologi Manusia"
    },
    {
        "soal": "Satuan standar internasional untuk energi adalah...",
        "pilihan": ["Watt", "Newton", "Joule", "Volt"],
        "jawaban": "Joule",
        "materi": "Fisika"
    },
    {
        "soal": "Senyawa kimia air adalah...",
        "pilihan": ["CO2", "H2O", "O2", "NaCl"],
        "jawaban": "H2O",
        "materi": "Kimia"
    },
    {
        "soal": "Apa yang membuat daun berwarna hijau?",
        "pilihan": ["Xantofil", "Antosianin", "Klorofil", "Karoten"],
        "jawaban": "Klorofil",
        "materi": "Biologi"
    },
    {
        "soal": "Gaya yang menyebabkan benda jatuh ke bawah adalah...",
        "pilihan": ["Gaya gesek", "Gaya magnet", "Gaya pegas", "Gaya gravitasi"],
        "jawaban": "Gaya gravitasi",
        "materi": "Fisika"
    },
    {
        "soal": "Bagian sel tumbuhan yang tidak ada pada sel hewan adalah...",
        "pilihan": ["Dinding sel", "Membran sel", "Nukleus", "Sitoplasma"],
        "jawaban": "Dinding sel",
        "materi": "Biologi Sel"
    },
    {
        "soal": "Logam yang berada dalam wujud cair pada suhu kamar adalah...",
        "pilihan": ["Besi", "Emas", "Perak", "Raksa"],
        "jawaban": "Raksa",
        "materi": "Kimia"
    },
    {
        "soal": "Hewan yang memiliki tulang belakang disebut...",
        "pilihan": ["Avertebrata", "Vertebrata", "Mamalia", "Herbivora"],
        "jawaban": "Vertebrata",
        "materi": "Biologi Hewan"
    },
    {
        "soal": "Alat yang digunakan untuk mengukur tekanan udara adalah...",
        "pilihan": ["Termometer", "Barometer", "Anemometer", "Hidrometer"],
        "jawaban": "Barometer",
        "materi": "Fisika"
    },
    {
        "soal": "Berapa jumlah planet di tata surya kita?",
        "pilihan": ["7", "8", "9", "10"],
        "jawaban": "8",
        "materi": "Astronomi"
    },
    {
        "soal": "Penyebab terjadinya siang dan malam adalah...",
        "pilihan": ["Rotasi bumi", "Revolusi bumi", "Rotasi bulan", "Revolusi matahari"],
        "jawaban": "Rotasi bumi",
        "materi": "Astronomi"
    }
]

# Acak soal sekali saja
if 'shuffled_soal' not in st.session_state:
    st.session_state.shuffled_soal = random.sample(soal_ipa, len(soal_ipa))
    st.session_state.current_index = 0
    st.session_state.skor = 0
    st.session_state.sudah_dijawab = False

st.title("🧪🔭 Kuis IPA Interaktif")
st.subheader("Jawab 15 soal pilihan ganda dan uji pengetahuan IPA-mu!")

# Menampilkan soal saat ini
if st.session_state.current_index < len(st.session_state.shuffled_soal):
    current_q = st.session_state.shuffled_soal[st.session_state.current_index]
    st.write(f"**Soal ke-{st.session_state.current_index + 1} ({current_q['materi']})**")
    st.write(current_q["soal"])
    
    pilihan = st.radio("Pilih jawaban kamu:", current_q["pilihan"], key=f"q{st.session_state.current_index}")

    if st.button("Kirim Jawaban"):
        if not st.session_state.sudah_dijawab:
            st.session_state.sudah_dijawab = True
            if pilihan == current_q["jawaban"]:
                st.success("Benar! 🎉")
                st.session_state.skor += 1
            else:
                st.error(f"Salah. 😥 Jawaban yang benar adalah: **{current_q['jawaban']}**")
        else:
            st.info("Kamu sudah menjawab soal ini.")

    if st.session_state.sudah_dijawab:
        if st.button("Lanjut ke Soal Berikutnya ➡️"):
            st.session_state.current_index += 1
            st.session_state.sudah_dijawab = False
            st.experimental_rerun()

else:
    st.markdown("## 🏁 Permainan Selesai!")
    st.markdown(f"### Skor Akhir: **{st.session_state.skor} / 15**")

    if st.session_state.skor >= 12:
        st.success("🌟 Luar biasa! Kamu adalah ilmuwan cilik sejati!")
    elif st.session_state.skor >= 8:
        st.info("👍 Bagus! Pengetahuan IPA-mu cukup baik.")
    else:
        st.warning("📘 Terus semangat belajar, ya!")

    if st.button("🔁 Main Lagi"):
        st.session_state.clear()
        st.experimental_rerun()
