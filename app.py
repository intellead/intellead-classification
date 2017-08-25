# -*- coding: utf-8 -*-
import requests
import json
from flask import Flask, abort, request

import normalize
import service

app = Flask(__name__)


test_2 = {
	'leads': [{
		'email': 'andreza.geovana@hotmail.com',
		'name': 'Andreza',
		'company': 'Elitim',
		'job_title': 'Assistente',
		'bio': None,
		'public_url': 'http://rdstation.com.br/leads/public/5a0aa3fe-9fda-461e-ab75-1350c31fb4c4',
		'created_at': '2010-01-01T00:00:00.000-02:00',
		'opportunity': 'false',
		'number_conversions': '38',
		'user': None,
		'first_conversion': {
			'content': {
				'email_lead': 'andreza.geovana@hotmail.com',
				'tags': 'PlanilhasXERP - A',
				'created_at': '2010-01-01T02:00:00.000Z',
				'identificador': 'Planilhas_x_ERP_-_Base',
				'company_id': None,
				'import_token': 'b91e6b31-a42e-4187-8b9f-7821dd27a846'
			},
			'created_at': '2010-01-01T00:00:00.000-02:00',
			'cumulative_sum': '1',
			'source': 'Planilhas_x_ERP_-_Base',
			'conversion_origin': {
				'source': 'unknown',
				'medium': 'unknown',
				'value': None,
				'campaign': 'unknown',
				'channel': 'Unknown'
			}
		},
		'last_conversion': {
			'content': {
				'identificador': '/palestra-terceirizacao-impactos-nas-empresas-da-construcao/',
				'nome': 'Andreza',
				'empresa': 'Elitim',
				'cargo': 'Assistente',
				'telefone': '(84) 9878-44161',
				'Quer receber novidades': None,
				'Empresa usa o Sienge?': 'Não',
				'Tem interesse em contratar ferramenta de gestão?': None,
				'Porque se interessou pela palestra?': None,
				'Qual é o principal desafio da sua empresa neste ano?': None,
				'Usa o Sienge?': None,
				'Como soube da Palestra': None,
				'Empresa que Trabalha': None,
				'Segmento': 'Construtora e Incorporadora',
				'Área': 'Outros',
				'Sua empresa tem obras em andamento?': None,
				'Qual sua maior preocupação hoje?': None,
				'Como sua empresa é gerenciada?': None,
				'O que sua empresa precisa?': None,
				'Como as decisões são tomadas?': None,
				'Costuma faltar material nas suas obras?': None,
				'Você já ouviu falar do Sienge?': None,
				'Qual área da sua empresa tem mais dificuldades?': None,
				'Qual o impacto de uma semana de chuva em sua obra?': None,
				'Sua empresa tem processos eficientes?': None,
				'Possui verba para investir em software?': None,
				'Sua obra possui acesso à internet?': None,
				'Quantos funcionários há na sua empresa nas áreas de Engenharia, Compras, Financeiro, Administrativo e Comercial?': None,
				'Alguma empresa indicou o Sienge para você?': None,
				'Qual o problema você está tentando resolver na sua empresa?': None,
				'Estado': None,
				'Estado_Adicional': None,
				'Cidade': None,
				'Gostaria de receber um contato do consultor para avaliação da ferramenta?': None,
				'Sim, eu gostaria de receber um contato do consultor para avaliação do software': 'Não',
				'Quero uma demonstração de um software de gestão para minha empresa!': None,
				'Quero uma demonstração de um software de gestão para minha empresa! - Palestras': None,
				'Quero uma demonstração de um software de gestão para minha empresa! - Planilhas e Ebooks': None,
				'Condição de Pagamento': None,
				'Estou a procura de um software de gestão para minha empresa!': None,
				'Pop up Demonstração': None,
				'Cargo_complemento': None,
				'Segmento_complemento': None,
				'Area_complemento': None,
				'¿Cuáles son tus mayores preocupaciones relacionadas con la empresa? ': None,
				'¿Cómo funciona la gestión de su empresa?': None,
				'Ahora ¿cuáles son sus mayores dificultades con su herramienta de gestión?': None,
				'Falar com': '',
				'Mensagem': None,
				'Campaign_Source': '',
				'Campaign_Name': '',
				'Campaign_Medium': '',
				'Campaign_Term': '',
				'Campaign_Content': '',
				'Frist_Visit': '',
				'Previous_Visit': '',
				'Current_visit_started': '',
				'Times_visited': '',
				'Pages_Viewed': '',
				'traffic_source': 'encoded_eyJmaXJzdF9zZXNzaW9uIjp7InZhbHVlIjoiMjI5MzcwNTI2LjE0OTg2OTY3NzYuMS4xLnV0bWNzcj1FbWFpbC1BY2FvfHV0bWNjbj1kb3NlLW1lbnNhbC1DRC0yOC0wN3x1dG1jbWQ9ZW1haWwiLCJleHRyYV9wYXJhbXMiOnt9fSwiY3VycmVudF9zZXNzaW9uIjp7InZhbHVlIjoiMjI5MzcwNTI2LjE0OTg2OTY3NzYuMS4xLnV0bWNzcj1FbWFpbC1BY2FvfHV0bWNjbj1kb3NlLW1lbnNhbC1DRC0yOC0wN3x1dG1jbWQ9ZW1haWwiLCJleHRyYV9wYXJhbXMiOnt9fSwiY3JlYXRlZF9hdCI6MTQ5ODY5Njc3NzMzN30=',
				'created_at': '2017-06-29 00:40:40 UTC',
				'email_lead': 'andreza.geovana@hotmail.com'
			},
			'created_at': '2017-06-28T21:40:40.000-03:00',
			'cumulative_sum': '38',
			'source': '/palestra-terceirizacao-impactos-nas-empresas-da-construcao/',
			'conversion_origin': {
				'source': 'Email-Acao',
				'medium': 'email',
				'value': None,
				'campaign': 'dose-mensal-CD-28-07',
				'channel': 'Email'
			}
		},
		'custom_fields': {
			'Campaign_Source': 'Email-Acao',
			'Campaign_Medium': 'email',
			'Frist_Visit': '05 Apr 2017 - 22:53',
			'Previous_Visit': '08 Apr 2017 - 23:54',
			'Current_visit_started': '27 Apr 2017 - 22:57',
			'Times_visited': '15',
			'Pages_Viewed': '5',
			'Campaign_Name': 'dose-mensal-04-17',
			'c_utmz': '229370526.1491706454.13.10.utmcsr=Email-Fluxo|utmccn=ME-A-agradecimento-whitepaper-passo-a-passo-da-construcao-civil|utmcmd=email',
			'Quer receber novidades': 'Sim',
			'Empresa usa o Sienge?': 'Não',
			'Segmento': 'Construtora e Incorporadora',
			'Área': 'Outros',
			'Sim, eu gostaria de receber um contato do consultor para avaliação do software': 'Não',
			'Estou a procura de um software de gestão para minha empresa!': 'Não',
			'Qual sua maior preocupação hoje?': 'Reduzir custos',
			'Como sua empresa é gerenciada?': 'Usamos planilhas',
			'Costuma faltar material nas suas obras?': 'De vez em quando falta',
			'Qual o impacto de uma semana de chuva em sua obra?': 'Pequeno, planejamos atividades para que a equipe não fique parada',
			'Sua empresa tem obras em andamento?': 'Sim, até 3 obras',
			'Como as decisões são tomadas?': 'Meu gestor decide',
			'Você já ouviu falar do Sienge?': 'Sim',
			'Qual área da sua empresa tem mais dificuldades?': 'Obras',
			'Sua empresa tem processos eficientes?': 'Não',
			'Sua obra possui acesso à internet?': 'Rede Fixa (Cabo, Rádio, Wifi)',
			'Possui verba para investir em software?': 'Não',
			'Quantos funcionários há na sua empresa nas áreas de Engenharia, Compras, Financeiro, Administrativo e Comercial?': '10 a 19',
			'Alguma empresa indicou o Sienge para você?': 'Não'
		},
		'website': None,
		'personal_phone': '(84) 9878-44161',
		'mobile_phone': None,
		'city': None,
		'state': None,
		'tags': ['planilhasxerp - a'],
		'lead_stage': 'Lead',
		'last_marked_opportunity_date': None,
		'uuid': '5a0aa3fe-9fda-461e-ab75-1350c31fb4c4',
		'fit_score': 'c',
		'interest': 12,
		'_id': '151680927',
		'enrichByReceitaWS': 1,
		'cnpj': '13.926.863/0001-36',
		'main_activity_name': 'Construção de edifícios',
		'main_activity_code': '41.20-4-00',
		'company_situation': 'ATIVA',
		'company_social_capital': '500000.00',
		'company_telephone': '(48) 3348-0406',
		'company_type': 'MATRIZ',
		'company_opening_date': '01/07/2011',
		'company_name': 'ELITIM CONSTRUCAO E INCORPORACAO LTDA',
		'company_fantasy_name': 'ELITIM CONSTRUTORA E ELITIM CONSTRUTORA E INCORPORADORA',
		'company_uf': 'SC',
		'company_neighborhood': 'ESTREITO',
		'company_street': 'R SOUZA DUTRA',
		'company_adress_number': '145',
		'company_zip_code': '88.070-605',
		'company_city': 'FLORIANOPOLIS',
		'company_board_members': [{
			'qual': '05-Administrador',
			'nome': 'LUIZ FELIPE VIEIRA SCHMIDT'
		}, {
			'qual': '22-Sócio',
			'qual_rep_legal': '05-Administrador',
			'nome_rep_legal': 'LUIZ FELIPE VIEIRA SCHMIDT',
			'nome': 'BRACO INVESTIMENTOS E PARTICIPACOES LTDA'
		}, {
			'qual': '05-Administrador',
			'nome': 'THIERRY JULES CHATELAN'
		}, {
			'qual': '49-Sócio-Administrador',
			'nome': 'CARLOS ALBERTO PRUDENCIO DE SOUZA'
		}],
		'lead_status': 1
	}]
}


@app.route('/')
def index():
    return "Intellead Classification"


@app.route('/lead_status_by_id/<int:lead_id>', methods=['GET'])
def get_lead_status_by_id(lead_id):
    json_lead = get_data_from_lead(lead_id)
    if (json_lead is None) | (json_lead == ''):
        abort(404)
    normalized_data = normalize.lead(json_lead)
    lead_status = service.classification(normalized_data)
    save_lead_status(lead_id, lead_status)
    if lead_status == 1:
        json_lead['lead']['lead_status'] = lead_status
        send_data_to_connector(json_lead['lead'])
        print('connected')
    return str(lead_status)


def get_data_from_lead(lead_id):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    url = 'https://intellead-data.herokuapp.com/lead-info'
    data = {"lead_id": str(lead_id)}
    response = requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_lead_status(lead_id, lead_status):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    url = 'https://intellead-data.herokuapp.com/save-lead-status'
    data = {"lead_id": str(lead_id), "lead_status": int(lead_status)}
    requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    print('lead has been sended to intellead-data')


def send_data_to_connector(data):
    print(data['email'] + ' connecting... to intellead-connector')
    leads = {}
    leads['leads'] = [data]
    print(leads)
    print(test_2)
    print(type(leads))
    print(type(test_2))
    url = 'https://intellead-connector.herokuapp.com/teste'
    r = requests.post(url, json=leads)
    print(r.status_code)



if __name__ == '__main__':
    app.run(debug=True)




