#import library yg dibutuhkan
import streamlit as st 

#Part 1 - text element
st.title("Praktikum 1 Visualisasi Data") #ini untuk judul
st.header("Text Elements dengan header") #utk buat header
st.subheader("ini sub header") #utk buat sub judul
st.text("ini teks b aja") #utk teks biasa 
st.markdown("**ini teks bold** dan *ini italic*") #utk format teks jd bold/italic
st.markdown("""
- ini baris 1
- baris 2
1. ini baris 1
2. ini baris 2
* ini baris 1
* ini baris 2
            """)
st.caption("ini untuk buat caption") #untuk buat teks kecil untuk penjelasan

#TRY URSELF
#1. tuliskan judul praktikum pakai judul
st.title("praktikum 1 visdat")
#2.bagian praktikum pakai header
st.subheader("praktikum bagian 1")
#3. nama lengkap anggota - NIM pakai markdown
st.markdown("""
            1. Muhammad Nur Faqih (0110122007)
            2. Nasywa Dhiya Ulhaq (0110221031)
            3. July Ismail (0110221024)
            """)

#Bagian 2: menampilkan rumus pake latex
st.header("Displaying LaTex")
st.subheader("Rumus")
st.latex(r'''\cos^2\theta = 1-2\sin^2\theta''') #rumus trigonometri
st.latex(''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binominal

#Bagian 3: Menampilkan kode program
st.header("Displaying Code")
st.subheader("Python code")
#simpan ke variable code
code = '''
def hello():
    print("Hello, streamlit!")
'''
st.code(code, language='python') #menampilkan kode nya

st.subheader("Java code")
st.code("""
public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello world");
        }
}
        """, language='java')

st.subheader("Javascript Code")
st.code("""
<script>
try {
    addalert("welcome guest!); //kesalahan ketik (addalert) sengaja untuk menimbulkan eror
}
catch(err){
    document.getElementById("demo").innerHTML = err.message; //menampilkan pesan eror di elemen HTML dengan id 'demo'
}
</script>
        """, language='javascript')

