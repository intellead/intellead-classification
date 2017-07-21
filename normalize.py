def lead(data):
    role = job_title(data['lead']['job_title'])
    profile = lead_profile(data['lead']['fit_score'])
    conversion = int(data['lead']['number_conversions'])
    lead_area = area(data['lead']['custom_fields']['Área'])
    number_of_employees = number_of_employees_in_office(data['lead']['custom_fields']['Quantos funcionários há na sua empresa nas áreas de Engenharia, Compras, Financeiro, Administrativo e Comercial?'])
    company_segment = segment(data['lead']['custom_fields']['Segmento'])
    wip = works_in_progress(data['lead']['custom_fields']['Sua empresa tem obras em andamento?'])
    source_first_conv = source_of_first_convertion(data['lead']['first_conversion']['conversion_origin']['source'])
    source_last_conv = source_of_last_convertion(data['lead']['last_conversion']['conversion_origin']['source'])
    concern = biggest_concern(data['lead']['custom_fields']['Qual sua maior preocupação hoje?'])
    business_manage = business_management(data['lead']['custom_fields']['Como sua empresa é gerenciada?'])
    lack_mat = lack_material(data['lead']['custom_fields']['Costuma faltar material nas suas obras?'])
    decision = decision_made(data['lead']['custom_fields']['Como as decisões são tomadas?'])
    difficulties = area_difficulties(data['lead']['custom_fields']['Qual área da sua empresa tem mais dificuldades?'])
    efficient = efficient_processes(data['lead']['custom_fields']['Sua empresa tem processos eficientes?'])
    impact_of_a_rain = impact_of_a_rainy_week(data['lead']['custom_fields']['Qual o impacto de uma semana de chuva em sua obra?'])
    consultant_contact = receive_consultant_contact(data['lead']['custom_fields']['Sim, eu gostaria de receber um contato do consultor para avaliação do software'])
    interested_in_tool = interested_in_hiring_management_tool(data['lead']['last_conversion']['content']['Tem interesse em contratar ferramenta de gestão?'])
    looking_for_a_software = looking_for_a_management_software(data['lead']['last_conversion']['content']['Estou a procura de um software de gestão para minha empresa!'])
    normalized_data = (role, profile, conversion, lead_area, number_of_employees, company_segment, wip, source_first_conv, source_last_conv, concern, business_manage, lack_mat, decision, difficulties, efficient, impact_of_a_rain, consultant_contact, interested_in_tool, looking_for_a_software)
    return normalized_data


def job_title(data):
    if data is None | data == '':
        return 0
    elif data == 'Sócio/Proprietário':
        return 1
    elif data == 'ADM' | data == 'adm':
        return 2
    elif data == 'Aluno' | data == 'Estudante':
        return 3
    elif data == 'TI' | data == 'ti':
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
    elif data == 'Outros':
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
    if data is None | data == '':
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
    elif data == 'RH' | data == 'rh':
        return 9
    elif data == 'TI' | data == 'ti':
        return 10
    elif data == 'Suprimentos':
        return 11
    elif data == 'Outros' | data == 'outros':
        return 12
    elif data == 'Contabilidade':
        return 13


def number_of_employees_in_office(data):
    if data is None | data == '':
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


def segment(data):
    if data is None | data == '':
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
    if data is None | data == '':
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
    if data is None | data == '' | data == 'Desconhecido':
        return 0
    elif data.find('Orgânica') != -1:
        return 1
    elif data.find('Paga') != -1:
        return 2
    elif data.find('Email') != -1:
        return 3
    elif data.find('Outros') != -1:
        return 4
    elif data.find('Referência') != -1:
        return 5
    elif data.find('Social | Facebook') != -1:
        return 6
    elif data.find('Social') != -1:
        return 7
    elif data == 'Tráfego Direto':
        return 8


def source_of_last_convertion(data):
    if data is None | data == '' | data == 'Desconhecido':
        return 0
    elif data.find('Orgânica') != -1:
        return 1
    elif data.find('Paga') != -1:
        return 2
    elif data.find('Email') != -1:
        return 3
    elif data.find('Outros') != -1:
        return 4
    elif data.find('Referência') != -1:
        return 5
    elif data.find('Social | Facebook') != -1:
        return 6
    elif data.find('Social') != -1:
        return 7
    elif data == 'Tráfego Direto':
        return 8


def biggest_concern(data):
    if data is None | data == '':
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
    if data is None | data == '':
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
    if data is None | data == '':
        return 0
    elif data == 'De vez em quando falta':
        return 1
    elif data == 'É raro faltar algo':
        return 2
    elif data == 'Sim, o tempo todo':
        return 3


def decision_made(data):
    if data is None | data == '':
        return 0
    elif data == 'Eu mesmo decido':
        return 1
    elif data == 'Meu gestor decide':
        return 2
    elif data == 'É complicado, passa por muita gente':
        return 3


def area_difficulties(data):
    if data is None | data == '':
        return 0
    elif data == 'Financeiro':
        return 1
    elif data == 'Engenharia':
        return 2
    elif data == 'RH' | data == 'rh':
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
    if data is None | data == '':
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def impact_of_a_rainy_week(data):
    if data is None | data == '':
        return 0
    elif data == 'Grande, esses imprevistos atrasam a entrega':
        return 1
    elif data == 'Pequeno, planejamos atividades para que a equipe não fique parada':
        return 2


def receive_consultant_contact(data):
    if data is None | data == '':
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def interested_in_hiring_management_tool(data):
    if data is None | data == '':
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1


def looking_for_a_management_software(data):
    if data is None | data == '':
        return 9
    elif data == 'Não':
        return 0
    elif data == 'Sim':
        return 1
