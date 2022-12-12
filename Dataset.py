import joblib
import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

st.title("Studi Kasus Mobile Price Classification")
st.header("Link Dataset")
st.subheader("https://raw.githubusercontent.com/rahadis/datamining/main/train.csv")
st.header("Link Github")
st.subheader("https://github.com/rahadis")

st.header("Mobile Price Classification Dataset")
data = pd.read_csv('Final/Mobilepricefinal.csv')
data = data.drop(data.columns[0],axis=1)
df=pd.DataFrame(data)
st.dataframe(df)

st.subheader("Penjelasan")
st.write("battery_power = Kapasitas Baterai")
st.write("blue = bluetooth ") 
st.write("clock_speed = Kecepatan Processor") 
st.write("dual_sim = Dual sim") 
st.write("fc = Kamera Depan") 
st.write("four_g = Jaringan 4G") 
st.write("int_memory = Memori internal") 
st.write("m_dep = Ketebalan HP") 
st.write("mobile_wt = Berat HP") 
st.write("n_cores = Jumlah Core GPU") 
st.write("pc = Kamera utama") 
st.write("px_height = Tinggi Resolusi Layar ") 
st.write("px_width = Lebar Resolusi Layar") 
st.write("ram = RAM") 
st.write("sc_h = Tinggi Layar") 
st.write("sc_w = Lebar Layar") 
st.write("talk_time =Lama waktu pakai satu kali charge ") 
st.write("three_g = Jaringan 3G") 
st.write("touch_screen = Layar Sentuh") 
st.write("wifi = Layanan Wi-Fi") 




def pisahnormalisasi(data):

    cols = ["battery_power", "clock_speed", "fc", "int_memory", "m_dep", "mobile_wt", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi"]
    df = pd.DataFrame([data],columns=cols)
    data_test = pd.read_csv('Final/Datafinal.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    data_final = data_test.append(df,ignore_index = True)


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
    
    return scaled_fitur

def DT(x):
    return joblib.load('Final/Model/DTFinal.pkl').predict(x)
def NB(x):
    return joblib.load('Final/Model/ModelNBFinal.pkl').predict(x)
def ranforest(x):
    return joblib.load('Final/Model/randomforestfinal.pkl').predict(x)

def tanpanormalisasi(data):
    cols = ["battery_power", "clock_speed", "fc", "int_memory", "m_dep", "mobile_wt", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi"]
    df = pd.DataFrame([data],columns=cols)
    data_test = pd.read_csv('Final/Datafinal.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1) 
    data_final = data_test.append(df,ignore_index = True)
    return data_final





