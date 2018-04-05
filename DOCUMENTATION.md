# Welcome to Intellead Classification documentation!

Intellead Classification aims to be an easy way to identify the qualified lead for Intellead project.

## Contents
  * Introduction
    * Features
  * Instalation
    * Dependencies
    * Get a copy
  * Configuration
  * Dataset
    * Dataset information
    * Attribute information
  * Use Cases
    * Lead status [/lead_status_by_id]
  * Copyrights and Licence

## Introduction
Intellead Classification aims to be an easy way to identify the qualified lead for Intellead ecosystem.

#### Features
This application provides lead status.
  * 0 - Not qualified
  * 1 - Qualified

## Instalation
intellead-classification is a very smaller component that provide a simple way to classify lead.
This way you do not need to install any other components for this to work.

#### Dependencies
Despite what has been said above, intellead-classification depends on intellead-data to retrieval information from lead and to store the identified lead status.
In addition, all libraries required by the service are described in requirements.txt document.

#### Get a copy
I like to encourage you to contribute to the repository.
This should be as easy as possible for you but there are few things to consider when contributing. The following guidelines for contribution should be followed if you want to submit a pull request.
  * You need a GitHub account.
  * Submit an issue ticket for your issue if there is no one yet.
  * If you are able and want to fix this, fork the repository on GitHub.
  * Make commits of logical units and describe them properly.
  * If possible, submit tests to your patch / new feature so it can be tested easily.
  * Assure nothing is broken by running all the tests.
  * Open a pull request to the original repository and choose the right original branch you want to patch.
  * Even if you have write access to the repository, do not directly push or merge pull-requests. Let another team member review your pull request and approve.

## Configuration
Once the application is installed (check Installation) define the following settings to enable the application behavior.

#### Config vars
The application uses a postgres database to store the dataset.
For this it is necessary to configure the connection variables.
You must config the following vars:
  * SECURITY_URL - Full URL to intellead-security auth endpoint (`http://intellead-security/auth`);
  * DATABASE_HOST - Host from database;
  * DATABASE_PORT - The port where database is connected;
  * DATABASE_NAME - Database name;
  * DATABASE_USER - User account to connect to the database;
  * DATABASE_PASSWORD - Password to connect to the database;
  * DATA_LEAD_INFO_URL - Full URL of Lead Info API from Data Service;
  * DATA_SAVE_LEAD_STATUS_URL - Full URL of Save Lead Status API from Data Service;
  * NORMALIZATION_URL - Full URL of normalize endpoint from Normalization Service;
  * CONNECTOR_CLASSIFICATION_WEBHOOK - Full URL of Classification Webhook API from Connector Service.

## Dataset
This dataset contains leads from construction industry.

#### Dataset information
  * Data Set Characteristics: Multivariate
  * Number of Instances: 595
  * Attribute Characteristics: Integer
  * Number of Attributes: 16
  * Associated Tasks: Classification
  * Missing Values?: No

#### Attribute information
1. Company name (string)<br>
2. E-mail of the lead (string)  <br>
3. Name of the lead (string)<br>
4. Job title of the lead in company (numerical)<br>
-- 0 = unknow<br>
-- 1 = owner/partner<br>
-- 2 = adm<br>
-- 3 = student<br>
-- 4 = it (information technology)<br>
-- 5 = analist<br>
-- 6 = assistant<br>
-- 7 = independent<br>
-- 8 = consultant<br>
-- 9 = construction coordinator<br>
-- 10 = director<br>
-- 11 = engineer and owner<br>
-- 12 = finance department<br>
-- 13 = intern<br>
-- 14 = administrative manager<br>
-- 15 = financial manager <br>
-- 16 = general manager<br>
-- 17 = area manager<br>
-- 18 = planning manager<br>
-- 19 = others<br>
-- 20 = owner<br>
-- 21 = partner<br>
-- 22 = financial and administrative partner<br>
5. Lead profile (numerical)<br>
-- 1 = a<br>
-- 2 = b<br>
-- 3 = c<br>
-- 4 = d<br>
6. Number of conversion (numerical)<br>
7. Area(numerical)<br>
-- 0 = unknow<br>
-- 1 = architecture<br>
-- 2 = commercial<br>
-- 3 = directorship<br>
-- 4 = engineering<br>
-- 5 = financial and administrative<br>
-- 6 = incorporation<br>
-- 7 = budget<br>
-- 8 = planning<br>
-- 9 = hr (human resources)<br>
-- 10 = it (information technology<br>
-- 11 = supplies<br>
-- 12 = others<br>
-- 13 = accounting<br>
8. Number of employees in areas of engineering, purchasing, financial, administrative and commercial (numerical)<br>
-- 0 = unknow<br>
-- 1 = 0 to 4<br>
-- 2 = 5 to 9<br>
-- 3 = 10 to 19<br>
-- 4 = 20 to 29<br>
-- 5 = 30 to 49<br>
-- 6 = 50 to 99<br>
-- 7 = 100 to 249<br>
-- 8 = 250 to 499<br>
-- 9 = more than 500<br>
9. Segment (numerical)<br>
-- 0 = unknow<br>
-- 1 = construction company<br>
-- 2 = builder and incorporator<br>
-- 3 = incorporator<br>
-- 4 = installer<br>
-- 5 = allotment<br>
-- 6 = own works<br>
-- 7 = reforms<br>
-- 8 = services<br>
-- 9 = special services<br>
-- 10 = others<br>
10. Number of works in progress (numerical)<br>
-- 0 = unknow<br>
-- 1 = none<br>
-- 2 = small reforms<br>
-- 3 = up to 3 works<br>
-- 4 = 4 to 10 works<br>
-- 5 = more than 11 works<br>
11. Source of the first conversion (numerical)<br>
-- 0 = unknow<br>
-- 1 = organic search<br>
-- 2 = paid search<br>
-- 3 = email<br>
-- 4 = others<br>
-- 5 = reference<br>
-- 6 = social/facebook<br>
-- 7 = social<br>
-- 8 = direct traffic<br>
12. Source of the last conversion (numerical)<br>
-- 0 = unknow<br>
-- 1 = organic search<br>
-- 2 = paid search<br>
-- 3 = email<br>
-- 4 = others<br>
-- 5 = reference<br>
-- 6 = social/facebook<br>
-- 7 = social<br>
-- 8 = direct traffic<br>
13. What is your biggest concern today? (numerical)<br>
-- 0 = unknow<br>
-- 1 = sell more<br>
-- 2 = get credit for the company<br>
-- 3 = reduce costs<br>
-- 4 = organize the company to grow<br>
-- 5 = know where I lose money<br>
14. I am looking for a management software for my company!<br>
-- 0 = no<br>
-- 1 = yes<br>
-- 9 = unknow<br>
15. Cnae (numerical)<br>
-- 0 = unknow<br>
-- 1 = 43.99-1-99 - Serviços especializados para construção não especificados anteriormente<br>
-- 2 = 74.90-1-99 - Outras atividades profissionais, cientificas e técnicas não especificadas anteriormente<br>
-- 3 = 43.30-4-01 - Impermeabilização em obras de engenharia civil<br>
-- 4 = 42.13-8-00 - Obras de urbanização - ruas, praças e calçadas<br>
-- 5 = 69.20-6-01 - Atividades de contabilidade<br>
-- 6 = 82.19-9-99 - Preparação de Documentos e Serviços Especializados de Apoio Administrativo Não Especificados Anteriormente<br>
-- 7 = 68.21-8-01 - Corretagem na compra e venda e avaliação de imóveis<br>
-- 8 = 42.21-9-02 - Construção de estações e redes de distribuição de energia elétrica<br>
-- 9 = 68.22-6-00 - Gestão e administração da propriedade imobiliária<br>
-- 10 = 68.10-2-02 - Aluguel de imóveis próprios<br>
-- 11 = 42.92-8-02 - Obras de montagem industrial<br>
-- 12 = 71.19-7-03 - Serviços de desenho técnico relacionados à arquitetura e engenharia<br>
-- 13 = 43.30-4-04 - Serviços de pintura de edifícios em geral<br>
-- 14 = 42.22-7-01 - Construção de redes de abastecimento de água, coleta de esgoto e construções<br>
-- 15 = 42.99-5-01 - Construção de instalações esportivas e recreativas<br>
-- 16 = 23.30-3-01 - Fabricação de estruturas pré-moldadas de concreto armado, em série e sob encomenda<br>
-- 17 = 42.21-9-03 - Manutenção de redes de distribuição de energia elétrica<br>
-- 18 = 25.11-0-00 - Fabricação de estruturas metálicas<br>
-- 19 = 68.10-2-03 - Loteamento de imóveis próprios<br>
-- 20 = 43.13-4-00 - Obras de terraplenagem<br>
-- 21 = 68.10-2-01 - Compra e venda de imóveis próprios<br>
-- 22 = 43.21-5-00 - Instalação e manutenção elétrica<br>
-- 23 = 43.30-4-99 - Outras obras de acabamento da construção<br>
-- 24 = 71.11-1-00 - Serviços de Arquitetura<br>
-- 25 = 42.99-5-99 - Outras obras de engenharia civil não especificadas anteriormente<br>
-- 26 = 43.99-1-01 - Administração de obras<br>
-- 27 = 43.99-1-03 - Obras de alvenaria<br>
-- 28 = 42.11-1-01 - Construção de rodovias e ferrovias<br>
-- 29 = 71.12-0-00 - Serviços de engenharia<br>
-- 30 = 41.10-7-00 - Incorporação de empreendimentos imobiliários<br>
-- 31 = 41.20-4-00 - Construção de edifícios<br>
-- 999 = others<br>
16. Lead status (class attribute)<br>
-- 1 = the lead bought the system<br>
-- 0 = the lead did not buy system<br>

## Use Cases
Currently the application only proves the service to identify if the lead is qualified or not.

#### Lead status [/lead_status_by_id]
This service receive an id from the lead e returns the lead status.  
[0] - not qualified  
[1] - qualified  
To retrieval information about lead this application use a service from intellead-data (/lead-info).
After that it normalizes the data of the lead to play in the classification algorithm of the machine.
Finally, the lead status is persisted through the intellead-data service (/save-lead-status).
We can call the API like this:

```
request.get('https://your_domain.com/lead_status_by_id/'+lead_id);
```

## Copyrights and Licence
Project copyright and license is available at [LICENSE](./LICENSE).
