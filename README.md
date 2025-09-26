# FWO Postdoc Proposal Template

A LaTeX template for preparing postdoctoral fellowship applications to the Research Foundation - Flanders (FWO). This template provides a structured format that complies with FWO guidelines and formatting requirements.

## 📄 Project Overview

This repository contains a complete LaTeX template for FWO postdoctoral fellowship applications. The template follows FWO's specific formatting requirements including Carlito 11 font, single line spacing, and 2.5cm margins.

## 🗂️ File Structure

### Core LaTeX Files
- **`main.tex`** - Main LaTeX document containing the complete proposal structure with sections for rationale, methodology, timeline, and references
- **`main.pdf`** - Compiled PDF output of the proposal document
- **`FWO.bib`** - BibTeX bibliography file containing research references

### Utility Scripts
- **`remove_duplicates.py`** - Python script to automatically detect and remove duplicate entries from BibTeX files, helping maintain clean bibliography

### Documentation
- **`README.md`** - This documentation file
- **`LICENSE`** - Project license information

## 🚀 Getting Started

### Prerequisites
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- BibTeX for bibliography management
- Python 3.x (for running the duplicate removal script)

### Compiling the Document
1. Compile the main document:
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```

2. Or use latexmk for automatic compilation:
   ```bash
   latexmk -pdf main.tex
   ```

### Managing Bibliography
- Add your references to `FWO.bib` following BibTeX format
- Use the `remove_duplicates.py` script to clean duplicate entries:
  ```bash
  python remove_duplicates.py
  ```

## 📋 Template Features

- **FWO Compliant Formatting**: Follows official FWO guidelines for font (Carlito 11), spacing, and margins
- **Structured Sections**: Pre-defined sections for all required proposal components
- **Professional Styling**: Clean layout with custom boxes and formatting
- **Bibliography Management**: Integrated BibTeX support with IEEE citation style
- **Comprehensive Packages**: Includes essential LaTeX packages for figures, tables, algorithms, and mathematical notation

## 🎯 Usage Instructions

1. **Clone or download** this repository
2. **Edit `main.tex`** to include your research proposal content
3. **Update `FWO.bib`** with your references
4. **Compile** the document to generate your PDF proposal
5. **Review** the output and make necessary adjustments

## 🔧 Customization

The template can be easily customized by:
- Modifying section content in `main.tex`
- Adding or removing LaTeX packages as needed
- Adjusting the custom box styling
- Adding figures, tables, or algorithms using the included packages
