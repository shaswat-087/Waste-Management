import folium
import pandas as pd
m1=folium.Map(location=[23.5874,87.3814],zoom_start=7,tiles="cartodbpositron")


waste_centres = {
    "Andhra Pradesh": [
        ["Srichakra E-Waste Recycling", 16.5062, 80.6480],
        ["Vishakhapatnam Solid Waste Processing Plant", 17.6868, 83.2185],
        ["Guntur Municipal Recycling Centre", 16.3067, 80.4365],
        ["Tirupati Waste Collection Centre", 13.6288, 79.4192],
        ["Kurnool Dry Waste Collection Centre", 15.8281, 78.0373]
    ],

    "Arunachal Pradesh": [
        ["Itanagar Municipal Waste Centre", 27.0844, 93.6053],
        ["Naharlagun Waste Collection Point", 27.1046, 93.6952],
        ["Pasighat Recycling Centre", 28.0661, 95.3268]
    ],

    "Assam": [
        ["Guwahati Waste Processing Facility", 26.1445, 91.7362],
        ["Silchar Municipal Recycling Centre", 24.8333, 92.7789],
        ["Dibrugarh Solid Waste Centre", 27.4728, 94.9120],
        ["Jorhat Waste Collection Facility", 26.7509, 94.2037],
        ["Tezpur Municipal Waste Yard", 26.6528, 92.7926]
    ],

    "Bihar": [
        ["Patna E-Waste Collection Centre", 25.5941, 85.1376],
        ["Muzaffarpur Waste Recycling Hub", 26.1209, 85.3647],
        ["Gaya Municipal Waste Plant", 24.7914, 85.0002],
        ["Bhagalpur Solid Waste Centre", 25.2425, 86.9842],
        ["Darbhanga Recycling Facility", 26.1542, 85.8918]
    ],

    "Chhattisgarh": [
        ["Raipur Solid Waste Management Plant", 21.2514, 81.6296],
        ["Bilaspur Recycling Centre", 22.0797, 82.1409],
        ["Durg Waste Collection Yard", 21.1904, 81.2849],
        ["Korba Municipal Waste Centre", 22.3595, 82.7501],
        ["Jagdalpur Dry Waste Collection Centre", 19.0741, 82.0080]
    ],

    "Goa": [
        ["Saligao Waste Management Facility", 15.5531, 73.7898],
        ["Margao Recycling Centre", 15.2993, 74.1240],
        ["Panaji Waste Collection Centre", 15.4909, 73.8278]
    ],

    "Gujarat": [
        ["Ahmedabad Pirana Waste Processing Plant", 23.0225, 72.5714],
        ["Surat Solid Waste Facility", 21.1702, 72.8311],
        ["Vadodara Recycling Centre", 22.3072, 73.1812],
        ["Rajkot Waste Collection Centre", 22.3039, 70.8022],
        ["Bhavnagar Municipal Waste Plant", 21.7645, 72.1519],
        ["Jamnagar Recycling Yard", 22.4707, 70.0577],
        ["Gandhinagar Dry Waste Centre", 23.2156, 72.6369]
    ],

    "Haryana": [
        ["Gurugram Waste Processing Facility", 28.4595, 77.0266],
        ["Faridabad Recycling Centre", 28.4089, 77.3178],
        ["Panipat Waste Collection Hub", 29.3909, 76.9635],
        ["Karnal Solid Waste Centre", 29.6857, 76.9905],
        ["Hisar Municipal Recycling Yard", 29.1492, 75.7217]
    ],

    "Himachal Pradesh": [
        ["Shimla Waste Collection Centre", 31.1048, 77.1734],
        ["Dharamshala Recycling Centre", 32.2190, 76.3234],
        ["Mandi Solid Waste Facility", 31.7084, 76.9310],
        ["Solan Dry Waste Collection Point", 30.9045, 77.0967]
    ],

    "Jharkhand": [
        ["Ranchi Solid Waste Plant", 23.3441, 85.3096],
        ["Jamshedpur Recycling Centre", 22.8046, 86.2029],
        ["Dhanbad Waste Collection Yard", 23.7957, 86.4304],
        ["Bokaro Municipal Waste Facility", 23.6693, 86.1511]
    ],

    "Karnataka": [
        ["Bengaluru E-Parisaraa Recycling", 12.9716, 77.5946],
        ["Mysuru Solid Waste Management Plant", 12.2958, 76.6394],
        ["Hubballi Waste Collection Centre", 15.3647, 75.1240],
        ["Mangaluru Recycling Facility", 12.9141, 74.8560],
        ["Belagavi Dry Waste Collection Centre", 15.8497, 74.4977],
        ["Kalaburagi Municipal Waste Yard", 17.3297, 76.8343],
        ["Udupi Waste Processing Unit", 13.3409, 74.7421]
    ],

    "Kerala": [
        ["Kochi Brahmapuram Waste Plant", 9.9312, 76.2673],
        ["Thiruvananthapuram Recycling Centre", 8.5241, 76.9366],
        ["Kozhikode Waste Collection Facility", 11.2588, 75.7804],
        ["Thrissur Solid Waste Plant", 10.5276, 76.2144],
        ["Kannur Municipal Recycling Centre", 11.8745, 75.3704]
    ],

    "Madhya Pradesh": [
        ["Indore Solid Waste Management Plant", 22.7196, 75.8577],
        ["Bhopal Recycling Centre", 23.2599, 77.4126],
        ["Jabalpur Waste Collection Hub", 23.1815, 79.9864],
        ["Gwalior Municipal Waste Yard", 26.2183, 78.1828],
        ["Ujjain Dry Waste Collection Centre", 23.1765, 75.7885],
        ["Sagar Recycling Facility", 23.8388, 78.7378]
    ],

    "Maharashtra": [
        ["Mumbai Deonar Waste Processing Plant", 19.0760, 72.8777],
        ["Pune SWaCH Recycling Centre", 18.5204, 73.8567],
        ["Nagpur Waste Collection Centre", 21.1458, 79.0882],
        ["Nashik Municipal Recycling Plant", 19.9975, 73.7898],
        ["Aurangabad Solid Waste Facility", 19.8762, 75.3433],
        ["Kolhapur Dry Waste Collection Centre", 16.7050, 74.2433],
        ["Thane Waste Processing Unit", 19.2183, 72.9781],
        ["Solapur Municipal Waste Yard", 17.6599, 75.9064],
        ["Amravati Recycling Centre", 20.9374, 77.7796],
        ["Navi Mumbai Waste Collection Facility", 19.0330, 73.0297],
        ["Jalgaon Solid Waste Plant", 21.0077, 75.5626],
        ["Satara Recycling Centre", 17.6805, 74.0183]
    ],

    "Manipur": [
        ["Imphal Waste Collection Centre", 24.8170, 93.9368],
        ["Thoubal Recycling Facility", 24.6388, 94.0100]
    ],

    "Meghalaya": [
        ["Shillong Municipal Waste Facility", 25.5788, 91.8933],
        ["Tura Recycling Centre", 25.5142, 90.2021]
    ],

    "Mizoram": [
        ["Aizawl Waste Collection Centre", 23.7271, 92.7176],
        ["Lunglei Recycling Facility", 22.8925, 92.7425]
    ],

    "Nagaland": [
        ["Kohima Waste Processing Centre", 25.6751, 94.1086],
        ["Dimapur Recycling Yard", 25.9091, 93.7266]
    ],

    "Odisha": [
        ["Bhubaneswar Solid Waste Facility", 20.2961, 85.8245],
        ["Cuttack Recycling Centre", 20.4625, 85.8828],
        ["Rourkela Waste Collection Yard", 22.2604, 84.8536],
        ["Berhampur Municipal Waste Plant", 19.3149, 84.7941],
        ["Sambalpur Dry Waste Centre", 21.4669, 83.9812]
    ],

    "Punjab": [
        ["Ludhiana Waste Processing Plant", 30.9010, 75.8573],
        ["Amritsar Recycling Centre", 31.6340, 74.8723],
        ["Jalandhar Solid Waste Facility", 31.3260, 75.5762],
        ["Patiala Waste Collection Yard", 30.3398, 76.3869],
        ["Bathinda Municipal Recycling Centre", 30.2110, 74.9455]
    ],

    "Rajasthan": [
        ["Jaipur Solid Waste Processing Plant", 26.9124, 75.7873],
        ["Jodhpur Recycling Centre", 26.2389, 73.0243],
        ["Udaipur Waste Collection Facility", 24.5854, 73.7125],
        ["Kota Municipal Waste Yard", 25.2138, 75.8648],
        ["Bikaner Dry Waste Collection Centre", 28.0229, 73.3119],
        ["Ajmer Recycling Plant", 26.4499, 74.6399],
        ["Alwar Waste Processing Centre", 27.5529, 76.6346],
        ["Bharatpur Municipal Waste Facility", 27.2152, 77.5030],
        ["Sikar Recycling Centre", 27.6094, 75.1399],
        ["Pali Waste Collection Hub", 25.7711, 73.3234],
        ["Chittorgarh Solid Waste Centre", 24.8799, 74.6299]
    ],

    "Sikkim": [
        ["Gangtok Waste Collection Centre", 27.3389, 88.6065],
        ["Namchi Recycling Facility", 27.1667, 88.3667]
    ],

    "Tamil Nadu": [
        ["Chennai Perungudi Dump Yard", 13.0827, 80.2707],
        ["Coimbatore Waste Collection Centre", 11.0168, 76.9558],
        ["Madurai Recycling Facility", 9.9252, 78.1198],
        ["Tiruchirappalli Solid Waste Plant", 10.7905, 78.7047],
        ["Salem Municipal Waste Centre", 11.6643, 78.1460],
        ["Erode Recycling Yard", 11.3410, 77.7172],
        ["Tirunelveli Waste Processing Unit", 8.7139, 77.7567],
        ["Vellore Dry Waste Collection Centre", 12.9165, 79.1325],
        ["Thoothukudi Waste Management Facility", 8.7642, 78.1348],
        ["Thanjavur Recycling Centre", 10.7867, 79.1378]
    ],

    "Telangana": [
        ["Hyderabad Jawaharnagar Waste Plant", 17.3850, 78.4867],
        ["Warangal Recycling Centre", 17.9689, 79.5941],
        ["Karimnagar Waste Collection Facility", 18.4386, 79.1288],
        ["Nizamabad Solid Waste Centre", 18.6725, 78.0941],
        ["Khammam Dry Waste Collection Centre", 17.2473, 80.1514]
    ],

    "Tripura": [
        ["Agartala Waste Processing Centre", 23.8315, 91.2868],
        ["Udaipur Recycling Centre", 23.5330, 91.4830]
    ],

    "Uttar Pradesh": [
        ["Lucknow Solid Waste Plant", 26.8467, 80.9462],
        ["Kanpur Recycling Centre", 26.4499, 80.3319],
        ["Varanasi Waste Collection Facility", 25.3176, 82.9739],
        ["Agra Municipal Waste Yard", 27.1767, 78.0081],
        ["Prayagraj Recycling Plant", 25.4358, 81.8463],
        ["Ghaziabad Waste Processing Unit", 28.6692, 77.4538],
        ["Meerut Dry Waste Collection Centre", 28.9845, 77.7064],
        ["Gorakhpur Waste Collection Centre", 26.7606, 83.3732],
        ["Noida Recycling Facility", 28.5355, 77.3910],
        ["Bareilly Solid Waste Centre", 28.3670, 79.4304]
    ],

    "Uttarakhand": [
        ["Dehradun Waste Collection Centre", 30.3165, 78.0322],
        ["Haridwar Recycling Facility", 29.9457, 78.1642],
        ["Haldwani Solid Waste Plant", 29.2183, 79.5130],
        ["Rudrapur Municipal Waste Centre", 28.9875, 79.4141]
    ],

    "West Bengal": [
        ["Kolkata Dhapa Waste Processing Facility", 22.5726, 88.3639],
        ["Durgapur Recycling Centre", 23.5204, 87.3119],
        ["Siliguri Waste Collection Hub", 26.7271, 88.3953],
        ["Howrah Solid Waste Plant", 22.5958, 88.2636],
        ["Asansol Recycling Yard", 23.6739, 86.9524],
        ["Kharagpur Municipal Waste Centre", 22.3460, 87.2319],
        ["Malda Waste Processing Unit", 25.0108, 88.1411],
        ["Bardhaman Dry Waste Collection Centre", 23.2324, 87.8615]
    ]
}


rows = []
for state, centres in waste_centres.items():
    for centre in centres:
        rows.append([state, centre[0], centre[1], centre[2]])

df = pd.DataFrame(rows, columns=["State", "Centre Name", "Latitude", "Longitude"])


for i ,row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"],row["Longitude"]],
        popup=str(row["Centre Name"]),
        icon=folium.Icon(color="lightgray")
       ).add_to(m1)
    
m1.save("map.html")
