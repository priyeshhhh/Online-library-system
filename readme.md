 Install packages:

   pip install openpyxl
   pip install django openpyxl django-crispy-forms


Update settings.py:
   - Add 
   'library', 
   'crispy_forms', 
   'crispy_bootstrap5' to INSTALLED_APPS  
   - Set:
     CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  
     CRISPY_TEMPLATE_PACK = "bootstrap5"  
   - Add 'templates' folder to TEMPLATES['DIRS']   

Django==5.1.2
openpyxl==3.1.2
django-crispy-forms==2.1
crispy-bootstrap5==2022.1

In this project task Project :

   - CRUD operations
   - Pagination
   - Export to Excel
   - Bootstrap 5 UI (crispy forms)