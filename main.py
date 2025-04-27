#!/usr/bin/env python3

from xml.dom.minidom import parse, parseString, Document

# dom = parse('./Championnat.xml')
# print(dom)

# Step1: generate the base Employes.xml
doc = Document()

root = doc.createElement('Employes')
doc.appendChild(root)

employees = [
    ('E05', 'Kadri', 'Amina', '23-11-1995', 'S3'),
    ('E04', 'Abelmalk', 'Hakima', '18-10-1977', 'S3'),
    ('E01', 'Nouar', 'Mohamed', '08-04-1975', 'S1'),
    ('E02', 'Benali', 'Mostapha', '06-07-1965', 'S2'),
    ('E06', 'Safi', 'Mostapha', '23-12-1966', 'S4'),
    ('E03', 'Drissi', 'Oussama', '21-09-1956', 'S2'),
    ('E07', 'Nadji', 'Youssef', '31-12-1985', 'S4'),
]

# build each employee node
for mat, nom, prenom, date_n, service in employees:
    employe = doc.createElement('Employe')
    # print(doc.toprettyxml(indent='  '))
    # break

    mat_elem = doc.createElement('Mat')
    mat_elem.appendChild(doc.createTextNode(mat))

    nom_elem = doc.createElement('Nom')
    nom_elem.appendChild(doc.createTextNode(nom))

    prenom_elem = doc.createElement('Prenom')
    prenom_elem.appendChild(doc.createTextNode(prenom))

    date_n_elem = doc.createElement('Date_N')
    date_n_elem.appendChild(doc.createTextNode(date_n))

    service_elem = doc.createElement('Service')
    service_elem.appendChild(doc.createTextNode(service))

    employe.appendChild(mat_elem)
    employe.appendChild(nom_elem)
    employe.appendChild(prenom_elem)
    employe.appendChild(date_n_elem)
    employe.appendChild(service_elem)

    root.appendChild(employe)

#!/usr/bin/env python3

from xml.dom.minidom import parse, parseString, Document

# dom = parse('./Championnat.xml')
# print(dom)

# Step1: generate the base Employes.xml
doc = Document()

root = doc.createElement('Employes')
doc.appendChild(root)

employees = [
    ('E05', 'Kadri', 'Amina', '23-11-1995', 'S3'),
    ('E04', 'Abelmalk', 'Hakima', '18-10-1977', 'S3'),
    ('E01', 'Nouar', 'Mohamed', '08-04-1975', 'S1'),
    ('E02', 'Benali', 'Mostapha', '06-07-1965', 'S2'),
    ('E06', 'Safi', 'Mostapha', '23-12-1966', 'S4'),
    ('E03', 'Drissi', 'Oussama', '21-09-1956', 'S2'),
    ('E07', 'Nadji', 'Youssef', '31-12-1985', 'S4'),
]

# build each employee node
for mat, nom, prenom, date_n, service in employees:
    employe = doc.createElement('Employe')
    # print(doc.toprettyxml(indent='  '))
    # break

    mat_elem = doc.createElement('Mat')
    mat_elem.appendChild(doc.createTextNode(mat))

    nom_elem = doc.createElement('Nom')
    nom_elem.appendChild(doc.createTextNode(nom))

    prenom_elem = doc.createElement('Prenom')
    prenom_elem.appendChild(doc.createTextNode(prenom))

    date_n_elem = doc.createElement('Date_N')
    date_n_elem.appendChild(doc.createTextNode(date_n))

    service_elem = doc.createElement('Service')
    service_elem.appendChild(doc.createTextNode(service))

    employe.appendChild(mat_elem)
    employe.appendChild(nom_elem)
    employe.appendChild(prenom_elem)
    employe.appendChild(date_n_elem)
    employe.appendChild(service_elem)

    root.appendChild(employe)


# with open('./results/Employes.xml', 'w', encoding='utf-8') as f:
#     f.write(doc.toprettyxml(indent='    '))


