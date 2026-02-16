#!/usr/bin/env python3
"""
Business Booster Prospect Scanner
Scrapes a website and extracts business information for lead generation
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import sys
from urllib.parse import urljoin, urlparse

def clean_text(text):
    """Clean extracted text"""
    if not text:
        return ""
    return " ".join(text.split()).strip()

def extract_phone(soup, url):
    """Extract phone numbers from page"""
    phones = []
    # Look in text content
    text = soup.get_text()
    phone_patterns = [
        r'\b0\d{1,3}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}\b',  # Dutch landline
        r'\b06[\s-]?\d{8}\b',  # Dutch mobile
        r'\b\+31[\s-]?\d{1,3}[\s-]?\d{6,8}\b',  # International
    ]
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        phones.extend(matches)
    
    # Look in href="tel:"
    for link in soup.find_all('a', href=re.compile(r'^tel:')):
        phone = link.get('href').replace('tel:', '').strip()
        phones.append(phone)
    
    return list(set(phones))[:3]  # Return up to 3 unique phones

def extract_email(soup, url):
    """Extract email addresses"""
    emails = []
    # Look in mailto links
    for link in soup.find_all('a', href=re.compile(r'^mailto:')):
        email = link.get('href').replace('mailto:', '').split('?')[0].strip()
        emails.append(email)
    
    # Look in text content
    text = soup.get_text()
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, text)
    emails.extend(matches)
    
    return list(set(emails))[:2]  # Return up to 2 unique emails

def extract_address(soup):
    """Try to extract business address"""
    # Look for common address patterns
    text = soup.get_text()
    # Dutch address pattern: street + number, postcode + city
    address_pattern = r'([A-Z][a-z\s]+\d+[a-z]?),?\s*(\d{4}\s?[A-Z]{2}\s+[A-Z][a-z\s-]+)'
    matches = re.findall(address_pattern, text)
    if matches:
        return f"{matches[0][0]}, {matches[0][1]}"
    return None

def extract_logo(soup, base_url):
    """Try to find the logo"""
    # Look for common logo patterns
    logo_selectors = [
        'img[class*="logo"]',
        'img[id*="logo"]',
        '.logo img',
        '#logo img',
        'header img:first-of-type',
        '.header img:first-of-type',
    ]
    
    for selector in logo_selectors:
        logo = soup.select_one(selector)
        if logo and logo.get('src'):
            return urljoin(base_url, logo.get('src'))
    
    return None

def extract_business_name(soup, url):
    """Extract business name"""
    # Try title tag
    title = soup.find('title')
    if title:
        name = clean_text(title.string)
        # Clean up common suffixes
        name = re.sub(r'\s*[-|]\s*(Home|Homepage|Welkom).*$', '', name, flags=re.IGNORECASE)
        if name:
            return name
    
    # Try h1
    h1 = soup.find('h1')
    if h1:
        return clean_text(h1.get_text())
    
    # Fallback to domain name
    domain = urlparse(url).netloc.replace('www.', '').split('.')[0]
    return domain.title()

def extract_description(soup):
    """Extract business description/services"""
    # Try meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        return clean_text(meta_desc.get('content'))
    
    # Try to find about/intro paragraphs
    paragraphs = soup.find_all('p')
    for p in paragraphs[:5]:  # Check first 5 paragraphs
        text = clean_text(p.get_text())
        if len(text) > 50:  # Meaningful content
            return text[:300]  # First 300 chars
    
    return "Geen beschrijving beschikbaar"

def score_design(soup, url):
    """Score website design quality (1-10)"""
    score = 5  # Base score
    
    # Check for modern practices
    # Responsive meta tag
    if soup.find('meta', attrs={'name': 'viewport'}):
        score += 1
    else:
        score -= 2
    
    # CSS frameworks/modern styling
    stylesheets = soup.find_all('link', rel='stylesheet')
    if len(stylesheets) > 2:
        score += 1
    
    # JavaScript (indicates interactivity)
    scripts = soup.find_all('script')
    if len(scripts) > 3:
        score += 1
    
    # Check for outdated signs
    text = str(soup).lower()
    if 'table' in text and 'layout' in text:
        score -= 2  # Table-based layout
    if 'font' in text and 'face' in text:
        score -= 1  # Inline font tags
    if re.search(r'copyright.*20(0[0-9]|1[0-5])', text):
        score -= 2  # Old copyright
    
    # Check visual indicators
    images = soup.find_all('img')
    if len(images) < 3:
        score -= 1  # Too few images
    
    # SSL check
    if url.startswith('https://'):
        score += 1
    else:
        score -= 1
    
    return max(1, min(10, score))  # Clamp between 1-10

def scan_website(url):
    """Main scanning function"""
    # Ensure URL has protocol
    if not url.startswith('http'):
        url = 'https://' + url
    
    try:
        # Fetch the website
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all information
        data = {
            'url': url,
            'business_name': extract_business_name(soup, url),
            'description': extract_description(soup),
            'address': extract_address(soup),
            'phones': extract_phone(soup, url),
            'emails': extract_email(soup, url),
            'logo_url': extract_logo(soup, url),
            'design_score': score_design(soup, url),
            'status': 'success'
        }
        
        return data
        
    except requests.RequestException as e:
        return {
            'url': url,
            'status': 'error',
            'error': str(e)
        }

def main():
    if len(sys.argv) < 2:
        print("Usage: python prospect-scanner.py <url>")
        print("Example: python prospect-scanner.py vakgarageblokhuis.nl")
        sys.exit(1)
    
    url = sys.argv[1]
    print(f"Scanning {url}...\n")
    
    result = scan_website(url)
    
    # Pretty print JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Optionally save to file
    if len(sys.argv) > 2 and sys.argv[2] == '--save':
        domain = urlparse(result['url']).netloc.replace('www.', '')
        filename = f"{domain.replace('.', '_')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Saved to {filename}")

if __name__ == '__main__':
    main()
