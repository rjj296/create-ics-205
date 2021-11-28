#!/usr/bin/env python3

# Sample Call
# python3 create205.py "Event Name" "County Name" 11DEC21 07:00 12DEC21 17:00 VTAC11 VTAC12
############################################
# Expected Arguments:
# sys.argv[1] = name of event
# sys.argv[2] = County/Folder Name
# sys.argv[3] = Start Date
# sys.argv[4] = Start Time
# sys.argv[5] = End Date
# sys.argv[6] = End Time
# sys.argv[7] = CHAN1
# sys.argv[8] = CHAN2
# sys.argv[9] = CHAN3
# sys.argv[10] = CHAN4
# sys.argv[11] = CHAN5
# sys.argv[12] = CHAN6
# sys.argv[13] = CHAN7
# sys.argv[14] = CHAN8
############################################
# https://akdux.com/python/2020/10/31/python-fill-pdf-files.html

from datetime import datetime
import sys
import pdfrw

def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for annotation in template_pdf.pages[0][ANNOT_KEY]:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    if type(data_dict[key]) == bool:
                        if data_dict[key] == True:
                            annotation.update(pdfrw.PdfDict(
                                AS=pdfrw.PdfName('Yes')))
                    else:
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )
                        annotation.update(pdfrw.PdfDict(AP=''))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

RX_freq_dict = {'TXCALL1D': '154.9500 N','VMED28': '155.3400 N','VMED29': '155.3475 N','VLAW31': '155.4750 N','VLAW32': '155.4825 N','FIRE21': '154.2800 N','FIRE22': '154.2650 N','FIRE23': '154.2950 N','FIRE24': '154.2725 N','FIRE25': '154.2875 N','FIRE26': '154.3025 N','COMPAC': '159.2850 N','VCAL10': '155.7525 N','VTAC11': '151.1375 N','VTAC12': '154.4525 N','VTAC13': '158.7375 N','VTAC14': '159.4725 N','VTAC33': '159.4725 N','VTAC34': '158.7375 N','VTAC35': '159.4725 N','VTAC36': '151.1375 N','VTAC37': '154.4525 N','VTAC38': '158.7375 N','MARS1': '143.9750 N','MARS2': '143.9750 N'}
RX_tone_dict = {'TXCALL1D': '156.7','VMED28': '156.7','VMED29': '156.7','VLAW31': '156.7','VLAW32': '156.7','FIRE21': '156.7','FIRE22': '156.7','FIRE23': '156.7','FIRE24': '156.7','FIRE25': '156.7','FIRE26': '156.7','COMPAC': '127.3','VCAL10': '156.7','VTAC11': '156.7','VTAC12': '156.7','VTAC13': '156.7','VTAC14': '156.7','VTAC33': '136.5','VTAC34': '136.5','VTAC35': '136.5','VTAC36': '136.5','VTAC37': '136.5','VTAC38': '136.5','MARS1': '123.0','MARS2': '123.0'}
TX_freq_dict = {'TXCALL1D': '154.9500 N','VMED28': '155.3400 N','VMED29': '155.3475 N','VLAW31': '155.4750 N','VLAW32': '155.4825 N','FIRE21': '154.2800 N','FIRE22': '154.2650 N','FIRE23': '154.2950 N','FIRE24': '154.2725 N','FIRE25': '154.2875 N','FIRE26': '154.3025 N','COMPAC': '159.2850 N','VCAL10': '155.7525 N','VTAC11': '151.1375 N','VTAC12': '154.4525 N','VTAC13': '158.7375 N','VTAC14': '159.4725 N','VTAC33': '151.1375 N','VTAC34': '154.4525 N','VTAC35': '158.7375 N','VTAC36': '159.4725 N','VTAC37': '158.7375 N','VTAC38': '159.4725 N','MARS1': '148.0500 N','MARS2': '148.0250 N'}
TX_tone_dict = {'TXCALL1D': '156.7','VMED28': '156.7','VMED29': '156.7','VLAW31': '156.7','VLAW32': '156.7','FIRE21': '156.7','FIRE22': '156.7','FIRE23': '156.7','FIRE24': '156.7','FIRE25': '156.7','FIRE26': '156.7','COMPAC': '127.3','VCAL10': '156.7','VTAC11': '156.7','VTAC12': '156.7','VTAC13': '156.7','VTAC14': '156.7','VTAC33': '136.5','VTAC34': '136.5','VTAC35': '136.5','VTAC36': '136.5','VTAC37': '136.5','VTAC38': '136.5','MARS1': '123.0','MARS2': '123.0'}
data_dict = {'1 Incident Name_8': sys.argv[1],'2 Date/Time Prepared': datetime.now(),'Date From': sys.argv[3],'Date To': sys.argv[5],'Time From': sys.argv[4],'Time To': sys.argv[6],'Zone GrpRow1': '','Ch Row1': '','FunctionRow1': 'COMMAND','Channel NameTrunked Radio System TalkgroupRow1': sys.argv[7],'AssignmentRow1': 'OPS','RX Freq N or WRow1': RX_freq_dict[sys.argv[7]],'RX ToneNACRow1': RX_tone_dict[sys.argv[7]],'TX Freq N or WRow1': TX_freq_dict[sys.argv[7]],'TX ToneNACRow1': TX_tone_dict[sys.argv[7]],'Mode A D or MRow1': 'A','RemarksRow1': '','5 Special Instructions': 'This 205 will be superceeded by any on-site COML, any representitive of a Public Safety Agenecy, or Garrison Command.\n\nYou are secondary users of these channels, if interfearence is observed, cease using the channels and contact the COML for new channel assignments.\n\nBegin and end every transmission of substance with the words “This is an exercise”. Call Sign of “WQBC290” must be broadcast every 30 minutes while using the channel and at the end of use.','6 Prepared by Communications Unit Leader Name': 'Robert Johnson','Signature_9': '','IAP Page_4': '','DateTime_8': datetime.now()}

if len(sys.argv)>=9:
    data_dict['Zone GrpRow2'] = ''
    data_dict['Ch Row2'] = ''
    data_dict['FunctionRow2'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow2'] = sys.argv[8]
    data_dict['AssignmentRow2'] = 'OPS'
    data_dict['RX Freq N or WRow2'] = RX_freq_dict[sys.argv[8]]
    data_dict['RX ToneNACRow2'] = RX_tone_dict[sys.argv[8]]
    data_dict['TX Freq N or WRow2'] = TX_freq_dict[sys.argv[8]]
    data_dict['TX ToneNACRow2'] = TX_tone_dict[sys.argv[8]]
    data_dict['Mode A D or MRow2'] = 'A'
    data_dict['RemarksRow2'] = ''

if len(sys.argv)>=10:
    data_dict['Zone GrpRow3'] = ''
    data_dict['Ch Row3'] = ''
    data_dict['FunctionRow3'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow3'] = sys.argv[9]
    data_dict['AssignmentRow3'] = 'OPS'
    data_dict['RX Freq N or WRow3'] = RX_freq_dict[sys.argv[9]]
    data_dict['RX ToneNACRow3'] = RX_tone_dict[sys.argv[9]]
    data_dict['TX Freq N or WRow3'] = TX_freq_dict[sys.argv[9]]
    data_dict['TX ToneNACRow3'] = TX_tone_dict[sys.argv[9]]
    data_dict['Mode A D or MRow3'] = 'A'
    data_dict['RemarksRow3'] = ''

if len(sys.argv)>=11:
    data_dict['Zone GrpRow4'] = ''
    data_dict['Ch Row4'] = ''
    data_dict['FunctionRow4'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow4'] = sys.argv[10]
    data_dict['AssignmentRow4'] = 'OPS'
    data_dict['RX Freq N or WRow4'] = RX_freq_dict[sys.argv[10]]
    data_dict['RX ToneNACRow4'] = RX_tone_dict[sys.argv[10]]
    data_dict['TX Freq N or WRow4'] = TX_freq_dict[sys.argv[10]]
    data_dict['TX ToneNACRow4'] = TX_tone_dict[sys.argv[10]]
    data_dict['Mode A D or MRow4'] = 'A'
    data_dict['RemarksRow4'] = ''

if len(sys.argv)>=12:
    data_dict['Zone GrpRow5'] = ''
    data_dict['Ch Row5'] = ''
    data_dict['FunctionRow5'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow5'] = sys.argv[11]
    data_dict['AssignmentRow5'] = 'OPS'
    data_dict['RX Freq N or WRow5'] = RX_freq_dict[sys.argv[11]]
    data_dict['RX ToneNACRow5'] = RX_tone_dict[sys.argv[11]]
    data_dict['TX Freq N or WRow5'] = TX_freq_dict[sys.argv[11]]
    data_dict['TX ToneNACRow5'] = TX_tone_dict[sys.argv[11]]
    data_dict['Mode A D or MRow5'] = 'A'
    data_dict['RemarksRow5'] = ''

if len(sys.argv)>=13:
    data_dict['Zone GrpRow6'] = ''
    data_dict['Ch Row6'] = ''
    data_dict['FunctionRow6'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow6'] = sys.argv[12]
    data_dict['AssignmentRow6'] = 'OPS'
    data_dict['RX Freq N or WRow6'] = RX_freq_dict[sys.argv[12]]
    data_dict['RX ToneNACRow6'] = RX_tone_dict[sys.argv[12]]
    data_dict['TX Freq N or WRow6'] = TX_freq_dict[sys.argv[12]]
    data_dict['TX ToneNACRow6'] = TX_tone_dict[sys.argv[12]]
    data_dict['Mode A D or MRow6'] = 'A'
    data_dict['RemarksRow6'] = ''

if len(sys.argv)>=14:
    data_dict['Zone GrpRow7'] = ''
    data_dict['Ch Row7'] = ''
    data_dict['FunctionRow7'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow7'] = sys.argv[13]
    data_dict['AssignmentRow7'] = 'OPS'
    data_dict['RX Freq N or WRow7'] = RX_freq_dict[sys.argv[13]]
    data_dict['RX ToneNACRow7'] = RX_tone_dict[sys.argv[13]]
    data_dict['TX Freq N or WRow7'] = TX_freq_dict[sys.argv[13]]
    data_dict['TX ToneNACRow7'] = TX_tone_dict[sys.argv[13]]
    data_dict['Mode A D or MRow7'] = 'A'
    data_dict['RemarksRow7'] = ''

if len(sys.argv)>=15:
    data_dict['Zone GrpRow8'] = ''
    data_dict['Ch Row8'] = ''
    data_dict['FunctionRow8'] = 'TACTICAL'
    data_dict['Channel NameTrunked Radio System TalkgroupRow8'] = sys.argv[14]
    data_dict['AssignmentRow8'] = 'OPS'
    data_dict['RX Freq N or WRow8'] = RX_freq_dict[sys.argv[14]]
    data_dict['RX ToneNACRow8'] = RX_tone_dict[sys.argv[14]]
    data_dict['TX Freq N or WRow8'] = TX_freq_dict[sys.argv[14]]
    data_dict['TX ToneNACRow8'] = TX_tone_dict[sys.argv[14]]
    data_dict['Mode A D or MRow8'] = 'A'
    data_dict['RemarksRow8'] = ''

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'
 
pdf_template = "template.pdf"
pdf_output = sys.argv[2]+"/"+sys.argv[1]+".pdf"
template_pdf = pdfrw.PdfReader(pdf_template)

fill_pdf(pdf_template, pdf_output, data_dict)