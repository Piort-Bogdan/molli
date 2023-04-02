from docxtpl import DocxTemplate
from pathlib import Path
from datetime import date
def get_age(date_of_birth):
    diff_date = (date.today() - date_of_birth).days
    years = diff_date // 365
    months = (diff_date % 365) // 30
    days = (diff_date % 365) % 30
    if (years != 0 and years > 4) and months != 0:
        age = f'{years} лет, {abs(months)} мес.'
    elif (years != 0 and years <= 4) and months != 0:
        age = f'{years} года, {abs(months)} мес.'
    elif years == 0 and months != 0:
        age = f'{months} мес.'
    elif years == 0 and months == 0 and days != 0:
        age = f'{abs(days)} дней'
    else:
        age = '     '
    return age


def create_docx(data, id):
    print(data)
    if data['send_to_email']:
        template_path = Path(__file__).parent / 'Vet_card_01.docx'
        doc = DocxTemplate(template_path)
        todays_date = date.today().strftime('%Y-%m-%d')
        context = {
            'doctor': data['doctor'],
            'pet_name': data['pet'],
            'full_name': data['owner_name'],
            'date': todays_date,
            'gender': data['gender'],
            'weight': data['weight'],
            'tel': data['phone_number'],
            'species': data['species'],
            'temp': data['temperature'],
            'date_of_birth': data['year_of_birth'],
            'preliminary_diagnosis': data['preliminary_diagnosis'],
            'appointments': data['appointments'],
            'recommended_researches': data['recommended_researches'],
            'id': id,
            'breed': data['breed'],
            'age': get_age(data['year_of_birth']),
        }
        doc.render(context)
        current_reception = Path(__file__).parent / f'Molli_reception_{todays_date}_{data["pet"]}.docx'
        doc.save(current_reception)


def conver_docx_to_pdf():
    pass
