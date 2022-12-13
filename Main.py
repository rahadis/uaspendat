import streamlit as st
st.set_page_config(
  page_title="Prediksi Harga HP",
)
import Dataset


st.subheader("Prediksi Harga HP")

battery_power = st.number_input("Kapasitas baterai (MaH)",min_value=501,max_value=1998)
blue = st.number_input("Memiliki Bluetooth atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
clock_speed = st.number_input("Kecepatan processor (dalam GHz)",min_value=0.5,max_value=3.0)
dual_sim = st.number_input("Dual SIM atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
fc = st.number_input("Kamera Depan (Megapixel)",min_value=0,max_value=19)
four_g = st.number_input("Memiliki 4G atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
int_memory = st.number_input("Memory Internal (GB)",min_value=2,max_value=64)
m_dep = st.number_input("Ketebalan hp (dalam cm)",min_value=0.1,max_value=1.0)
mobile_wt = st.number_input("Berat Hp (Gr)",min_value=80,max_value=200)
n_cores = st.number_input("Jumlah core processor",min_value=1,max_value=8)
px_height = st.number_input("Tinggi pixel layar (px)",min_value=0,max_value=1960)
px_width = st.number_input("Lebar pixel Layar (px)",min_value=500,max_value=1998)
pc = st.number_input("Kamera Belakang (Megapixel)",min_value=0,max_value=20)
ram = st.number_input("Ram (dalam Mb)",min_value=256,max_value=3998)
sc_h = st.number_input("Tinggi Layar (inch) ",min_value=5,max_value=19)
sc_w = st.number_input("Lebar Layar (inch)",min_value=1,max_value=18)
talk_time = st.number_input("Talk Time (Lama waktu pakai (jam) satu kali charge)",min_value=2,max_value=20)
three_g = st.number_input("Memiliki 3G atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
touch_screen = st.number_input("Touch screen atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
wifi = st.number_input("Memiliki Wifi atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)


columns = st.columns((2, 0.6, 2))
save = columns[1].button("Submit")


def execute(prediksi):
    with st.spinner("Tunggu Sebentar Masih Proses..."):
        st.write("Golongan ",prediksi[-1])  
        if prediksi[-1]==0:
            st.subheader("Hp anda termasuk hp dengan harga murah")
        if prediksi[-1]==1:
            st.subheader("Hp anda termasuk hp dengan harga sedang")
        if prediksi[-1]==2:
            st.subheader("Hp anda termasuk hp dengan harga mahal")
        if prediksi[-1]==3:
            st.subheader("Hp anda termasuk hp dengan harga sangat mahal")


if save:
    data = Dataset.pisahnormalisasi([battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi])
    prediksi = Dataset.DT(data)
    execute(prediksi)



   


