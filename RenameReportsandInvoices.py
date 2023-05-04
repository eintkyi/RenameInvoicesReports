import fitz
import datetime
import string
import re
from os import chdir, rename
from glob import glob as glob

directory = r'C:\Users\ekyi\Invoices'
chdir(directory)

pdf_list = glob('[Inv]*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
    new_file_name = text.split("\n")[0].strip()

    new_file_name1 = re.sub(r'/','-',new_file_name)
    str(new_file_name1)
    new_file_name1 = datetime.datetime.strptime(new_file_name1, '%m-%d-%Y').date()
    new_file_name1 = new_file_name1.strftime('%Y-%m-%d')
    new_file_name2 = text.split("\n")[1]
    new_file_name3 = text.split("\n")[2]
    final_file_name = [new_file_name1, new_file_name2, new_file_name3]
    final_file_name = ' '.join(final_file_name)
    rename(pdf, final_file_name + '.pdf')


pdf_list = glob('[Rpt]*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
    new_file_name = text.split("\n")[0].strip()
    new_file_name1 = re.sub(r',', ' ', new_file_name)
    new_file_name1 = datetime.datetime.strptime(new_file_name1, "%B %d %Y").strftime('%Y-%m-%d')
    new_file_name2 = text.split("\n")[6]
    new_file_name2 = re.sub(r'OrderNo.: ', 'REPORT INVOICE ', new_file_name2)
    final_file_name = [new_file_name1, new_file_name2]
    final_file_name = ' '.join(final_file_name)
    rename(pdf, final_file_name + '.pdf')
