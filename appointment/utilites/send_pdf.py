from docxtpl import DocxTemplate
from pathlib import Path
from datetime import date


def create_word_and_convert_to_pdf(data):
    if data['send_to_email']:
        template_path = Path(__file__).parent / 'Vet_card_01.docx'
        doc = DocxTemplate(template_path)
        context = {
            'doctor': data['doctor'],
            'pet_name': data['pet'],
            'full_name': data['owner'],
            'date': date.today(),
            'gender': data['gender'],
            'weight': data['weight'],
            'tel': data['phone_number'],
            'species': data['species'],
            'temp': data['temperature'],
            'date_of_birth': data['year_of_birth'],
            'preliminary_diagnosis': data['preliminary_diagnosis'],
            'appointments': data['appointments'],
            'recommended_researches': data['recommended_researches'],
            'id': data['id'],
        }
        doc.render(context)
        current_reception = Path(__file__).parent / f'Molli_reception_{data["date"]},{data["pet"]}.docx'
        doc.save(current_reception)
