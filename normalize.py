def lead(data):
    role = job_title(data['lead']['job_title'])
    profile = lead_profile(data['lead']['fit_score'])
    conversion = int(data['lead']['number_conversions'])
    lead_area = area(data['lead']['custom_fields']['Área'])
    number_of_employees = 0
    if data['lead']['custom_fields'].get(('Quantos funcionários há na sua empresa nas áreas de Engenharia, Compras, Financeiro, Administrativo e Comercial?'), 0) != 0:
        number_of_employees = number_of_employees_in_office(data['lead']['custom_fields']['Quantos funcionários há na sua empresa nas áreas de Engenharia, Compras, Financeiro, Administrativo e Comercial?'])
    company_segment = segment(data['lead']['custom_fields']['Segmento'])
    wip = 0
    if data['lead']['custom_fields'].get(('Sua empresa tem obras em andamento?'), 0) != 0:
        wip = works_in_progress(data['lead']['custom_fields']['Sua empresa tem obras em andamento?'])
    source_first_conv = source_of_first_convertion(data['lead']['first_conversion']['conversion_origin']['source'])
    source_last_conv = source_of_last_convertion(data['lead']['last_conversion']['conversion_origin']['source'])
    concern = 0
    if data['lead']['custom_fields'].get(('Qual sua maior preocupação hoje?'), 0) != 0:
        concern = biggest_concern(data['lead']['custom_fields']['Qual sua maior preocupação hoje?'])
    looking_for_a_software = 0
    if data['lead']['custom_fields'].get(('Estou a procura de um software de gestão para minha empresa!'), 0) != 0:
        looking_for_a_software = looking_for_a_management_software(data['lead']['last_conversion']['content']['Estou a procura de um software de gestão para minha empresa!'])
    main_activity = None
    if data['lead'].get('main_activity_code') != None:
        main_activity = cnae(data['lead'].get('main_activity_code'))

    if main_activity != None:
        normalized_data = (role, profile, conversion, lead_area, number_of_employees, company_segment, wip, source_first_conv, source_last_conv, concern, looking_for_a_software, main_activity)
    else:
        normalized_data = (role, profile, conversion, lead_area, number_of_employees, company_segment, wip, source_first_conv, source_last_conv, concern, looking_for_a_software)
    return normalized_data


def job_title(data):
    if (data is None) | (data == '') | (data == 'unknow'):
        return 0
    elif data == 'Sócio/Proprietário':
        return 1
    elif (data == 'ADM') | (data == 'adm'):
        return 2
    elif (data == 'Aluno') | (data == 'Estudante'):
        return 3
    elif (data == 'TI') | (data == 'ti'):
        return 4
    elif data == 'Analista':
        return 5
    elif data == 'Assistente':
        return 6
    elif data == 'Autônomo':
        return 7
    elif data == 'Consultor':
        return 8
    elif data == 'Coordenador de obras':
        return 9
    elif data == 'Diretor':
        return 10
    elif data == 'Engeenheiro e proprietário':
        return 11
    elif data == 'Departamento financeiro':
        return 12
    elif data == 'Estagiário':
        return 13
    elif data == 'Gerente administrativo':
        return 14
    elif data == 'Gerente financeiro':
        return 15
    elif data == 'Gerente geral':
        return 16
    elif data == 'Gestor de área':
        return 17
    elif data == 'Gerente de planejamento':
        return 18
    elif (data == 'Outros') | (data == 'outros'):
        return 19
    elif data == 'Proprietário':
        return 20
    elif data == 'Sócio':
        return 21
    elif data == 'Sócio financeiro e administrativo':
        return 22


def lead_profile(data):
    if data == 'a':
        return 1
    elif data == 'b':
        return 2
    elif data == 'c':
        return 3
    elif data == 'd':
        return 4


def area(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Arquiterura':
        return 1
    elif data == 'Comercial':
        return 2
    elif data == 'Diretoria':
        return 3
    elif data == 'Engenharia':
        return 4
    elif data == 'Financeiro e Administrativo':
        return 5
    elif data == 'Incorporação':
        return 6
    elif data == 'Orçamento':
        return 7
    elif data == 'Planejamento':
        return 8
    elif (data == 'RH') | (data == 'rh'):
        return 9
    elif (data == 'TI') | (data == 'ti'):
        return 10
    elif data == 'Suprimentos':
        return 11
    elif (data == 'Outros') | (data == 'outros'):
        return 12
    elif data == 'Contabilidade':
        return 13


def number_of_employees_in_office(data):
    if (data is None) | (data == ''):
        return 0
    elif data == '0 a 4':
        return 1
    elif data == '5 a 9':
        return 2
    elif data == '10 a 19':
        return 3
    elif data == '20 a 29':
        return 4
    elif data == '30 a 49':
        return 5
    elif data == '50 a 99':
        return 6
    elif data == '100 a 249':
        return 7
    elif data == '250 a 499':
        return 8
    elif data == '500 ou mais':
        return 9


def segment(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Construtora':
        return 1
    elif data == 'Construtora e Incorporadora':
        return 2
    elif data == 'Incorporadora':
        return 3
    elif data == 'Instaladora':
        return 4
    elif data == 'Loteadora':
        return 5
    elif data == 'Obras Próprias':
        return 6
    elif data == 'Reformas':
        return 7
    elif data == 'Serviços':
        return 8
    elif data == 'Serviços Especiais':
        return 9
    elif data == 'Outros':
        return 10


def works_in_progress(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Não, nenhuma':
        return 1
    elif data == 'Sim, pequenas reformas':
        return 2
    elif data == 'Sim, até 3 obras':
        return 3
    elif data == 'Sim, de 4 a 10 obras':
        return 4
    elif data == 'Sim, mais de 11 obras':
        return 5


def source_of_first_convertion(data):
    if (data is None) | (data == '') | (data == 'Desconhecido') | (data == 'unknown'):
        return 0
    elif (data.find('Orgânica') != -1) | (data == 'Google') | (data == 'google'):
        return 1
    elif data.find('Paga') != -1:
        return 2
    elif data.find('Email') != -1:
        return 3
    elif data.find('Outros') != -1:
        return 4
    elif data.find('Referência') != -1:
        return 5
    elif (data.find('Social | Facebook') != -1) | (data.find('Facebook Ads') != -1) | (data == 'Facebook-Ads') | (data == 'Facebook-ads'):
        return 6
    elif data.find('Social') != -1:
        return 7
    elif (data == 'Tráfego Direto') | (data.find('direct') != -1):
        return 8


def source_of_last_convertion(data):
    if (data is None) | (data == '') | (data == 'Desconhecido') | (data == 'unknown'):
        return 0
    elif (data.find('Orgânica') != -1) | (data == 'Google') | (data == 'google'):
        return 1
    elif data.find('Paga') != -1:
        return 2
    elif data.find('Email') != -1:
        return 3
    elif data.find('Outros') != -1:
        return 4
    elif data.find('Referência') != -1:
        return 5
    elif (data.find('Social | Facebook') != -1) | (data.find('Facebook Ads') != -1) | (data == 'Facebook-Ads') | (data == 'Facebook-ads'):
        return 6
    elif data.find('Social') != -1:
        return 7
    elif (data == 'Tráfego Direto') | (data.find('direct') != -1):
        return 8


def biggest_concern(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Vender mais':
        return 1
    elif data == 'Conseguir crédito para a empresa':
        return 2
    elif data == 'Reduzir custos':
        return 3
    elif data == 'Organizar a empresa para poder crescer':
        return 4
    elif data == 'Saber onde perco dinheiro':
        return 5


def business_management(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Eu tenho o que preciso na cabeça mesmo':
        return 1
    elif data == 'Usamos um software integrado':
        return 2
    elif data == 'Usamos vários softwares específicos':
        return 3
    elif data == 'Usamos planilhas':
        return 4


def lack_material(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'De vez em quando falta':
        return 1
    elif data == 'É raro faltar algo':
        return 2
    elif data == 'Sim, o tempo todo':
        return 3


def decision_made(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Eu mesmo decido':
        return 1
    elif data == 'Meu gestor decide':
        return 2
    elif data == 'É complicado, passa por muita gente':
        return 3


def area_difficulties(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Financeiro':
        return 1
    elif data == 'Engenharia':
        return 2
    elif (data == 'RH') | (data == 'rh'):
        return 3
    elif data == 'Contabilidade':
        return 4
    elif data == 'Compras':
        return 5
    elif data == 'Vendas':
        return 6
    elif data == 'Obras':
        return 7


def efficient_processes(data):
    if (data is None) | (data == ''):
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def impact_of_a_rainy_week(data):
    if (data is None) | (data == ''):
        return 0
    elif data == 'Grande, esses imprevistos atrasam a entrega':
        return 1
    elif data == 'Pequeno, planejamos atividades para que a equipe não fique parada':
        return 2


def receive_consultant_contact(data):
    if (data is None) | (data == ''):
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def interested_in_hiring_management_tool(data):
    if (data is None) | (data == ''):
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def looking_for_a_management_software(data):
    if (data is None) | (data == ''):
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def cnae(data):
    if (data is None) | (data == ''):
        return 0
    elif data == '43.99-1-99':
        return 1
    elif data == '74.90-1-99':
        return 2
    elif data == '43.30-4-01':
        return 3
    elif data == '42.13-8-00':
        return 4
    elif data == '69.20-6-01':
        return 5
    elif data == '82.19-9-99':
        return 6
    elif data == '68.21-8-01':
        return 7
    elif data == '42.21-9-02':
        return 8
    elif data == '68.22-6-00':
        return 9
    elif data == '68.10-2-02':
        return 10
    elif data == '42.92-8-02':
        return 11
    elif data == '71.19-7-03':
        return 12
    elif data == '43.30-4-04':
        return 13
    elif data == '42.22-7-01':
        return 14
    elif data == '42.99-5-01':
        return 15
    elif data == '23.30-3-01':
        return 16
    elif data == '42.21-9-03':
        return 17
    elif data == '25.11-0-00':
        return 18
    elif data == '68.10-2-03':
        return 19
    elif data == '43.13-4-00':
        return 20
    elif data == '68.10-2-01':
        return 21
    elif data == '43.21-5-00':
        return 22
    elif data == '43.30-4-99':
        return 23
    elif data == '71.11-1-00':
        return 24
    elif data == '42.99-5-99':
        return 25
    elif data == '43.99-1-01':
        return 26
    elif data == '43.99-1-03':
        return 27
    elif data == '42.11-1-01':
        return 28
    elif data == '71.12-0-00':
        return 29
    elif data == '41.10-7-00':
        return 30
    elif data == '41.20-4-00':
        return 31
    else:
        return 999

