import tkinter as tk
from tkinter import ttk, scrolledtext
import joblib
import numpy as np

# ---------------------------
# CROP INFORMATION DATABASE
# ---------------------------
CROP_INFO = {
    "rice": {
        "name": "Rice (Riz)",
        "emoji": "🌾",
        "N": "60-120 mg/kg",
        "P": "35-60 mg/kg", 
        "K": "35-50 mg/kg",
        "temp": "20-27°C",
        "humidity": "80-90%",
        "ph": "5.5-7.0",
        "rainfall": "150-300 mm",
        "season": "Kharif (Jun-Nov)",
        "description": "Needs abundant water and warm climate. Grows in clayey, flooded soil."
    },
    "maize": {
        "name": "Maize (Maïs)",
        "emoji": "🌽",
        "N": "75-100 mg/kg",
        "P": "40-60 mg/kg",
        "K": "20-40 mg/kg",
        "temp": "18-27°C",
        "humidity": "60-80%",
        "ph": "5.5-7.0",
        "rainfall": "60-110 mm",
        "season": "Kharif & Rabi",
        "description": "Versatile crop, moderate water needs, well-drained soil required."
    },
    "chickpea": {
        "name": "Chickpea (Pois chiche)",
        "emoji": "🫘",
        "N": "20-60 mg/kg",
        "P": "60-80 mg/kg",
        "K": "70-80 mg/kg",
        "temp": "20-25°C",
        "humidity": "15-20%",
        "ph": "6.0-7.5",
        "rainfall": "60-90 mm",
        "season": "Rabi (Oct-Mar)",
        "description": "Drought resistant, cool climate, well-drained soil."
    },
    "kidneybeans": {
        "name": "Kidney Beans (Haricots rouges)",
        "emoji": "🫘",
        "N": "20-40 mg/kg",
        "P": "60-70 mg/kg",
        "K": "20-30 mg/kg",
        "temp": "15-25°C",
        "humidity": "20-25%",
        "ph": "5.5-6.5",
        "rainfall": "60-80 mm",
        "season": "Rabi",
        "description": "Rich nutrient soil, regular watering, cool to moderate climate."
    },
    "pigeonpeas": {
        "name": "Pigeon Peas (Pois d'Angole)",
        "emoji": "🫛",
        "N": "20-40 mg/kg",
        "P": "60-80 mg/kg",
        "K": "20-40 mg/kg",
        "temp": "20-27°C",
        "humidity": "50-70%",
        "ph": "6.0-7.5",
        "rainfall": "60-100 mm",
        "season": "Kharif",
        "description": "Drought resistant, improves soil fertility, long duration crop."
    },
    "mothbeans": {
        "name": "Moth Beans (Haricots papillon)",
        "emoji": "🫘",
        "N": "20-40 mg/kg",
        "P": "40-60 mg/kg",
        "K": "30-40 mg/kg",
        "temp": "24-30°C",
        "humidity": "15-25%",
        "ph": "6.5-8.0",
        "rainfall": "40-60 mm",
        "season": "Kharif",
        "description": "Very drought resistant, sandy soil, arid climate suitable."
    },
    "mungbean": {
        "name": "Mung Bean (Haricot mungo)",
        "emoji": "🫛",
        "N": "20-40 mg/kg",
        "P": "40-60 mg/kg",
        "K": "20-40 mg/kg",
        "temp": "25-35°C",
        "humidity": "80-90%",
        "ph": "6.5-7.5",
        "rainfall": "80-100 mm",
        "season": "Kharif & Summer",
        "description": "Quick growing, hot climate, well-drained loamy soil."
    },
    "blackgram": {
        "name": "Black Gram (Haricot noir)",
        "emoji": "🫘",
        "N": "30-50 mg/kg",
        "P": "55-75 mg/kg",
        "K": "30-40 mg/kg",
        "temp": "25-35°C",
        "humidity": "60-70%",
        "ph": "6.5-7.5",
        "rainfall": "60-100 mm",
        "season": "Kharif & Rabi",
        "description": "Warm climate, fertile soil, moderate water requirement."
    },
    "lentil": {
        "name": "Lentil (Lentilles)",
        "emoji": "🫛",
        "N": "20-40 mg/kg",
        "P": "60-80 mg/kg",
        "K": "20-40 mg/kg",
        "temp": "18-25°C",
        "humidity": "30-70%",
        "ph": "6.0-8.0",
        "rainfall": "50-70 mm",
        "season": "Rabi",
        "description": "Cool climate, well-drained soil, crop rotation recommended."
    },
    "pomegranate": {
        "name": "Pomegranate (Grenade)",
        "emoji": "🍎",
        "N": "20-40 mg/kg",
        "P": "10-40 mg/kg",
        "K": "40-50 mg/kg",
        "temp": "15-35°C",
        "humidity": "35-45%",
        "ph": "6.5-7.5",
        "rainfall": "50-70 mm",
        "season": "Year-round",
        "description": "Dry climate, well-drained soil, moderate irrigation."
    },
    "banana": {
        "name": "Banana (Banane)",
        "emoji": "🍌",
        "N": "100-120 mg/kg",
        "P": "80-100 mg/kg",
        "K": "50-60 mg/kg",
        "temp": "25-35°C",
        "humidity": "75-85%",
        "ph": "6.0-7.5",
        "rainfall": "100-200 mm",
        "season": "Year-round",
        "description": "Tropical climate, rich soil, abundant watering required."
    },
    "mango": {
        "name": "Mango (Mangue)",
        "emoji": "🥭",
        "N": "20-40 mg/kg",
        "P": "15-25 mg/kg",
        "K": "20-30 mg/kg",
        "temp": "24-30°C",
        "humidity": "50-60%",
        "ph": "5.5-7.5",
        "rainfall": "90-120 mm",
        "season": "Summer",
        "description": "Hot climate, deep soil, irrigation in dry season."
    },
    "grapes": {
        "name": "Grapes (Raisins)",
        "emoji": "🍇",
        "N": "20-60 mg/kg",
        "P": "125-145 mg/kg",
        "K": "200-250 mg/kg",
        "temp": "15-25°C",
        "humidity": "60-80%",
        "ph": "6.0-7.0",
        "rainfall": "50-80 mm",
        "season": "Feb-Mar",
        "description": "Temperate climate, well-drained soil, regular pruning needed."
    },
    "watermelon": {
        "name": "Watermelon (Pastèque)",
        "emoji": "🍉",
        "N": "80-120 mg/kg",
        "P": "40-60 mg/kg",
        "K": "40-60 mg/kg",
        "temp": "24-30°C",
        "humidity": "50-70%",
        "ph": "6.0-7.0",
        "rainfall": "40-60 mm",
        "season": "Summer",
        "description": "Hot climate, sandy loam soil, regular watering."
    },
    "muskmelon": {
        "name": "Muskmelon (Melon)",
        "emoji": "🍈",
        "N": "100-120 mg/kg",
        "P": "50-60 mg/kg",
        "K": "50-60 mg/kg",
        "temp": "25-30°C",
        "humidity": "85-95%",
        "ph": "6.0-7.0",
        "rainfall": "40-60 mm",
        "season": "Summer",
        "description": "Hot climate, fertile soil, good drainage essential."
    },
    "apple": {
        "name": "Apple (Pomme)",
        "emoji": "🍎",
        "N": "20-40 mg/kg",
        "P": "125-145 mg/kg",
        "K": "200-225 mg/kg",
        "temp": "18-24°C",
        "humidity": "60-70%",
        "ph": "5.5-6.5",
        "rainfall": "100-125 mm",
        "season": "Winter chill required",
        "description": "Cool climate, deep soil, annual pruning required."
    },
    "orange": {
        "name": "Orange",
        "emoji": "🍊",
        "N": "20-40 mg/kg",
        "P": "10-20 mg/kg",
        "K": "10-20 mg/kg",
        "temp": "15-30°C",
        "humidity": "70-80%",
        "ph": "6.0-7.5",
        "rainfall": "100-120 mm",
        "season": "Year-round",
        "description": "Subtropical climate, well-drained soil, regular irrigation."
    },
    "papaya": {
        "name": "Papaya (Papaye)",
        "emoji": "🫒",
        "N": "50-100 mg/kg",
        "P": "50-100 mg/kg",
        "K": "50-100 mg/kg",
        "temp": "25-35°C",
        "humidity": "50-60%",
        "ph": "6.0-6.5",
        "rainfall": "120-150 mm",
        "season": "Year-round",
        "description": "Tropical climate, rich soil, constant watering."
    },
    "coconut": {
        "name": "Coconut (Noix de coco)",
        "emoji": "🥥",
        "N": "20-30 mg/kg",
        "P": "10-20 mg/kg",
        "K": "20-30 mg/kg",
        "temp": "27-32°C",
        "humidity": "70-80%",
        "ph": "5.5-7.0",
        "rainfall": "175-250 mm",
        "season": "Year-round",
        "description": "Tropical coastal climate, sandy soil, high humidity."
    },
    "cotton": {
        "name": "Cotton (Coton)",
        "emoji": "🌸",
        "N": "115-125 mg/kg",
        "P": "40-50 mg/kg",
        "K": "40-50 mg/kg",
        "temp": "23-32°C",
        "humidity": "60-70%",
        "ph": "6.5-8.0",
        "rainfall": "60-100 mm",
        "season": "Kharif",
        "description": "Hot climate, black cotton soil, controlled irrigation."
    },
    "jute": {
        "name": "Jute",
        "emoji": "🌿",
        "N": "80-100 mg/kg",
        "P": "40-50 mg/kg",
        "K": "40-50 mg/kg",
        "temp": "25-35°C",
        "humidity": "70-80%",
        "ph": "6.0-7.0",
        "rainfall": "150-250 mm",
        "season": "Kharif",
        "description": "Humid climate, alluvial soil, abundant water needed."
    },
    "coffee": {
        "name": "Coffee (Café)",
        "emoji": "☕",
        "N": "100-120 mg/kg",
        "P": "20-30 mg/kg",
        "K": "20-30 mg/kg",
        "temp": "15-28°C",
        "humidity": "70-80%",
        "ph": "6.0-6.5",
        "rainfall": "150-200 mm",
        "season": "Year-round",
        "description": "Medium altitude, partial shade, acidic soil required."
    }
}

# ---------------------------
# LOAD MODEL AND SCALER
# ---------------------------
try:
    model = joblib.load("model.joblib")
    scaler = joblib.load("scaler.joblib")
    print("Modèles chargés avec succès!")
except FileNotFoundError:
    print("Erreur: Fichiers model.joblib ou scaler.joblib non trouvés!")
    exit()

# ---------------------------
# PREDICTION FUNCTION
# ---------------------------
def predict_crop():
    try:
        N = float(entry_N.get())
        P = float(entry_P.get())
        K = float(entry_K.get())
        temperature = float(entry_temp.get())
        humidity = float(entry_hum.get())
        ph = float(entry_ph.get())
        rainfall = float(entry_rain.get())

        # Prepare input
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        data_scaled = scaler.transform(data)

        # Predict crop
        prediction = model.predict(data_scaled)[0]
        
        # Get probability (if available)
        try:
            probabilities = model.predict_proba(data_scaled)[0]
            result_text = f"🎯 Recommended Crop\n\n{prediction.upper()}"
        except:
            result_text = f"🎯 Recommended Crop\n\n{prediction.upper()}"

        # Show result
        result_label.config(text=result_text, bg='#2ecc71', fg='white')

    except ValueError:
        result_label.config(text="❌ Error\n\nPlease enter\nvalid numbers!", bg='#e74c3c', fg='white')
    except Exception as e:
        result_label.config(text=f"❌ Error\n\n{str(e)[:30]}", bg='#e74c3c', fg='white')

def clear_fields():
    """Effacer tous les champs"""
    for entry in entries:
        entry.delete(0, tk.END)
    result_label.config(text="Enter values and click PREDICT", bg='#ecf0f1', fg='#2c3e50')

def show_crop_info():
    """Afficher la fenêtre d'informations sur les cultures"""
    info_window = tk.Toplevel(root)
    info_window.title("🌾 Crop Information Database")
    info_window.geometry("700x600")
    info_window.configure(bg='#ffffff')
    
    # Header
    header = tk.Frame(info_window, bg='#1e8449', height=60)
    header.pack(fill='x')
    
    title = tk.Label(
        header,
        text="Crop Growing Conditions Database",
        font=("Arial", 16, "bold"),
        bg='#1e8449',
        fg='#ffffff'
    )
    title.pack(pady=15)
    
    # Search frame
    search_frame = tk.Frame(info_window, bg='#ffffff')
    search_frame.pack(fill='x', padx=20, pady=10)
    
    tk.Label(
        search_frame,
        text="Select Crop:",
        font=("Arial", 11, "bold"),
        bg='#ffffff',
        fg='#1e8449'
    ).pack(side='left', padx=(0, 10))
    
    crop_var = tk.StringVar()
    crop_names = sorted(CROP_INFO.keys())
    
    crop_dropdown = ttk.Combobox(
        search_frame,
        textvariable=crop_var,
        values=crop_names,
        state='readonly',
        font=("Arial", 10),
        width=20
    )
    crop_dropdown.pack(side='left')
    crop_dropdown.set(crop_names[0])
    
    # Info display area
    info_text = scrolledtext.ScrolledText(
        info_window,
        wrap=tk.WORD,
        width=80,
        height=20,
        font=("Arial", 10),
        bg='#f8f9fa',
        fg='#2c3e50',
        padx=15,
        pady=15
    )
    info_text.pack(fill='both', expand=True, padx=20, pady=10)
    
    def update_info(*args):
        """Mettre à jour l'affichage des informations"""
        selected = crop_var.get()
        info = CROP_INFO.get(selected, {})
        
        info_text.config(state='normal')
        info_text.delete(1.0, tk.END)
        
        if info:
            display_text = f"""
{info['emoji']} {info['name'].upper()}
{'=' * 60}

📊 OPTIMAL GROWING CONDITIONS:

💊 Nitrogen (N):        {info['N']}
💊 Phosphorus (P):      {info['P']}
💊 Potassium (K):       {info['K']}

🌡 Temperature:         {info['temp']}
💧 Humidity:            {info['humidity']}
🧪 pH Level:            {info['ph']}
🌧 Rainfall:            {info['rainfall']}

📅 Growing Season:      {info['season']}

📝 DESCRIPTION:
{info['description']}

{'=' * 60}

💡 TIP: These values represent optimal ranges for maximum yield.
Values outside these ranges may still grow but with reduced productivity.
"""
            info_text.insert(1.0, display_text)
        
        info_text.config(state='disabled')
    
    crop_var.trace('w', update_info)
    update_info()
    
    # Show all button
    def show_all_crops():
        info_text.config(state='normal')
        info_text.delete(1.0, tk.END)
        
        all_text = "ALL CROPS QUICK REFERENCE\n"
        all_text += "=" * 70 + "\n\n"
        
        for crop_key in sorted(CROP_INFO.keys()):
            info = CROP_INFO[crop_key]
            all_text += f"{info['emoji']} {info['name']}\n"
            all_text += f"   N: {info['N']} | P: {info['P']} | K: {info['K']}\n"
            all_text += f"   Temp: {info['temp']} | pH: {info['ph']} | Rain: {info['rainfall']}\n\n"
        
        info_text.insert(1.0, all_text)
        info_text.config(state='disabled')
    
    # Buttons frame
    btn_frame = tk.Frame(info_window, bg='#ffffff')
    btn_frame.pack(fill='x', padx=20, pady=(0, 15))
    
    tk.Button(
        btn_frame,
        text="Show All Crops",
        command=show_all_crops,
        font=("Arial", 10, "bold"),
        bg='#3498db',
        fg='white',
        cursor='hand2',
        relief='flat',
        bd=0,
        width=15,
        height=2
    ).pack(side='left', padx=5)
    
    tk.Button(
        btn_frame,
        text="❌ Close",
        command=info_window.destroy,
        font=("Arial", 10, "bold"),
        bg='#e74c3c',
        fg='white',
        cursor='hand2',
        relief='flat',
        bd=0,
        width=15,
        height=2
    ).pack(side='right', padx=5)

# ---------------------------
# TKINTER INTERFACE
# ---------------------------
root = tk.Tk()
root.title("🌾 AgriHelp - Crop Recommendation System")
root.geometry("500x720")
root.resizable(False, False)
root.configure(bg='#f5f5f5')

# Frame principal
main_frame = tk.Frame(root, bg='#ffffff')
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# ---------------------------
# HEADER
# ---------------------------
header_frame = tk.Frame(main_frame, bg='#1e8449', height=100)
header_frame.pack(fill='x')

# Logo/Icon
logo_label = tk.Label(
    header_frame,
    text="🌾",
    font=("Arial", 36),
    bg='#1e8449',
    fg='#ffffff'
)
logo_label.pack(pady=(10, 0))

title_label = tk.Label(
    header_frame,
    text="AgriHelp",
    font=("Arial", 24, "bold"),
    bg='#1e8449',
    fg='#ffffff'
)
title_label.pack()

subtitle_label = tk.Label(
    header_frame,
    text="Smart Crop Recommendation System",
    font=("Arial", 10),
    bg='#1e8449',
    fg='#a9dfbf'
)
subtitle_label.pack(pady=(0, 10))

# ---------------------------
# INPUT SECTION
# ---------------------------
input_container = tk.Frame(main_frame, bg='#ffffff')
input_container.pack(fill='both', expand=True, padx=20, pady=(15, 5))

section_title = tk.Label(
    input_container,
    text="Soil & Climate Parameters",
    font=("Arial", 13, "bold"),
    bg='#ffffff',
    fg='#1e8449'
)
section_title.pack(pady=(0, 12))

# Données des labels
labels_data = [
    ("💊 Nitrogen (N)", "mg/kg", "#27ae60"),
    ("💊 Phosphorus (P)", "mg/kg", "#27ae60"),
    ("💊 Potassium (K)", "mg/kg", "#27ae60"),
    ("🌡 Temperature", "°C", "#e67e22"),
    ("💧 Humidity", "%", "#3498db"),
    ("🧪 pH Level", "", "#9b59b6"),
    ("🌧 Rainfall", "mm", "#3498db")
]

entries = []

for label_text, unit, color in labels_data:
    # Frame pour chaque ligne
    row_frame = tk.Frame(input_container, bg='#ffffff')
    row_frame.pack(fill='x', pady=4)
    
    # Label avec couleur
    lbl = tk.Label(
        row_frame,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg='#ffffff',
        fg=color,
        anchor='w',
        width=18
    )
    lbl.pack(side='left')
    
    # Entry stylé
    entry = tk.Entry(
        row_frame,
        font=("Arial", 10),
        bg='#ecf0f1',
        fg='#2c3e50',
        relief='solid',
        bd=1,
        width=10,
        justify='center'
    )
    entry.pack(side='right', padx=(5, 0))
    
    # Unit
    if unit:
        unit_lbl = tk.Label(
            row_frame,
            text=unit,
            font=("Arial", 9),
            bg='#ffffff',
            fg='#7f8c8d',
            width=6
        )
        unit_lbl.pack(side='right')
    
    entries.append(entry)

(entry_N, entry_P, entry_K,
 entry_temp, entry_hum,
 entry_ph, entry_rain) = entries

# ---------------------------
# BUTTONS
# ---------------------------
buttons_frame = tk.Frame(main_frame, bg='#ffffff')
buttons_frame.pack(pady=8)

# Predict Button
predict_btn = tk.Button(
    buttons_frame,
    text="CROP TYPE",
    command=predict_crop,
    font=("Arial", 11, "bold"),
    bg='#27ae60',
    fg='white',
    activebackground='#229954',
    activeforeground='white',
    cursor='hand2',
    relief='flat',
    bd=0,
    width=14,
    height=2
)
predict_btn.pack(side='left', padx=4)

# Clear Button
clear_btn = tk.Button(
    buttons_frame,
    text="CLEAR",
    command=clear_fields,
    font=("Arial", 11, "bold"),
    bg='#e67e22',
    fg='white',
    activebackground='#d35400',
    activeforeground='white',
    cursor='hand2',
    relief='flat',
    bd=0,
    width=9,
    height=2
)
clear_btn.pack(side='left', padx=4)

# Info Button
info_btn = tk.Button(
    buttons_frame,
    text="INFO",
    command=show_crop_info,
    font=("Arial", 11, "bold"),
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    activeforeground='white',
    cursor='hand2',
    relief='flat',
    bd=0,
    width=9,
    height=2
)
info_btn.pack(side='left', padx=4)

# ---------------------------
# RESULT SECTION
# ---------------------------
result_label = tk.Label(
    main_frame,
    text="Enter values and click PREDICT",
    font=("Arial", 11, "bold"),
    bg='#ecf0f1',
    fg='#2c3e50',
    justify='center',
    relief='flat',
    bd=0,
    pady=15
)
result_label.pack(fill='x', padx=20, pady=(0, 12))

# ---------------------------
# HOVER EFFECTS
# ---------------------------
def create_hover_effect(button, normal_color, hover_color):
    def on_enter(e):
        button.config(bg=hover_color)
    def on_leave(e):
        button.config(bg=normal_color)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

create_hover_effect(predict_btn, '#27ae60', '#229954')
create_hover_effect(clear_btn, '#e67e22', '#d35400')
create_hover_effect(info_btn, '#3498db', '#2980b9')

# ---------------------------
# START APPLICATION
# ---------------------------
print("=" * 50)
print("🌾 AGRIPREDICT - Crop Recommendation System")
print("=" * 50)
print("✅ Application lancée avec succès!")
print("📊 Entrez les paramètres du sol et du climat")
print("🚀 Cliquez sur PREDICT pour obtenir la recommandation")
print("=" * 50)

root.mainloop()