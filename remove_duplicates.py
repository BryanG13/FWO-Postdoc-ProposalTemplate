#!/usr/bin/env python3
"""
Script to remove duplicate entries from a BibTeX file.
"""

import re
from collections import defaultdict

def read_bibtex_file(file_path):
    """Read the BibTeX file and return its content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_bibtex_entries(content):
    """Parse BibTeX entries and return a dictionary of entry_key -> (entry_text, line_number)."""
    entries = {}
    entry_counts = defaultdict(int)
    
    # Pattern to match BibTeX entries
    pattern = r'@(\w+)\s*\{\s*([^,\s}]+)\s*,'
    
    lines = content.split('\n')
    current_entry = ""
    current_key = None
    current_type = None
    brace_count = 0
    in_entry = False
    start_line = 0
    
    for i, line in enumerate(lines):
        # Check if line starts a new entry
        match = re.match(pattern, line.strip())
        if match:
            # Save previous entry if it exists
            if current_key and current_entry:
                entries[current_key] = {
                    'content': current_entry.strip(),
                    'line': start_line,
                    'type': current_type,
                    'count': entry_counts[current_key]
                }
            
            # Start new entry
            current_type = match.group(1)
            current_key = match.group(2)
            entry_counts[current_key] += 1
            current_entry = line
            in_entry = True
            start_line = i
            brace_count = line.count('{') - line.count('}')
        elif in_entry:
            current_entry += '\n' + line
            brace_count += line.count('{') - line.count('}')
            
            # Check if entry is complete
            if brace_count <= 0:
                in_entry = False
                if current_key:
                    entries[current_key] = {
                        'content': current_entry.strip(),
                        'line': start_line,
                        'type': current_type,
                        'count': entry_counts[current_key]
                    }
                current_entry = ""
                current_key = None
                current_type = None
        elif not in_entry and line.strip() and not line.startswith('%'):
            # This handles the header comments
            if not entries.get('__header__'):
                entries['__header__'] = {
                    'content': line,
                    'line': i,
                    'type': 'header',
                    'count': 1
                }
            else:
                entries['__header__']['content'] += '\n' + line
    
    # Handle last entry
    if current_key and current_entry:
        entries[current_key] = {
            'content': current_entry.strip(),
            'line': start_line,
            'type': current_type,
            'count': entry_counts[current_key]
        }
    
    return entries, entry_counts

def find_duplicates(entry_counts):
    """Find entries that appear more than once."""
    duplicates = {}
    for key, count in entry_counts.items():
        if count > 1:
            duplicates[key] = count
    return duplicates

def remove_duplicates(file_path):
    """Remove duplicate entries from BibTeX file."""
    print(f"Reading file: {file_path}")
    content = read_bibtex_file(file_path)
    
    print("Parsing BibTeX entries...")
    entries, entry_counts = parse_bibtex_entries(content)
    
    print("Finding duplicates...")
    duplicates = find_duplicates(entry_counts)
    
    if duplicates:
        print(f"\nFound {len(duplicates)} duplicate entry keys:")
        for key, count in duplicates.items():
            print(f"  - {key}: appears {count} times")
        
        # Create new content with duplicates removed
        print("\nRemoving duplicates...")
        new_content = ""
        
        # Add header if it exists
        if '__header__' in entries:
            new_content += entries['__header__']['content'] + '\n\n'
        
        # Add unique entries (sorted by entry key for consistency)
        seen = set()
        for key in sorted(entries.keys()):
            if key != '__header__' and key not in seen:
                new_content += entries[key]['content'] + '\n\n'
                seen.add(key)
        
        # Write the cleaned content back to the file
        backup_path = file_path + '.backup'
        print(f"Creating backup: {backup_path}")
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Writing cleaned file: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content.rstrip() + '\n')
        
        print(f"\nSummary:")
        print(f"  - Original entries: {len(entries) - (1 if '__header__' in entries else 0)}")
        print(f"  - Duplicate keys: {len(duplicates)}")
        print(f"  - Total duplicates removed: {sum(duplicates.values()) - len(duplicates)}")
        print(f"  - Final unique entries: {len(seen)}")
        
    else:
        print("No duplicates found!")

if __name__ == "__main__":
    file_path = "/Users/bryangalarza/Library/CloudStorage/GoogleDrive-bryangalarza1303@gmail.com/My Drive/6. Postdoc UA/The future/FWO/2026/FWO_proposal/FWO.bib"
    remove_duplicates(file_path)