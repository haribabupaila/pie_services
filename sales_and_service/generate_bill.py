from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_TAB_ALIGNMENT
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml, OxmlElement

class generate_service_bill:
    def create_bill(self, data_dict):
        document=Document()

        section = document.sections[0]  # Accessing the first section

        # Adjust the section's border properties
        section.top_margin = Inches(1)  # Example of adjusting top margin (change as needed)
        section.bottom_margin = Inches(1)  # Example of adjusting bottom margin (change as needed)
        section.left_margin = Inches(1)  # Example of adjusting left margin (change as needed)
        section.right_margin = Inches(1) 

        heading = document.add_heading("ROYAL COMPUTER SERVICES", 0)

        for paragraph in document.paragraphs:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        address_text_heading = "Jangam St, junction, Paralakhemundi, Odisha 761200 . Phone: 9700927779, 9000820760"
        address_heading_text = heading.add_run("\n\n" + address_text_heading)
        address_heading_text.font.size = Pt(14)
        address_heading_text.font.bold = True 

        gst_text_heading = "GST:  AATVS6598H"
        gst_heading_text = heading.add_run("\n\n" + gst_text_heading)
        gst_heading_text.font.size = Pt(14)
        gst_heading_text.font.bold = True 

        combined_p = document.add_paragraph()
        # for NAME
        name_p = combined_p.add_run('NAME: ').bold = True 
        name_p = combined_p.add_run(f' {data_dict["last_name"]} {data_dict["first_name"]}')

        for run in combined_p.runs:
            if 'NAME:' in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            elif data_dict["last_name"] in run.text or data_dict["first_name"] in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

        # for type_of_gadget
        type_of_gadget_p = combined_p.add_run(' ' * (70 - len(f'{data_dict["last_name"]} {data_dict["first_name"]}')) + 'TYPE OF GADGET: ').bold = True
        type_of_gadget_p = combined_p.add_run(f' {data_dict["type_of_gadget"]}')

        for run in combined_p.runs:
            if 'TYPE OF GADGET:' in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
            elif data_dict["type_of_gadget"] in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        combined_p = document.add_paragraph()
        # for mobile_number
        mobile_p = combined_p.add_run('MOBILE: ').bold = True 
        mobile_p = combined_p.add_run(f' {data_dict["mobile_number"]}')

        for run in combined_p.runs:
            if 'MOBILE:' in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            elif data_dict["mobile_number"] in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

        # for model_number
        model_number_p = combined_p.add_run(' ' * (64 - len(f'{data_dict["mobile_number"]}')) + 'MODEL NUMBER: ').bold = True
        model_number_p = combined_p.add_run(f' {data_dict["model_number"]}')

        for run in combined_p.runs:
            if 'MODEL NUMBER:' in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
            elif data_dict["model_number"] in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        combined_p = document.add_paragraph()
        # for email
        email_p = combined_p.add_run('EMAIL: ').bold = True 
        email_p = combined_p.add_run(f' {data_dict["email"]}')

        for run in combined_p.runs:
            if 'EMAIL:' in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            elif data_dict["email"] in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

        # for serial_number
        serial_number_p = combined_p.add_run(' ' * (61 - len(f'{data_dict["email"]}')) + 'SERIAL NUMBER: ').bold = True
        serial_number_p = combined_p.add_run(f' {data_dict["serial_number"]}')

        for run in combined_p.runs:
            if 'SERIAL NUMBER:' in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
            elif data_dict["serial_number"] in run.text:
                run.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        #for address
        address_p = document.add_paragraph()
        address_p.add_run('ADDRESS: ').bold = True 
        address_p.add_run(f' {data_dict["address"]}')

        #add space
        document.add_paragraph() 

        #specifications
        specifications_p = document.add_paragraph()
        specifications_p.add_run('SPECIFICATIONS:    ').bold = True
        specific_entry_p = specifications_p.add_run(f'{data_dict["specifications"]}')
        specific_entry_p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        specific_entry_p.font.color.rgb = RGBColor(0, 0, 0)
        specific_entry_p.bold = False

        #Remarks
        remarks_p = document.add_paragraph()
        remarks_p.add_run('RAMARKS:    ').bold = True
        remarks_entry_p = remarks_p.add_run(f'{data_dict["remarks"]}')
        remarks_entry_p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        remarks_entry_p.font.color.rgb = RGBColor(0, 0, 0)
        remarks_entry_p.bold = False

        #Warrenty
        warrenty_period_p = document.add_paragraph()
        warrenty_period_p.add_run('WARRENTY PERIOD:    ').bold = True
        warrenty_entry_p = warrenty_period_p.add_run(f'{data_dict["warrenty_period"]}')
        warrenty_entry_p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        warrenty_entry_p.font.color.rgb = RGBColor(0, 0, 0)
        warrenty_entry_p.bold = False

        payment_table = document.add_table(rows=6, cols=4)
        payment_table.columns[1].width = Pt(3.5)
        for row in payment_table.rows:
            for cell in row.cells:
                cell.text = 'Sample Text'
        border_color = RGBColor(0, 82, 155)  # RGB color code for blue

        
        document.add_paragraph(
            'first item in unordered list', style='List Bullet'
        )
        records = (
            (3, '101', 'Spam'),
            (7, '422', 'Eggs'),
            (4, '631', 'Spam, spam, eggs, and spam')
        )

        table = document.add_table(rows=1, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Qty'
        hdr_cells[1].text = 'Id'
        hdr_cells[2].text = 'Desc'
        for qty, id, desc in records:
            row_cells = table.add_row().cells
            row_cells[0].text = str(qty)
            row_cells[1].text = id
            row_cells[2].text = desc

        document.save('demo.docx')

obj = generate_service_bill()
obj.create_bill({   
    "type_of_gadget":"laptop",
    "model_number":"DESKTOP-TR2QICC",
    "serial_number":"jlfslkfjdslk",
    "specifications":"ksldflksjfl",
    "remarks":"ksfslfs",
    "price":"20000",
    "warrenty_period":"2",
    "mobile_number":"8658102648",
    "first_name":"deepak",
    "last_name":"paila",
    "email":"deepak@gmail.com",
    "address":"padmapur"
})

