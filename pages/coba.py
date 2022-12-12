import streamlit as st
import pandas as pd
import joblib

from sklearn.preprocessing import MinMaxScaler
def coba(x):
    # import data test
    cols = ["battery_power", "clock_speed", "fc", "int_memory", "m_dep", "mobile_wt", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi"]
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('Pendat/Datafinal.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test.append(df,ignore_index = True)
    # return data_test yang sudah dinormalisasi
    #return joblib.load('Pendat/Normalisasifinal.sav').fit_transform(data_test)
    return data_test



st.subheader("Prediksi harga hp")

battery_power = st.number_input("Kapasitas baterai",min_value=501,max_value=1998)
blue = st.number_input("Memiliki Bluetooth atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
clock_speed = st.number_input("Kecepatan processor (dalam GHz)",min_value=0.5,max_value=3.0)
dual_sim = st.number_input("Dual SIM atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
fc = st.number_input("Kamera Depan",min_value=0,max_value=19)
four_g = st.number_input("Memiliki 4G atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
int_memory = st.number_input("Memory Internal",min_value=2,max_value=64)
m_dep = st.number_input("Ketebalan hp (dalam cm)",min_value=0.1,max_value=1.0)
mobile_wt = st.number_input("Berat Hp (Gr)",min_value=80,max_value=200)
n_cores = st.number_input("Jumlah core processor",min_value=1,max_value=8)
px_height = st.number_input("Tinggi pixel layar",min_value=0,max_value=1960)
px_width = st.number_input("Lebar pixel Layar",min_value=500,max_value=1998)
pc = st.number_input("Kamera Belakang",min_value=0,max_value=20)
ram = st.number_input("Ram (dalam Mb)",min_value=256,max_value=3998)
sc_h = st.number_input("Tinggi Layar",min_value=5,max_value=19)
sc_w = st.number_input("Lebar Layar",min_value=0,max_value=18)
talk_time = st.number_input("Talk Time (Lama waktu pakai satu kali charge)",min_value=2,max_value=20)
three_g = st.number_input("Memiliki 3G atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
touch_screen = st.number_input("Touch screen atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)
wifi = st.number_input("Memiliki Wifi atau tidak (0=TIDAK,1=YA)",min_value=0,max_value=1)


columns = st.columns((2, 0.6, 2))
save = columns[1].button("Submit")

if save:
    # normalisasi data
    data = [battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi]
    cols = ["battery_power", "clock_speed", "fc", "int_memory", "m_dep", "mobile_wt", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi"]
    df = pd.DataFrame([data],columns=cols)
    st.write("Sebelum",df)
    #data_test = pd.read_csv('Pendat/Datafinal.csv')
    #data_test = pd.read_csv('Coba/Tanpa/Datafinal.csv')
    data_test = pd.read_csv('Final/Datafinal.csv')
    #data_test = pd.read_csv('Final/Datafinal (4).csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    st.write("data_test ",data_test)

    data_final = data_test.append(df,ignore_index = True)
    st.write("data_testfinal ",data_final)
    
    from sklearn.preprocessing import MinMaxScaler
    p = data_final.drop(columns=['blue', 'dual_sim', 'four_g' , 'three_g', 'touch_screen', 'wifi'],axis=1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(p)
    nama_fitur = p.columns.copy()
    scaled_fitur_p = pd.DataFrame(scaled,columns=nama_fitur)
    
    q = data_final.drop(columns=['battery_power','clock_speed','fc','int_memory','n_cores','pc','ram','m_dep', 'mobile_wt', 'px_height', 'px_width', 'sc_h', 'sc_w', 'talk_time'],axis=1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(q)
    nama_fitur = q.columns.copy()
    scaled_fitur_q = pd.DataFrame(scaled,columns=nama_fitur)
    
    scaled_fitur = scaled_fitur_p.join(scaled_fitur_q)


    st.write("Sudah normalisasi ",scaled_fitur)
   
  
    #prediksi1 = joblib.load('Pendat/Model/randomforestfinal.pkl').predict(scaled_fitur)
    #prediksi2 = joblib.load('Pendat/Model/ModelNBFinal.pkl').predict(scaled_fitur)
    #prediksi3 = joblib.load('Pendat/Model/DTFinal.pkl').predict(scaled_fitur)
    
    prediksi1 = joblib.load('Pendat/Model/randomforestfinal.pkl').predict(data_final)
    prediksi2 = joblib.load('Pendat/Model/ModelNBFinal.pkl').predict(data_final)
    prediksi3 = joblib.load('Pendat/Model/DTFinal.pkl').predict(data_final)


    with st.spinner("Tunggu Sebentar Masih Proses..."):
        st.write("prediksi1",prediksi1)  
        st.write("Golongan ",prediksi1[-1])  

        st.write("prediksi2",prediksi2) 
        
        st.write("Golongan ",prediksi2[-1])

        st.write("prediksi3",prediksi3) 
        
        st.write("Golongan ",prediksi3[-1])  
