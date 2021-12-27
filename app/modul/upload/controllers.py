#Import flask dependencies
from flask import Blueprint, request, render_template
from openpyxl import load_workbook 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import pandas as pd
import os

mod_upload = Blueprint('upload',__name__,url_prefix='/mod_upload')
mod_uploader = Blueprint('uploader',__name__,url_prefix='/mod_uploader')

mainTittle = 'Clustering [KMeans]'

@mod_upload.route('', methods = ['GET','POST'])
def upload_file():
	return render_template('upload/upload.html')

@mod_uploader.route('', methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		subTitle = ("Data Excel")
		f = request.files['file']
		f.save(os.path.join('app/upload_data', 'DATA EXCEL.xlsx'))
		wb = load_workbook(filename = 'app/upload_data/DATA EXCEL.xlsx')
		sheet_ranges = wb['Sheet5']
		data = pd.DataFrame(sheet_ranges.values)
		button = [(str(request.url_root))]
		
		return render_template('upload/tables.html',
			tables=[data.to_html (classes='Alumni')], 
			text =['Clustering [KMeans]', subTitle], 
			button=button, 
			data=data)
