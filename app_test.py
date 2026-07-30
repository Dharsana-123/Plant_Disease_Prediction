import streamlit as st
st.error("NEW VERSION RUNNING - TAMIL UPDATE")
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

@st.cache_resource
def load_disease_model():
    return load_model("plant_disease_model.h5")

model = load_disease_model()
st.set_page_config(
    page_title="SmartCrop AI",
    page_icon="🌱",
    layout="wide"
)
# ---------------- UI Design ----------------

st.markdown("""
<style>
.main {
    background-color: #F5FFF5;
}

h1 {
    color: #228B22;
    text-align: center;
}

h2 {
    color: #2E8B57;
}

.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<h1>🌱 SmartCrop AI</h1>
<h3 style='text-align:center;'>
AI-powered Plant Disease Detection & Farming Assistant
</h3>
<hr>
""", unsafe_allow_html=True)
st.sidebar.markdown("""
# 🌱 SmartCrop AI

### 🌿 AI Farming Assistant

---
### ✅ Features

- 🌱 Disease Detection
- 🌾 Crop Recommendation
- 💊 Treatment Advice
- 🌿 Fertilizer Recommendation
- 💧 Watering Advice
- 🌦 Seasonal Farming Tips
- 🌐 English & தமிழ்

---
### 👩‍💻 Developer

**Dharsana**

Version **1.0**
""")

# ---------------- About ----------------
st.markdown("---")
st.subheader("ℹ️ About SmartCrop AI")
st.write("""
SmartCrop AI is a deep learning-based application that helps identify plant diseases from leaf images.

It is designed to support farmers by enabling faster disease detection.
""")

# ---------------- Language ----------------
language = st.selectbox(
    "🌐 Choose Language / மொழியை தேர்ந்தெடுக்கவும்",
    ["English", "தமிழ்"],
    key="language1"
)
st.write("Selected Language:", language)

if language == "English":
    st.title("🌱 Plant Disease Prediction")
    st.write("Upload a plant leaf image to predict the disease.")
else:
    st.title("🌱 தாவர நோய் கண்டறிதல்")
    st.write("தாவர இலை படத்தை பதிவேற்றி நோயை கண்டறியவும்.")

# 👇 ADD STEP 1 HERE
# Season Selection

if language == "English":
    season = st.selectbox(
        "🌦 Select Current Season",
        ["Summer", "Monsoon", "Winter"],
        key="season1"
    )

else:
    season_tamil = st.selectbox(
        "🌦 தற்போதைய பருவத்தை தேர்வு செய்யவும்",
        ["கோடை", "மழைக்காலம்", "குளிர்காலம்"],
        key="season1"
    )

    season_map = {
        "கோடை": "Summer",
        "மழைக்காலம்": "Monsoon",
        "குளிர்காலம்": "Winter"
    }

    season = season_map[season_tamil]
# ---------------- Upload ----------------
if language == "English":
    uploaded_file = st.file_uploader(
        "Choose a plant image",
        type=["jpg", "jpeg", "png"]
    )
else:
    uploaded_file = st.file_uploader(
        "தாவர இலை படத்தை தேர்வு செய்யவும்",
        type=["jpg", "jpeg", "png"]
    )

# ---------------- Dictionaries ----------------

treatments = {
    "Apple___healthy": "No treatment needed. Keep watering regularly and monitor the plant.",
    "Tomato___Early_blight": "Remove infected leaves, apply a recommended fungicide, and avoid overhead watering.",
    "Tomato___Late_blight": "Remove infected plants immediately and use an appropriate fungicide.",
    "Potato___Early_blight": "Use disease-free seeds and apply fungicide if necessary.",
    "Potato___Late_blight": "Remove infected leaves and improve air circulation around the plants."
}
treatments_tamil = {
    "Apple___healthy": "சிகிச்சை தேவையில்லை. வழக்கமான நீர்ப்பாசனம் மற்றும் பராமரிப்பை தொடரவும்.",

    "Tomato___Early_blight": "பாதிக்கப்பட்ட இலைகளை அகற்றவும். பரிந்துரைக்கப்பட்ட பூஞ்சைக் கொல்லியை பயன்படுத்தவும். மேலிருந்து நீர் பாய்ச்சுவதை தவிர்க்கவும்.",

    "Tomato___Late_blight": "பாதிக்கப்பட்ட செடிகளை உடனடியாக அகற்றவும். பொருத்தமான பூஞ்சைக் கொல்லியை பயன்படுத்தவும்.",

    "Potato___Early_blight": "நோயற்ற விதைகளை பயன்படுத்தவும். தேவையெனில் பூஞ்சைக் கொல்லியை பயன்படுத்தவும்.",

    "Potato___Late_blight": "பாதிக்கப்பட்ட இலைகளை அகற்றவும். செடிகளுக்கு நல்ல காற்றோட்டம் ஏற்படுத்தவும்."
}

disease_info = {
    "Tomato___Early_blight": {
        "description": "A fungal disease caused by Alternaria solani.",
        "symptoms": "Brown spots with yellow rings on leaves.",
        "prevention": "Avoid overhead watering and remove infected leaves."
    },

    "Tomato___Late_blight": {
        "description": "A serious fungal disease caused by Phytophthora infestans.",
        "symptoms": "Dark brown or black spots on leaves and stems.",
        "prevention": "Use healthy seedlings and apply recommended fungicide."
    },

    "Potato___Early_blight": {
        "description": "A fungal disease affecting potato leaves.",
        "symptoms": "Dark circular spots with concentric rings.",
        "prevention": "Rotate crops and remove infected leaves."
    },

    "Potato___Late_blight": {
        "description": "A fungal disease causing rapid crop damage.",
        "symptoms": "Water-soaked lesions that quickly turn brown.",
        "prevention": "Use certified seeds and avoid excessive moisture."
    },

    "Apple___healthy": {
        "description": "The plant is healthy.",
        "symptoms": "No disease symptoms detected.",
        "prevention": "Continue regular watering and proper care."
    }
}
disease_info_tamil = {

    "Tomato___Early_blight": {
        "description": "Alternaria solani என்ற பூஞ்சையால் ஏற்படும் நோய்.",
        "symptoms": "இலைகளில் பழுப்பு நிற வட்டப்புள்ளிகள் மற்றும் மஞ்சள் வளையங்கள் தோன்றும்.",
        "prevention": "பாதிக்கப்பட்ட இலைகளை அகற்றவும். மேலிருந்து நீர் பாய்ச்சுவதை தவிர்க்கவும்."
    },

    "Tomato___Late_blight": {
        "description": "Phytophthora infestans என்ற பூஞ்சையால் ஏற்படும் தீவிர நோய்.",
        "symptoms": "இலைகள் மற்றும் தண்டுகளில் கருப்பு அல்லது அடர் பழுப்பு புள்ளிகள் தோன்றும்.",
        "prevention": "ஆரோக்கியமான நாற்றுகளை பயன்படுத்தவும். பூஞ்சைக் கொல்லியை பயன்படுத்தவும்."
    },

    "Potato___Early_blight": {
        "description": "உருளைக்கிழங்கு இலைகளை பாதிக்கும் பூஞ்சை நோய்.",
        "symptoms": "வட்ட வடிவ கருப்பு புள்ளிகள் தோன்றும்.",
        "prevention": "பயிர் மாற்றம் செய்யவும். பாதிக்கப்பட்ட இலைகளை அகற்றவும்."
    },

    "Potato___Late_blight": {
        "description": "பயிரை வேகமாக பாதிக்கும் தீவிர பூஞ்சை நோய்.",
        "symptoms": "நீர்ப்பசை போன்ற புள்ளிகள் பின்னர் பழுப்பு நிறமாக மாறும்.",
        "prevention": "சான்றளிக்கப்பட்ட விதைகளை பயன்படுத்தவும். அதிக ஈரப்பதத்தை தவிர்க்கவும்."
    },

    "Apple___healthy": {
        "description": "இந்த தாவரம் ஆரோக்கியமாக உள்ளது.",
        "symptoms": "நோய் அறிகுறிகள் எதுவும் இல்லை.",
        "prevention": "வழக்கமான பராமரிப்பு மற்றும் நீர்ப்பாசனத்தை தொடரவும்."
    }
}
tamil_disease_names = {
    "Apple___Apple_scab": "ஆப்பிள் - ஆப்பிள் ஸ்காப்",
    "Apple___Black_rot": "ஆப்பிள் - கருப்பு அழுகல்",
    "Apple___Cedar_apple_rust": "ஆப்பிள் - சீடர் ஆப்பிள் ரஸ்ட்",
    "Apple___healthy": "ஆரோக்கியமான ஆப்பிள்",

    "Blueberry___healthy": "ஆரோக்கியமான ப்ளூபெர்ரி",

    "Cherry_(including_sour)___Powdery_mildew": "செர்ரி - வெள்ளை பூஞ்சை நோய்",
    "Cherry_(including_sour)___healthy": "ஆரோக்கியமான செர்ரி",

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "சோளம் - செர்கோஸ்போரா இலைப்புள்ளி",
    "Corn_(maize)___Common_rust_": "சோளம் - பொதுவான ரஸ்ட் நோய்",
    "Corn_(maize)___Northern_Leaf_Blight": "சோளம் - வடக்கு இலை கருகல்",
    "Corn_(maize)___healthy": "ஆரோக்கியமான சோளம்",

    "Grape___Black_rot": "திராட்சை - கருப்பு அழுகல்",
    "Grape___Esca_(Black_Measles)": "திராட்சை - எஸ்கா (கருப்பு மீஸில்ஸ்)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "திராட்சை - இலை கருகல்",
    "Grape___healthy": "ஆரோக்கியமான திராட்சை",

    "Orange___Haunglongbing_(Citrus_greening)": "ஆரஞ்சு - சிட்ரஸ் கிரீனிங்",

    "Peach___Bacterial_spot": "பீச் - பாக்டீரியா புள்ளி",
    "Peach___healthy": "ஆரோக்கியமான பீச்",

    "Pepper,_bell___Bacterial_spot": "குடைமிளகாய் - பாக்டீரியா புள்ளி",
    "Pepper,_bell___healthy": "ஆரோக்கியமான குடைமிளகாய்",

    "Potato___Early_blight": "உருளைக்கிழங்கு - ஆரம்ப கருகல் நோய்",
    "Potato___Late_blight": "உருளைக்கிழங்கு - தீவிர கருகல் நோய்",
    "Potato___healthy": "ஆரோக்கியமான உருளைக்கிழங்கு",

    "Raspberry___healthy": "ஆரோக்கியமான ராஸ்பெர்ரி",

    "Soybean___healthy": "ஆரோக்கியமான சோயாபீன்",

    "Squash___Powdery_mildew": "ஸ்க்வாஷ் - வெள்ளை பூஞ்சை நோய்",

    "Strawberry___Leaf_scorch": "ஸ்ட்ராபெர்ரி - இலை கருகல்",
    "Strawberry___healthy": "ஆரோக்கியமான ஸ்ட்ராபெர்ரி",

    "Tomato___Bacterial_spot": "தக்காளி - பாக்டீரியா புள்ளி",
    "Tomato___Early_blight": "தக்காளி - ஆரம்ப கருகல் நோய்",
    "Tomato___Late_blight": "தக்காளி - தீவிர கருகல் நோய்",
    "Tomato___Leaf_Mold": "தக்காளி - இலை பூஞ்சை",
    "Tomato___Septoria_leaf_spot": "தக்காளி - செப்டோரியா இலைப்புள்ளி",
    "Tomato___Spider_mites Two-spotted_spider_mite": "தக்காளி - சிலந்திப் பூச்சி தாக்குதல்",
    "Tomato___Target_Spot": "தக்காளி - இலக்கு புள்ளி நோய்",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "தக்காளி - மஞ்சள் இலை சுருள் வைரஸ்",
    "Tomato___Tomato_mosaic_virus": "தக்காளி - மோசைக் வைரஸ்",
    "Tomato___healthy": "ஆரோக்கியமான தக்காளி"
}
seasonal_crops = {
    "Summer": [
        "🌽 Maize",
        "🥒 Cucumber",
        "🍉 Watermelon",
        "🍈 Muskmelon",
        "🌻 Sunflower"
    ],

    "Monsoon": [
        "🌾 Paddy (Rice)",
        "🌽 Maize",
        "🌱 Soybean",
        "🥜 Groundnut",
        "🌿 Cotton"
    ],

    "Winter": [
        "🌾 Wheat",
        "🥔 Potato",
        "🥕 Carrot",
        "🥬 Cabbage",
        "🥦 Cauliflower"
    ]
}
seasonal_crops_tamil = {
    "Summer": [
        "🌽 மக்காச்சோளம்",
        "🥒 வெள்ளரிக்காய்",
        "🍉 தர்பூசணி",
        "🍈 முலாம்பழம்",
        "🌻 சூரியகாந்தி"
    ],

    "Monsoon": [
        "🌾 நெல் (அரிசி)",
        "🌽 மக்காச்சோளம்",
        "🌱 சோயாபீன்",
        "🥜 நிலக்கடலை",
        "🌿 பருத்தி"
    ],

    "Winter": [
        "🌾 கோதுமை",
        "🥔 உருளைக்கிழங்கு",
        "🥕 கேரட்",
        "🥬 முட்டைக்கோஸ்",
        "🥦 காலிஃபிளவர்"
    ]
}
# ---------------- Prediction ----------------
if uploaded_file is not None:
    left_col, right_col = st.columns([1, 1])
    image = Image.open(uploaded_file).convert("RGB")
    st.write("✅ Step 1: Image loaded")

    if language == "English":
        with left_col:
            st.image(
               image,
               caption="🌿 Uploaded Leaf Image",
               use_container_width=True
           )
        st.success("Image uploaded successfully!")

    else:
        with left_col:
             st.image(
                image,
                caption="🌿 பதிவேற்றப்பட்ட இலை படம்",
                use_container_width=True
         )
        st.success("படம் வெற்றிகரமாக பதிவேற்றப்பட்டது!")
    

    # Load Classes
    with open("classes.txt", "r") as f:
        class_names = [line.strip() for line in f]
    st.write("✅ Step 2: Classes loaded")

    # Preprocess Image
    img = image.resize((224, 224))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    st.write("✅ Step 3: Starting prediction")
    prediction = model.predict(img)
    st.write("✅ Step 4: Prediction completed")
    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]

    confidence = prediction[0][predicted_index] * 100

    st.write("Predicted:", predicted_class)
    st.write("Tamil:", tamil_disease_names.get(predicted_class, "NOT FOUND"))

    english_name = predicted_class.replace("___", " : ").replace("_", " ")
    tamil_name = tamil_disease_names.get(predicted_class, english_name)


    # Result
    with right_col:
        if language == "English":
           st.success("Prediction completed successfully!")
           st.success(f"🌿 Predicted Disease: {english_name}")
           st.write(f"**Confidence:** {confidence:.2f}%")

    
        else:
            st.success("கணிப்பு வெற்றிகரமாக முடிந்தது!")
            st.success(f"🌿 கணிக்கப்பட்ட நோய்: {tamil_name}")
            st.write(f"**நம்பகத்தன்மை:** {confidence:.2f}%")

        st.progress(float(confidence / 100))
        col1, col2 = st.columns(2)

        with col1:
            st.info(f"📊 Confidence\n\n{confidence:.2f}%")

        with col2:
            if "healthy" in predicted_class.lower():
                if language == "English":
                    st.success("🌱 Healthy Plant")
                else:
                    st.success("🌱 ஆரோக்கியமான தாவரம்")
            else:
                if language == "English":
                    st.error("🍂 Diseased Plant")
                else:
                    st.error("🍂 நோய் பாதிக்கப்பட்ட தாவரம்")
        col3, col4 = st.columns(2)

        with col3:
            st.info(f"🌦 Season\n\n{season}")

        with col4:
            st.info("🌍 Language\n\n" + language)
    # Plant Status
    if "healthy" in predicted_class.lower():
        if language == "English":
            st.success("🌱 Plant Status: Healthy")
        else:
            st.success("🌱 தாவரம் ஆரோக்கியமாக உள்ளது")
    else:
        if language == "English":
            st.error("🍂 Plant Status: Diseased")
        else:
            st.error("🍂 தாவரத்தில் நோய் உள்ளது")


    # 🌦 Seasonal Crop Recommendation

    if language == "English":
        st.subheader("🌦 Seasonal Crop Recommendation")
        st.success(f"Recommended crops for {season} season:")

        for crop in seasonal_crops[season]:
            st.write("✅", crop)

    else:
        st.subheader("🌦 பருவகால பயிர் பரிந்துரை")
    
        tamil_season = {
            "Summer": "கோடை",
            "Monsoon": "மழைக்காலம்",
            "Winter": "குளிர்காலம்"
       }

        st.success(f"{tamil_season[season]} பருவத்திற்கு ஏற்ற பயிர்கள்:")

        if language == "English":
            for crop in seasonal_crops[season]:
                st.write("✅", crop)

        else:
            for crop in seasonal_crops_tamil[season]:
                st.write("✅", crop)

    if language == "English":
         tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "💊 Treatment",
            "📖 Disease Info",
            "🌾 Fertilizer",
            "💧 Watering",
            "🌦 Farming"
        ])
    else:
         tab1, tab2, tab3, tab4, tab5 = st.tabs([
             "💊 சிகிச்சை",
             "📖 நோய் தகவல்",
             "🌾 உர பரிந்துரை",
             "💧 நீர்ப்பாசனம்",
             "🌦 விவசாய ஆலோசனை"
        ])  
    with tab1:
    # Treatment
         if language == "English":
            st.subheader("💊 Treatment & Prevention")
         else:
            st.subheader("💊 சிகிச்சை மற்றும் தடுப்பு")

         if language == "English":
            if predicted_class in treatments:
                st.info(treatments[predicted_class])
            else:
                st.info("No specific treatment information available.")

         else:
             if predicted_class in treatments_tamil:
                st.info(treatments_tamil[predicted_class])
             else:
                st.info("இந்த நோய்க்கான குறிப்பிட்ட சிகிச்சை தகவல் இல்லை.")
    with tab2:
    # Disease Information
        if language == "English":
            st.subheader("📖 Disease Information")
        else:
            st.subheader("📖 நோய் தகவல்")

        if language == "English":
            if predicted_class in disease_info:
                info = disease_info[predicted_class]

                st.write("**Description:**")
                st.write(info["description"])

                st.write("**Symptoms:**")
                st.write(info["symptoms"])

                st.write("**Prevention:**")
                st.write(info["prevention"])

            else:
                 st.info("Disease information is not available.")

        else:

            if predicted_class in disease_info_tamil:
                 info = disease_info_tamil[predicted_class]

                 st.write("**விளக்கம்:**")
                 st.write(info["description"])

                 st.write("**அறிகுறிகள்:**")
                 st.write(info["symptoms"])

                 st.write("**தடுப்பு:**")
                 st.write(info["prevention"])

            else:
                 st.info("நோய் பற்றிய தகவல் இல்லை.")
    with tab3:
      fertilizers = {
          "Tomato___Early_blight": "🌾 Mancozeb + NPK 19:19:19",
          "Tomato___Late_blight": "🌾 Copper Oxychloride + Potash-rich fertilizer",
          "Tomato___healthy": "🌾 Organic Compost + Vermicompost",

          "Potato___Early_blight": "🌾 NPK 20:20:20",
          "Potato___Late_blight": "🌾 Copper-based fungicide + Potassium fertilizer",
          "Potato___healthy": "🌾 Farmyard Manure",

          "Apple___healthy": "🌾 Organic Compost"
      } 
      fertilizers_tamil = {

          "Tomato___Early_blight": "🌾 மான்கோசெப் + NPK 19:19:19",

         "Tomato___Late_blight": "🌾 காப்பர் ஆக்ஸிகுளோரைடு + பொட்டாசியம் அதிகமுள்ள உரம்",

         "Tomato___healthy": "🌾 இயற்கை கம்போஸ்ட் + வெர்மிகம்போஸ்ட்",

         "Potato___Early_blight": "🌾 NPK 20:20:20",

         "Potato___Late_blight": "🌾 காப்பர் அடிப்படையிலான பூஞ்சைக் கொல்லி + பொட்டாசியம் உரம்",

         "Potato___healthy": "🌾 பண்ணை இயற்கை உரம்",

         "Apple___healthy": "🌾 இயற்கை கம்போஸ்ட்"
      }  
                
      if language == "English":
        st.subheader("🌾 Fertilizer Recommendation")

        if predicted_class in fertilizers:
            st.success(fertilizers[predicted_class])
        else:
            st.info("No fertilizer recommendation available.")

      else:
        st.subheader("🌾 உர பரிந்துரை")

        if predicted_class in fertilizers_tamil:
            st.success(fertilizers_tamil[predicted_class])
        else:
            st.info("உர பரிந்துரை கிடைக்கவில்லை.")
    
    with tab4:
      watering_advice = {
       "Tomato___Early_blight": "💧 Water only at the base of the plant. Avoid wetting the leaves. Water early in the morning.",
       "Tomato___Late_blight": "💧 Reduce watering during humid weather. Ensure proper drainage.",
       "Tomato___healthy": "💧 Water regularly when the topsoil becomes dry.",

       "Potato___Early_blight": "💧 Water consistently but avoid waterlogging.",
       "Potato___Late_blight": "💧 Avoid excess watering and improve soil drainage.",
       "Potato___healthy": "💧 Keep the soil evenly moist.",

       "Apple___healthy": "💧 Water deeply once or twice a week depending on the weather."
      }
      watering_advice_tamil = {

        "Tomato___Early_blight": "💧 செடியின் அடிப்பகுதியில் மட்டும் நீர் ஊற்றவும். இலைகளை நனைக்க வேண்டாம். அதிகாலை நேரத்தில் நீர்ப்பாசனம் செய்யவும்.",

        "Tomato___Late_blight": "💧 ஈரப்பதமான காலநிலையில் நீர்ப்பாசனத்தை குறைக்கவும். வயலில் நல்ல வடிகால் வசதி இருக்க வேண்டும்.",

        "Tomato___healthy": "💧 மேல் மண் காய்ந்ததும் வழக்கமான நீர்ப்பாசனம் செய்யவும்.",

        "Potato___Early_blight": "💧 சீரான அளவில் நீர் வழங்கவும். அதிக நீர் தேங்க விடாதீர்கள்.",

        "Potato___Late_blight": "💧 அதிக நீர்ப்பாசனத்தை தவிர்க்கவும். மண்ணில் நல்ல வடிகால் வசதி இருக்க வேண்டும்.",

        "Potato___healthy": "💧 மண்ணை எப்போதும் லேசான ஈரப்பதத்துடன் வைத்திருக்கவும்.",

        "Apple___healthy": "💧 காலநிலைக்கு ஏற்ப வாரத்திற்கு ஒரு முறை அல்லது இரண்டு முறை ஆழமாக நீர்ப்பாசனம் செய்யவும்."
      }
     # Watering Advice

      if language == "English":
        st.subheader("💧 Watering Advice")
      else:
        st.subheader("💧 நீர்ப்பாசன ஆலோசனை")

      if language == "English":
        
        if predicted_class in watering_advice:
            st.info(watering_advice[predicted_class])
        else:
            st.info("No watering advice available.")

      else:

        if predicted_class in watering_advice_tamil:
            st.info(watering_advice_tamil[predicted_class])
        else:
            st.info("நீர்ப்பாசன ஆலோசனை கிடைக்கவில்லை.")

    with tab5:  
    # Seasonal Farming Suggestions

      if language == "English":
        st.subheader("🌾 Seasonal Farming Suggestions")

        if season == "Summer":
            st.write("💧 Use drip irrigation to save water.")
            st.write("🌱 Choose drought-resistant crops.")
            st.write("🌿 Apply mulch to maintain soil moisture.")

        elif season == "Monsoon":
            st.write("🌧 Ensure proper drainage in fields.")
            st.write("🌱 Monitor crops for fungal diseases.")
            st.write("☔ Avoid waterlogging near roots.")

        elif season == "Winter":
            st.write("❄️ Protect young plants from cold weather.")
            st.write("🌱 Use organic manure for better growth.")
            st.write("💧 Reduce watering frequency.")

      else:
        st.subheader("🌾 பருவகால விவசாய ஆலோசனைகள்")

        if season == "Summer":
             st.write("💧 நீரை சேமிக்க சொட்டு நீர்ப்பாசனம் பயன்படுத்தவும்.")
             st.write("🌱 வறட்சியை தாங்கும் பயிர்களை தேர்வு செய்யவும்.")
             st.write("🌿 மண்ணின் ஈரப்பதத்தை பாதுகாக்க மூடாக்கு பயன்படுத்தவும்.")

        elif season == "Monsoon":
             st.write("🌧 வயலில் நல்ல வடிகால் வசதி இருக்க வேண்டும்.")
             st.write("🌱 பூஞ்சை நோய்களை தொடர்ந்து கண்காணிக்கவும்.")
             st.write("☔ அதிக நீர் தேங்குவதை தவிர்க்கவும்.")

        elif season == "Winter":
             st.write("❄️ இளம் செடிகளை குளிரிலிருந்து பாதுகாக்கவும்.")
             st.write("🌱 சிறந்த வளர்ச்சிக்கு இயற்கை உரம் பயன்படுத்தவும்.")
             st.write("💧 நீர்ப்பாசன அளவை குறைக்கவும்.")
        
        
    