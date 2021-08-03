
import urllib.request, urllib.parse, urllib.error
import json

url = "http://api.currencylayer.com/live?access_key=42141e409e1f1bfffe491b212bacdd15"
   
currencycodes = {'Afghanistan': 'AFN', 'Akrotiri and Dhekelia(UK)': 'EUR', 'Aland Islands(Finland)': 'EUR', 'Albania': 'ALL', 'Algeria': 'DZD', 'American Samoa(USA)': 'USD', 'Andorra': 'EUR', 'Angola': 'AOA', 'Anguilla(UK)': 'XCD', 'Antigua and Barbuda': 'XCD', 'Argentina': 'ARS', 'Armenia': 'AMD', 'Aruba(Netherlands)': 'AWG', 'Ascension Island=(UK)': 'SHP', 'Australia': 'AUD', 'Austria': 'EUR', 'Azerbaijan': 'AZN', 'Bahamas': 'BSD', 'Bahrain':'BHD', 'Bangladesh': 'BDT', 'Barbados': 'BBD', 'Belarus': 'BYN', 'Belgium': 'EUR', 'Belize': 'BZD', 'Benin': 'XOF', 'Bermuda(UK)': 'BMD', 'Bhutan': 'BTN', 'Bolivia': 'BOB', 'Bonaire(Netherlands)': 'USD', 'Bosnia and Herzegovina': 'BAM', 'Botswana': 'BWP', 'Brazil': 'BRL', 'British Indian Ocean Territory(UK)': 'USD', 'British Virgin Islands(UK)': 'USD', 'Brunei': 'BND', 'Bulgaria': 'BGN', 'Burkina Faso': 'XOF', 'Burundi': 'BIF', 'Cabo Verde': 'CVE', 'Cambodia': 'KHR', 'Cameroon': 'XAF', 'Canada': 'CAD', 'Caribbean Netherlands(Netherlands)': 'USD', 'Cayman Islands(UK)': 'KYD', 'Central African Republic': 'XAF', 'Chad': 'XAF', 'Chatham Islands\xa0(New Zealand)': 'NZD', 'Chile': 'CLP', 'China': 'CNY', 'Christmas Island(Australia)': 'AUD', 'Cocos (Keeling) Islands(Australia)': 'AUD', 'Colombia': 'COP', 'Comoros': 'KMF', 'Congo, Democratic Republic of the': 'CDF', 'Congo, Republic of the': 'XAF', 'Cook Islands(New Zealand)': 'none', 'Costa Rica': 'CRC', "Cote d'Ivoire": 'XOF', 'Croatia': 'HRK', 'Cuba': 'CUP', 'Curacao(Netherlands)': 'ANG', 'Cyprus': 'EUR', 'Czechia': 'CZK', 'Denmark': 'DKK', 'Djibouti': 'DJF', 'Dominica': 'XCD', 'Dominican Republic': 'DOP', 'Ecuador': 'USD', 'Egypt': 'EGP', 'El Salvador': 'USD', 'Equatorial Guinea': 'XAF', 'Eritrea': 'ERN', 'Estonia': 'EUR', 'Eswatini(formerly Swaziland)': 'SZL', 'Ethiopia': 'ETB', 'Falkland Islands(UK)': 'FKP', 'Faroe Islands(Denmark)': 'none', 'Fiji': 'FJD', 'Finland': 'EUR', 'France': 'EUR', 'French Guiana(France)': 'EUR', 'French PolynesiaFrance)': 'XPF', 'Gabon': 'XAF', 'Gambia': 'GMD', 'Georgia': 'GEL', 'Germany': 'EUR', 'Ghana': 'GHS', 'Gibraltar(UK)': 'GIP', 'Greece': 'EUR', 'Greenland(Denmark)': 'DKK', 'Grenada': 'XCD', 'Guadeloupe(France)': 'EUR', 'Guam(USA)': 'USD', 'Guatemala': 'GTQ', 'Guernsey(UK)': 'GGP', 'Guinea': 'GNF', 'Guinea-Bissau': 'XOF', 'Guyana': 'GYD', 'Haiti': 'HTG', 'Honduras': 'HNL', 'Hong Kong(China)': 'HKD', 'Hungary': 'HUF', 'Iceland': 'ISK', 'India': 'INR', 'Indonesia': 'IDR', 'International Monetary Fund (IMF)': 'XDR', 'Iran': 'IRR', 'Iraq': 'IQD', 'Ireland': 'EUR', 'Isle of Man(UK)': 'IMP', 'Israel': 'ILS', 'Italy': 'EUR', 'Jamaica': 'JMD', 'Japan': 'JPY', 'Jersey(UK)': 'JEP', 'Jordan': 'JOD', 'Kazakhstan': 'KZT', 'Kenya': 'KES', 'Kiribati': 'AUD', 'Kosovo': 'EUR', 'Kuwait': 'KWD', 'Kyrgyzstan': 'KGS', 'Laos': 'LAK', 'Latvia': 'EUR', 'Lebanon': 'LBP', 'Lesotho': 'LSL', 'Liberia': 'LRD', 'Libya': 'LYD', 'Liechtenstein': 'CHF', 'Lithuania': 'EUR', 'Luxembourg': 'EUR', 'Macau(China)': 'MOP', 'Madagascar': 'MGA', 'Malawi': 'MWK', 'Malaysia': 'MYR', 'Maldives': 'MVR', 'Mali': 'XOF', 'Malta': 'EUR', 'Marshall Islands': 'USD', 'Martinique\xa0(France)': 'EUR', 'Mauritania': 'MRU', 'Mauritius': 'MUR', 'Mayotte\xa0(France)': 'EUR', 'Mexico': 'MXN', 'Micronesia': 'USD', 'Moldova': 'MDL', 'Monaco': 'EUR', 'Mongolia': 'MNT', 'Montenegro': 'EUR', 'Montserrat\xa0(UK)': 'XCD', 'Morocco': 'MAD', 'Mozambique': 'MZN', 'Myanmar\xa0(formerly Burma)': 'MMK', 'Namibia': 'NAD', 'Nauru': 'AUD', 'Nepal': 'NPR', 'Netherlands': 'EUR', 'New Caledonia(France)': 'XPF', 'New Zealand': 'NZD', 'Nicaragua': 'NIO', 'Niger': 'XOF', 'Nigeria': 'NGN', 'Niue(New Zealand)': 'NZD', 'Norfolk Island(Australia)': 'AUD', 'Northern Mariana Islands(USA)': 'USD', 'North Korea': 'KPW', 'North Macedonia(formerly Macedonia)': 'MKD', 'Norway':'NOK', 'Sudan': 'SSP', 'Spain': 'EUR', 'Sri Lanka': 'LKR', 'Sudan': 'SDG', 'Suriname': 'SRD', 'Svalbard and Jan Mayen(Norway)': 'NOK', 'Sweden': 'SEK', 'Switzerland': 'CHF', 'Syria': 'SYP', 'Taiwan': 'TWD', 'Tajikistan': 'TJS', 'Tanzania': 'TZS', 'Thailand': 'THB', 'Timor-Leste': 'USD', 'Togo': 'XOF', 'Tokelau(New Zealand)': 'NZD', 'Tonga': 'TOP', 'Trinidad and Tobago': 'TTD', 'Tristan da Cunha(UK)': 'GBP', 'Tunisia': 'TND', 'Turkey': 'TRY', 'Turkmenistan': 'TMT', 'Turks and Caicos Islands(UK)': 'USD', 'Tuvalu': 'AUD', 'Uganda': 'UGX', 'Ukraine': 'UAH', 'United Arab Emirates': 'AED', 'United Kingdom': 'GBP', 'United States of America': 'USD', 'Uruguay': 'UYU', 'US Virgin Islands(USA)': 'USD', 'Uzbekistan': 'UZS', 'Vanuatu': 'VUV', 'Vatican City (Holy See)': 'EUR', 'Venezuela': 'VES', 'Vietnam': 'VND', 'Wake Island(USA)': 'USD', 'Wallis and Futuna(France)': 'XPF', 'Yemen': 'YER', 'Zambia': 'ZMW', 'Zimbabwe': 'USD'}
for i in currencycodes:
    print(i, ':', currencycodes[i])

open_url = urllib.request.urlopen(url)    
source = open_url.read()

data = json.loads(source)
pydata = json.dumps(data, indent=4)

print("Refer the list above for ISO-4217 code of all currencies.")

while True:
    pri_cur= input('>>>Please enter the ISO-4217 code of primary currency you want to convert: ').upper()
    if pri_cur not in currencycodes.values():
        pri_cur= input('>>>Please enter the ISO-4217 code of primary currency you want to convert: ').upper()
    else:
        break


while True:
    sec_cur = input('>>>Please enter the ISO-4217 code of secondary currency you want to convert: ').upper()
    if sec_cur not in currencycodes.values():
        sec_cur = input('>>>Please enter the ISO-4217 code of secondary currency you want to convert: ').upper()
    else:
        break


while True:
    try:
        value = int(input(f'>>>How much of {pri_cur} do you want to convert to {sec_cur}, please avoid "," or ".". Just enter numbers alone: '))
        break
    except:
        continue
    

flo_val = float(value)
pri_cur_val = data["quotes"]["USD"+pri_cur]
pri2usd = flo_val/pri_cur_val
sec_cur_val = data["quotes"]["USD"+sec_cur]
answer = pri2usd*sec_cur_val

print(f"{value} {pri_cur} converted to {sec_cur} = {answer} {sec_cur}")


