#!/usr/bin/env python3
"""
Generate the three example frontpages for Business Booster prospects
"""

import sys
from pathlib import Path

# Add parent directory to path to import generate_frontpage
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Read the template
template_path = parent_dir / 'template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

from datetime import datetime

def get_color_scheme(business_type):
    """Return color scheme based on business type"""
    schemes = {
        'automotive': {
            'primary': '#1e3a8a',  # Deep blue
            'secondary': '#f97316',  # Orange
            'accent': '#fb923c'
        },
        'restaurant': {
            'primary': '#064e3b',  # Dark green
            'secondary': '#d97706',  # Gold
            'accent': '#fbbf24'
        },
        'education': {
            'primary': '#16a34a',  # Fresh green
            'secondary': '#0ea5e9',  # Sky blue
            'accent': '#22d3ee'
        }
    }
    return schemes.get(business_type, schemes['automotive'])

def generate_services_html(services_list):
    """Generate services cards HTML"""
    icons = ['🔧', '⚡', '🎯', '💎', '🚀', '🏆', '✨', '🔥']
    html = ''
    
    for i, service in enumerate(services_list):
        icon = icons[i % len(icons)]
        html += f'''
                <div class="service-card fade-in">
                    <div class="service-icon">{icon}</div>
                    <h3>{service['title']}</h3>
                    <p>{service['description']}</p>
                </div>'''
    
    return html

def generate_contact_items(data):
    """Generate contact items HTML"""
    html = ''
    
    # Address
    if data.get('address'):
        html += f'''
                    <div class="contact-item">
                        <div class="contact-icon">📍</div>
                        <div class="contact-details">
                            <h4>Adres</h4>
                            <p>{data['address']}</p>
                        </div>
                    </div>'''
    
    # Phone
    if data.get('phones') and len(data['phones']) > 0:
        phone = data['phones'][0]
        html += f'''
                    <div class="contact-item">
                        <div class="contact-icon">📞</div>
                        <div class="contact-details">
                            <h4>Telefoon</h4>
                            <p><a href="tel:{phone.replace(' ', '').replace('-', '')}">{phone}</a></p>
                        </div>
                    </div>'''
    
    # Email
    if data.get('emails') and len(data['emails']) > 0:
        email = data['emails'][0]
        html += f'''
                    <div class="contact-item">
                        <div class="contact-icon">✉️</div>
                        <div class="contact-details">
                            <h4>Email</h4>
                            <p><a href="mailto:{email}">{email}</a></p>
                        </div>
                    </div>'''
    
    return html

def generate_map_html(address):
    """Generate Google Maps embed"""
    if address:
        encoded_address = address.replace(' ', '+')
        return f'''
                    <iframe 
                        width="100%" 
                        height="100%" 
                        frameborder="0" 
                        style="border:0; border-radius: 20px;" 
                        src="https://www.google.com/maps?q={encoded_address}&output=embed"
                        allowfullscreen>
                    </iframe>'''
    return ''

def generate_about_image(business_type):
    """Generate placeholder image for about section"""
    placeholder_images = {
        'automotive': 'https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=800&q=80',
        'restaurant': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
        'education': 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80'
    }
    
    image_url = placeholder_images.get(business_type, placeholder_images['automotive'])
    return f'<img src="{image_url}" alt="About Us">'

def generate_page(data, services, business_type, about_content, about_subtitle, services_subtitle):
    """Generate a complete page"""
    colors = get_color_scheme(business_type)
    services_html = generate_services_html(services)
    contact_items_html = generate_contact_items(data)
    map_html = generate_map_html(data.get('address'))
    about_image_html = generate_about_image(business_type)
    
    replacements = {
        '{{BUSINESS_NAME}}': data.get('business_name', 'Uw Bedrijf'),
        '{{TAGLINE}}': 'Professionele dienstverlening',
        '{{DESCRIPTION}}': data.get('description', 'Welkom bij ons bedrijf'),
        '{{PRIMARY_COLOR}}': colors['primary'],
        '{{SECONDARY_COLOR}}': colors['secondary'],
        '{{ACCENT_COLOR}}': colors['accent'],
        '{{LOGO_HTML}}': '',
        '{{HERO_DESCRIPTION}}': data.get('description', 'Welkom bij ons bedrijf'),
        '{{ABOUT_SUBTITLE}}': about_subtitle,
        '{{ABOUT_CONTENT}}': about_content,
        '{{ABOUT_IMAGE}}': about_image_html,
        '{{SERVICES_SUBTITLE}}': services_subtitle,
        '{{SERVICES_LIST}}': services_html,
        '{{CONTACT_SUBTITLE}}': 'We staan voor u klaar. Neem vrijblijvend contact op!',
        '{{CONTACT_ITEMS}}': contact_items_html,
        '{{MAP_HTML}}': map_html,
        '{{YEAR}}': str(datetime.now().year),
        '{{FOOTER_LINKS}}': ''
    }
    
    html = template
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)
    
    return html

# =============================================================================
# EXAMPLE 1: Vakgarage Blokhuis
# =============================================================================

vakgarage_data = {
    "business_name": "Vakgarage Blokhuis",
    "description": "Al meer dan 65 jaar uw betrouwbare autobedrijf in Bunschoten-Spakenburg. BOVAG en RDW erkend voor verkoop, onderhoud, reparatie en schade.",
    "address": "Haarburg 1, 3751 LM Bunschoten-Spakenburg",
    "phones": ["033 298 14 98"],
    "emails": ["info@vakgarageblokhuis.nl"]
}

vakgarage_about = '''
                    <h3>Meer dan 65 jaar vakmanschap</h3>
                    <p>Vakgarage Blokhuis is al sinds 1958 een begrip in Bunschoten-Spakenburg. Wat begon als een kleine garage is uitgegroeid tot een volledig BOVAG en RDW erkend autobedrijf.</p>
                    <p>Of het nu gaat om de aankoop van een nieuwe auto, een APK-keuring, groot onderhoud of schadeherstel - bij ons bent u verzekerd van vakkundig werk door gecertificeerde monteurs. Eerlijkheid, transparantie en klanttevredenheid staan bij ons altijd voorop.</p>
                    <p>Ook voor elektrische fietsen (Puch en Knaap) bent u bij ons aan het juiste adres. Van verkoop tot onderhoud - wij hebben de kennis en ervaring.</p>'''

vakgarage_services = [
    {"title": "Verkoop Auto's", "description": "Breed aanbod nieuwe en occasion auto's met BOVAG garantie en transparante prijsstelling."},
    {"title": "Onderhoud & APK", "description": "Professioneel onderhoud en APK-keuring door RDW erkende monteurs."},
    {"title": "Reparatie & Diagnose", "description": "Moderne diagnoseapparatuur voor snelle en accurate probleemopsporing."},
    {"title": "Schadeherstel", "description": "Van kleine deuk tot grote schade - wij herstellen uw auto volledig."},
    {"title": "E-bikes", "description": "Specialist in Puch en Knaap elektrische fietsen. Verkoop en service."},
    {"title": "65+ Jaar Ervaring", "description": "Een familiebedrijf met generaties vakmanschap en klanttevredenheid."}
]

print("1️⃣  Generating Vakgarage Blokhuis...")
vakgarage_html = generate_page(
    vakgarage_data,
    vakgarage_services,
    'automotive',
    vakgarage_about,
    'Uw betrouwbare autobedrijf sinds 1958',
    'Van verkoop tot onderhoud - alles onder één dak'
)

output_path = Path(__file__).parent / 'vakgarageblokhuis.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(vakgarage_html)
print(f"✓ Generated: {output_path}")

# =============================================================================
# EXAMPLE 2: Restaurant De Mandemaaker
# =============================================================================

mandemaaker_data = {
    "business_name": "Restaurant De Mandemaaker",
    "description": "Michelin en Gault Millau erkend restaurant aan de historische museumhaven van Spakenburg. Gespecialiseerd in verse vis en zeevruchten.",
    "address": "Kerkstraat 103, 3751 AT Spakenburg",
    "phones": ["033 298 02 55"],
    "emails": ["info@demandemaaker.nl"]
}

mandemaaker_about = '''
                    <h3>Culinair genieten aan de haven</h3>
                    <p>Restaurant De Mandemaaker combineert eigentijdse gastronomie met de rijke visserstraditie van Spakenburg. Onze locatie aan de museumhaven biedt een unieke sfeer en adembenemend uitzicht.</p>
                    <p>Chef-kok en zijn team werken uitsluitend met dagverse producten van de hoogste kwaliteit. Onze specialiteit? Verse vis en zeevruchten, vakkundig bereid met moderne technieken en respect voor traditie.</p>
                    <p>Onze toewijding aan culinaire excellence is erkend door zowel Michelin als Gault Millau. Maar het belangrijkste is dat onze gasten keer op keer met een glimlach de deur uitgaan.</p>'''

mandemaaker_services = [
    {"title": "Verse Vis & Zeevruchten", "description": "Dagverse vis en zeevruchten van de beste kwaliteit, vakkundig bereid."},
    {"title": "Eigentijdse Keuken", "description": "Moderne gerechten met respect voor traditie en verrassende smaken."},
    {"title": "Michelin Erkend", "description": "Erkend in Michelin Guide en Gault Millau voor uitmuntende kwaliteit."},
    {"title": "Unieke Locatie", "description": "Dineren met uitzicht op de historische museumhaven van Spakenburg."},
    {"title": "Lunch & Diner", "description": "Open di vanaf 17:00, wo-za vanaf 12:00. Reserveren aanbevolen."},
    {"title": "Groepen & Events", "description": "Speciale arrangementen voor groepen en bijzondere gelegenheden."}
]

print("\n2️⃣  Generating Restaurant De Mandemaaker...")
mandemaaker_html = generate_page(
    mandemaaker_data,
    mandemaaker_services,
    'restaurant',
    mandemaaker_about,
    'Waar traditie en moderniteit samenkomen',
    'Een culinaire ervaring om nooit te vergeten'
)

output_path = Path(__file__).parent / 'demandemaaker.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(mandemaaker_html)
print(f"✓ Generated: {output_path}")

# =============================================================================
# EXAMPLE 3: Rijschool Vermeer
# =============================================================================

rijschool_data = {
    "business_name": "Rijschool Vermeer",
    "description": "Al meer dan 45 jaar dé rijschool in Bunschoten, Amersfoort, Nijkerk en Baarn. Van auto tot vrachtwagen - wij leiden u op tot een veilige chauffeur.",
    "address": "De Hooistreep 26, 3751 LW Bunschoten-Spakenburg",
    "phones": ["033 299 00 63", "06 22 48 24 06"],
    "emails": ["wim@rijschoolvermeer.nl"]
}

rijschool_about = '''
                    <h3>45 jaar ervaring in rijopleidingen</h3>
                    <p>Rijschool Vermeer staat sinds 1979 garant voor kwalitatieve rijopleidingen in de regio. Met meer dan vier decennia ervaring weten wij precies hoe we u kunnen helpen om een veilige en zelfverzekerde bestuurder te worden.</p>
                    <p>Ons team van gediplomeerde en ervaren instructeurs biedt persoonlijke begeleiding, van theorie tot praktijkexamen. We rijden in moderne lesauto's die perfect zijn uitgerust voor uw opleiding.</p>
                    <p>Of u nu uw auto-rijbewijs wilt halen, een vrachtwagenrijbewijs nodig heeft, of code 95 nascholing moet volgen - bij Rijschool Vermeer zit u goed!</p>'''

rijschool_services = [
    {"title": "Auto Rijbewijs (B)", "description": "Complete rijopleiding van theorie tot praktijkexamen. Flexibele lestijden."},
    {"title": "Vrachtwagen (C/CE)", "description": "Professionele vrachtwagenopleidingen voor wie in transport wil werken."},
    {"title": "Code 95", "description": "Nascholing voor vrachtwagen- en buschauffeurs. Houd uw bevoegdheid actueel."},
    {"title": "Aanhangwagen (BE)", "description": "Leer veilig rijden met aanhangwagen of caravan. Praktische training."},
    {"title": "Bromfiets (AM)", "description": "Bromfietscursus voor jongeren. Begin jong met verkeerservaring."},
    {"title": "45 Jaar Ervaring", "description": "Ruim vier decennia ervaring in het opleiden van veilige chauffeurs."}
]

print("\n3️⃣  Generating Rijschool Vermeer...")
rijschool_html = generate_page(
    rijschool_data,
    rijschool_services,
    'education',
    rijschool_about,
    'Leren rijden bij de beste',
    'Van theorie tot rijbewijs - wij begeleiden u'
)

output_path = Path(__file__).parent / 'rijschoolvermeer.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(rijschool_html)
print(f"✓ Generated: {output_path}")

print("\n" + "="*70)
print("✨ All example frontpages generated successfully!")
print("="*70)
print("\nView them at:")
print(f"• file://{Path(__file__).parent.absolute()}/vakgarageblokhuis.html")
print(f"• file://{Path(__file__).parent.absolute()}/demandemaaker.html")
print(f"• file://{Path(__file__).parent.absolute()}/rijschoolvermeer.html")
print("\nThese pages showcase:")
print("✓ Modern, responsive design")
print("✓ Custom color schemes per business type")
print("✓ Professional content and layout")
print("✓ Smooth animations and interactions")
print("✓ Mobile-first approach")
