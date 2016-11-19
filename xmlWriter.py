import lxml.etree as etree
from config import *
import os

class XmlWriter:
    root=None
    def __init__(self):
        if not os.path.exists('gocardless.xml'):
            XmlWriter.root=etree.Element(PROJECT_NAME)
        else:
            tree =etree.parse('gocardless.xml')
            XmlWriter.root= tree.getroot()

    @staticmethod
    def write(path_str):
        path_list = path_str.split("/")
        XmlWriter.add_to_elm(path_list, XmlWriter.root)
        XmlWriter.write_to_file()

    @staticmethod
    def get_child_or_create(parent, child_name):
        for ele in parent.iter():
            if ele.tag == child_name:
                return ele
        return etree.SubElement(parent, child_name)

    @staticmethod
    def sanitise_tag(tag):
        tag = tag.replace('@', '')
        tag = tag.replace(',', '')
        tag = tag.replace(';', '')
        tag = tag.replace('=', '')
        if tag[0].isdigit():
            tag = 'n' + tag
        return tag

    @staticmethod
    def add_to_elm(path_list, elm):
        tag=''
        while tag == '' and len(path_list) != 0:
            tag = path_list[0]
            path_list = path_list[1:]
        if tag == '':
            return
        xml_safe_tag = XmlWriter.sanitise_tag(tag)
        try:
            child = XmlWriter.get_child_or_create(elm, xml_safe_tag)
            XmlWriter.add_to_elm(path_list, child)
        except:
            print("Cannot add tag to tree: " + xml_safe_tag)

    @staticmethod
    def write_to_file():
        tree = etree.ElementTree(XmlWriter.root)
        tree.write(XmlWriter.root.tag + ".xml", pretty_print=True)
