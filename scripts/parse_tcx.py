import os
import xml.etree.ElementTree as ET

def is_running_activity(tcx_path):
    tree = ET.parse(tcx_path)
    root = tree.getroot()

    ns = {'tcx': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}

    activity = root.find('.//tcx:Activity', ns)
    if activity is None:
        return None
    
    sport = activity.attrib.get('Sport')
    if sport != "Running":
        return None # skips the non-running activities
    
    #Extraction of relevant info
    id_tag = activity.find('tcx:Id', ns)