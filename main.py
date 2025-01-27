import streamlit as st

import pandas as pd
import os
from fnmatch import fnmatch
from datetime import datetime

st.set_page_config(layout="wide")

acronimos = {
  "L'Hospitalet de Llobregat": "LHOS",
  "Barcelona-Sants": "BSAN",
  "Barcelona-Plaça de Catalunya": "BPCN",
  "Barcelona-Arc de Triomf": "BATR",
  "Barcelona-La Sagrera-Meridiana": "BLSG",
  "Barcelona-Fabra i Puig": "BFAB",
  "Barcelona-Torre Baró | Vallbona": "BTBV",
  "Montcada Bifurcació": "MBCF",
  "Montcada Ripollet": "MCRI",
  "Santa Perpètua de Mogoda La Florida": "SPMF",
  "Mollet-Santa Rosa": "MSRS",
  "Parets del Vallès": "PDVA",
  "Granollers-Canovelles": "GRCA",
  "Les Franqueses del Vallès": "LFVA",
  "La Garriga": "LGAR",
  "Figaró": "FIGA",
  "Sant Martí de Centelles": "SMCE",
  "Centelles": "CENL",
  "Balenyà-Els Hostalets": "BEHO",
  "Balenyà-Tona-Seva": "BTSV",
  "Vic": "VICC",
  "Manlleu": "MANL",
  "Torelló": "TORE",
  "Borgonyà": "BORG",
  "Sant Quirze de Besora": "SQBE",
  "La Farga de Bebié": "LFBE",
  "Ripoll": "RIPO",
  "Campdevànol": "CAMP",
  "Ribes de Freser": "RIFE",
  "Planoles": "PLAN",
  "Toses": "TOSE",
  "La Molina": "LMOL",
  "Urtx-Alp": "UALP",
  "Puigcerdà": "PUIG",
  "La Tor de Querol-Enveig": "LTQV"
}

with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image('images/logo.jpeg', width=300)

        st.write(f'<div style="text-align: left; font-size: 60px;"><b>Perquè no ens fotin el tren</b></div>',
             unsafe_allow_html=True
             )
        
        st.write('<div style="text-align: left; font-size: 20px;"><b>Grup de defensa de la línia R3 de Rodalies \
                 de Catalunya <br> (l\'Hospitalet de Llobregat - la Tor de Querol-Enveig)</b></div>',
             unsafe_allow_html=True
             )
        st.markdown("#")
    with col2:
        st.markdown("\
                    La red de Cercanías del núcleo de Barcelona (Rodalies de Catalunya), que conecta la capital catalana con \
                    diversas localidades de su área metropolitana y alrededores, atraviesa actualmente una fase crítica \
                    de problemas recurrentes. La **alta demanda**, la **falta de inversiones adecuadas** y \
                    la **deficiencia en la modernización de infraestructuras** han generado un malestar generalizado entre los usuarios. \
                    Muchos pasajeros se ven obligados a enfrentarse a retrasos constantes, fallos en la puntualidad y \
                    una falta de confort en los trenes, lo que afecta no solo la calidad del servicio, sino también la vida diaria \
                    de miles de personas que dependen de esta red para su movilidad.")
        st.markdown("Además, la **falta de comunicación efectiva** sobre los **cambios**, **retrasos** o **incidencias** \
                    hace que los usuarios se sientan frustrados, ya que no cuentan con información clara y en tiempo real \
                    para planificar sus viajes. Esto, combinado con los problemas de saturación en las horas punta, crea un \
                    ambiente de insatisfacción generalizada.")
        st.markdown("En respuesta a las crecientes preocupaciones sobre los retrasos en la línea R3 de Rodalies de Barcelona, \
                    hemos creado una plataforma web interactiva diseñada para estudiar y analizar detalladamente \
                    los problemas de puntualidad que afectan a esta línea.")

    st.divider()

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("""<div style="padding: 20px; background-color: #E9001A">
                            <div style="color:#ffffff; font-size:45px"><b>Datos<b></div>
                            <div style="color:#ffffff; font-size:20px">Los datos tienen como origen las fuentes de datos oficiales: Renfe-Rodalies como operador del servicio y Adif como gestor de la infraestructura ferroviaria</div>                            
                            <!--<div style="color:#ffffff; font-size:20px"><b>oficinas<b></div>-->
                        </div>""",
                        unsafe_allow_html=True
                        )

    with col2:
        st.write("""<div style="padding: 20px; background-color: #E9001A">
                            <div style="color:#ffffff; font-size:45px"><b>Fechas<b></div>
                            <div style="color:#ffffff; font-size:20px">Se han estudiado todas las circulaciones de la línea entre el 13 de enero 2025 y el 26 de enero de 2025, inclusive, en ambos sentidos de circulación</div>                            
                            <!--<div style="color:#ffffff; font-size:20px"><b>oficinas<b></div>-->
                        </div>""",
                        unsafe_allow_html=True
                        )

    with col3:
        st.write("""<div style="padding: 20px; background-color: #E9001A">
                            <div style="color:#ffffff; font-size:45px"><b>Resultados<b></div>
                            <div style="color:#ffffff; font-size:20px">Se tienen datos para cada día y sentido, con el detalle del número de tren, la hora de salida y el retraso tras el paso por cada estación de la línea</div>                            
                            <!--<div style="color:#ffffff; font-size:20px"><b>oficinas<b></div>-->
                        </div>""",
                        unsafe_allow_html=True
                        )

    with col4:
        st.write("""<div style="padding: 20px; background-color: #E9001A">
                            <div style="color:#ffffff; font-size:45px"><b>Simbología<b></div>
                            <div style="color:#ffffff; font-size:20px">Atendiendo al tiempo de retraso se ha asignado el siguiente código de color: verde (< 3 minutos), amarillo (4 y 7 min.), naranja (8 y 14 min.) y rojo (>15 min.)</div>                            
                            <!--<div style="color:#ffffff; font-size:20px"><b>oficinas<b></div>-->
                        </div>""",
                        unsafe_allow_html=True
                        )
    
    st.write('')
    st.error('**Importante:** Debido a la escasa información proporcionada desde los orígenes de datos es imposible determinar qué trenes o circulaciones han resultado canceladas.')
    st.info('**Nota:** Las paradas han sido renombradas para una mejor visualización de los datos.')
    st.divider()


all_dates = []
all_ways = ['Ida (LHOS -> LTQV)', 'Vuelta (LTQV -> LHOS)']

for file in os.listdir('data'):
    if fnmatch(file, '*-*.csv'):
        _date = file.split('-')[0]
        all_dates.append(datetime.strptime(_date, "%Y%m%d").date())

all_dates = set(all_dates)

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('## Visualiza los datos')
        st.markdown('Selecciona un día y un sentido')

    with col2:
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            opcion_fecha = None
            opcion_sentido = None

            # Crear un desplegable con opciones
            opcion_fecha = st.selectbox(
                'Selecciona un día',  # Título del desplegable
                [''] + sorted(all_dates)  # Opciones disponibles
            )

        with col2_2:
            if opcion_fecha:
                opcion_sentido = st.selectbox(
                    'Selecciona el sentido',  # Título del desplegable
                    [''] + all_ways,  # Opciones disponibles
                )

            if opcion_fecha and opcion_sentido:
                _opcion_fecha = str(opcion_fecha).replace('-', '')
                _opcion_sentido = None

                if 'Ida' in opcion_sentido:
                    _opcion_sentido = 'ida'
                else:
                    _opcion_sentido = 'vuelta'

                data = pd.read_csv(f'data/{_opcion_fecha}-R3-{_opcion_sentido}.csv')
                data['Tren'] = data['Tren'].astype(str)

                

                def color_celdas(val):
                    if isinstance(val, (int, float)):  # Verificar si el valor es numérico
                        if val <= 3:
                            color = '#6AA84F'
                        elif 4 <= val <= 7:
                            color = '#F1C232'
                        elif 8 <= val <= 14:
                            color = '#E69138'
                        elif val >= 15:
                            color = '#CC0000'
                        else:
                            color = ''
                        return f'background-color: {color}'
                    else:
                        return ''  # No aplicar color si no es un valor numérico
                        
                # Formatear solo las columnas numéricas sin decimales
                styled_df = data.style.map(color_celdas)

                # Aplicar el formato para las columnas numéricas sin decimales
                styled_df = styled_df.format({col: "{:.0f}" for col in data.select_dtypes(include=['number']).columns})

    with col3:
        col3_1, col3_2, col3_3 = st.columns([1, 2, 1])

        with col3_1:
            a = 1
        
        with col3_2:
            if 'data' in locals():
                data_csv = data.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="Descargar datos",
                    data=data_csv,
                    file_name=f'{_opcion_fecha}-R3-{_opcion_sentido}.csv',
                    mime="text/csv"
                )

        with col3_3:
            a = 1
    with col4:
        col4_1, col4_2, col4_3 = st.columns([1, 2, 1])

        with col4_1:
            a = 1
        
        with col4_2:
            if 'data' in locals():
                correspondencia = pd.read_csv('data/acronimos.csv', sep = ',')
                correspondencia_csv = correspondencia.to_csv(index = False)

                st.download_button(
                    label="Descargar paradas",
                    data=correspondencia_csv,
                    file_name = 'correspondencia_paradas.csv',
                    mime="text/csv"
                )

        with col4_3:
            a = 1
        

st.write('')

with st.container():
    if 'styled_df' in locals():  # Verificar que df ha sido generado
        st.dataframe(styled_df, hide_index = True, height=800)
