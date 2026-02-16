#!/usr/bin/env python3
"""
Business Booster Frontpage Generator
Takes prospect data (JSON) and generates a beautiful HTML page using the template
"""

import json
import sys
from pathlib import Path
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
        },
        'default': {
            'primary': '#2563eb',  # Blue
            'secondary': '#7c3aed',  # Purple
            'accent': '#a78bfa'
        }
    }
    return schemes.get(business_type, schemes['default'])

def detect_business_type(data):
    """Try to detect business type from data"""
    description = (data.get('description', '') + ' ' + data.get('business_name', '')).lower()
    
    if any(word in description for word in ['garage', 'auto', 'car', 'dealer', 'bovag']):
        return 'automotive'
    elif any(word in description for word in ['restaurant', 'cafe', 'eten', 'drinken', 'michelin']):
        return 'restaurant'
    elif any(word in description for word in ['rijschool', 'rijles', 'driving', 'les', 'opleiding']):
        return 'education'
    
    return 'default'

def generate_logo_html(data):
    """Generate logo HTML if available"""
    if data.get('logo_url'):
        return f'<img src="{data["logo_url"]}" alt="{data["business_name"]} Logo" class="hero-logo">'
    return ''

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
    """Generate Google Maps embed or placeholder"""
    if address:
        # Encode address for Google Maps
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
    else:
        return '''
                    <div class="map-placeholder">
                        <div style="font-size: 3rem; margin-bottom: 1rem;">📍</div>
                        <p>Google Maps</p>
                    </div>'''

def generate_about_content(data, business_type):
    """Generate about section content"""
    description = data.get('description', 'Een professioneel bedrijf met jarenlange ervaring.')
    
    content = f'''
                    <h3>Welkom bij {data['business_name']}</h3>
                    <p>{description}</p>
                    <p>Met jarenlange ervaring en een passie voor kwaliteit, staan wij voor u klaar. 
                    Ons team van professionals zorgt ervoor dat u de beste service ontvangt.</p>
                    <p>Neem vandaag nog contact met ons op en ontdek wat wij voor u kunnen betekenen!</p>'''
    
    return content

def generate_about_image(business_type):
    """Generate placeholder image for about section"""
    # In production, you'd use actual images
    placeholder_images = {
        'automotive': 'https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=800&q=80',
        'restaurant': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
        'education': 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
        'default': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80'
    }
    
    image_url = placeholder_images.get(business_type, placeholder_images['default'])
    return f'<img src="{image_url}" alt="About Us">'

def generate_frontpage(data, custom_services=None, output_file=None):
    """Generate complete frontpage HTML from data"""
    
    # Detect business type and get color scheme
    business_type = detect_business_type(data)
    colors = get_color_scheme(business_type)
    
    # Read template
    template_path = Path(__file__).parent / 'template.html'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Prepare default services if not provided
    if not custom_services:
        custom_services = [
            {
                'title': 'Professioneel',
                'description': 'Hoogwaardige dienstverlening met aandacht voor detail en kwaliteit.'
            },
            {
                'title': 'Betrouwbaar',
                'description': 'Jarenlange ervaring en een bewezen track record in de branche.'
            },
            {
                'title': 'Persoonlijk',
                'description': 'Elke klant is uniek. Wij bieden maatwerk dat perfect bij u past.'
            }
        ]
    
    # Generate HTML components
    logo_html = generate_logo_html(data)
    services_html = generate_services_html(custom_services)
    contact_items_html = generate_contact_items(data)
    map_html = generate_map_html(data.get('address'))
    about_content_html = generate_about_content(data, business_type)
    about_image_html = generate_about_image(business_type)
    
    # Create replacements dictionary
    replacements = {
        '{{BUSINESS_NAME}}': data.get('business_name', 'Uw Bedrijf'),
        '{{TAGLINE}}': 'Professionele dienstverlening',
        '{{DESCRIPTION}}': data.get('description', 'Welkom bij ons bedrijf'),
        '{{PRIMARY_COLOR}}': colors['primary'],
        '{{SECONDARY_COLOR}}': colors['secondary'],
        '{{ACCENT_COLOR}}': colors['accent'],
        '{{LOGO_HTML}}': logo_html,
        '{{HERO_DESCRIPTION}}': data.get('description', 'Welkom bij ons bedrijf. Wij staan voor kwaliteit en service.'),
        '{{ABOUT_SUBTITLE}}': 'Uw partner in kwaliteit en service',
        '{{ABOUT_CONTENT}}': about_content_html,
        '{{ABOUT_IMAGE}}': about_image_html,
        '{{SERVICES_SUBTITLE}}': 'Ontdek wat wij voor u kunnen betekenen',
        '{{SERVICES_LIST}}': services_html,
        '{{CONTACT_SUBTITLE}}': 'We staan voor u klaar. Neem vrijblijvend contact op!',
        '{{CONTACT_ITEMS}}': contact_items_html,
        '{{MAP_HTML}}': map_html,
        '{{YEAR}}': str(datetime.now().year),
        '{{FOOTER_LINKS}}': '<a href="#about">Over Ons</a><a href="#services">Diensten</a><a href="#contact">Contact</a>'
    }
    
    # Apply replacements
    html = template
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)
    
    # Save to file
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Generated frontpage: {output_file}")
    
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-frontpage.py <data.json> [output.html]")
        print("Example: python generate-frontpage.py vakgarageblokhuis.json output.html")
        sys.exit(1)
    
    # Load prospect data
    json_file = sys.argv[1]
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Determine output file
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = json_file.replace('.json', '.html')
    
    # Generate frontpage
    generate_frontpage(data, output_file=output_file)
    print(f"\n✨ Preview: file://{Path(output_file).absolute()}")

if __name__ == '__main__':
    main()
