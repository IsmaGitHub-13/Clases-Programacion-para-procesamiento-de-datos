import pyodbc
import PyPDF2
import os
server = r'DESKTOP-UV0H31O\SQLEXPRESS' 
database = 'BaseDatosPDF' 

connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

def extraer_texto_pdf(ruta_pdf):
    texto_extraido = ""
    try:
        with open(ruta_pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                texto_extraido += page.extract_text()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_pdf}")
        return None
    except Exception as e:
        print(f"Ocurrió un error leyendo el PDF: {e}")
        return None
    return texto_extraido

def guardar_en_sql_server(nombre_archivo, texto):
    try:
    
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
    
        query = "INSERT INTO Documentos (NombreArchivo, Contenido) VALUES (?, ?)"
        
        cursor.execute(query, (nombre_archivo, texto))
        
        conn.commit()
        conn.close()
        print("----------------------------------------------------")
        print(f"¡LISTO! Se guardó '{nombre_archivo}' en SQL Server.")
        print("----------------------------------------------------")
        
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        print("NOTA: Si dice 'Data source name not found', intenta cambiar el DRIVER a '{SQL Server}'")
        
if __name__ == "__main__":
    ruta_mi_pdf = r"C:\Users\alcan\OneDrive\Documentos\hola2.pdf"
    
    print("1. Extrayendo texto del PDF...")
    contenido = extraer_texto_pdf(ruta_mi_pdf)
    
    if contenido:
        print("2. Conectando a SQL Server...")
        nombre_del_archivo = os.path.basename(ruta_mi_pdf)
        guardar_en_sql_server(nombre_del_archivo, contenido)
    else:
        print("No se pudo leer el contenido para guardar.")