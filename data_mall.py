import os
import random
import string


pim_data = {
    'Location': 'Jl. Kol. H. Burlian',
    'Operating Hours': '10:00 AM - 10:00 PM',
    'Facilities': ['Food Court', 'Cinema', 'Game Center']
}

pi_data = {
    'Location': 'Jl. R. Sukamoto',
    'Operating Hours': '11:00 AM - 11:00 PM',
    'Facilities': ['Food Court', 'Cinema', 'Karaoke']
}

ps_data = {
    'Location': 'Jl.Angkatan 45, Lorok pakjo',
    'Operating Hours': '10:00 AM - 10:00 PM',
    'Facilities': ['Food Court', 'Cinema', 'Game Center']
}

PTC_data = {
    'Location': 'Jl. R.sukamto',
    'Operating Hours': '10:00 AM - 10:00 PM',
    'Facilities': ['Food Court', 'Cinema', 'Game Center']
}

opi_data = {
    'Location': 'Jl. Gubenur H.A',
    'Operating Hours': '10:00 AM - 10:00 PM',
    'Facilities': ['Food Court', 'Cinema', 'Game Center']
}

transmart_data = {
    'Location': 'Jl. Radial',
    'Operating Hours': '10:00 AM - 10:00 PM',
    'Facilities': ['Food Court', 'Cinema', 'Game Center']
}

df = pd.DataFrame([pim_data, pi_data, ps_data,PTC_data,opi_data,transmart_data], index=['PIM', 'PI','PS','PTC','opi','transmart'])


print(df)