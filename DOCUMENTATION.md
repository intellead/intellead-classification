<h1>Welcome to Intellead Classification documentation!</h1>
Intellead Classification aims to be an easy way to identify the qualified lead for Intellead project.

<h3>Contents</h3>
<ul>
  <li>Introduction</li>
    <ul>
      <li>Features</li>
    </ul>
  <li>Instalation
    <ul>
      <li>Dependencies</li>
      <li>Get a copy</li>
    </ul>
  </li>
  <li>Configuration</li>
  <li>Dataset
    <ul>
        <li>Dataset information</li>
        <li>Attribute information</li>
    </ul>
  </li>
  <li>Use Cases
    <ul>
      <li>Lead status [/lead_status_by_id]</li>
    </ul>
  </li>
  <li>Copyrights and Licence</li>
</ul>
<h3>Introduction</h3>
Intellead Classification aims to be an easy way to identify the qualified lead for Intellead ecosystem.
<h4>Features</h4>
This application provides lead status.<br>
0 - Not qualified <br>
1 - Qualified
<h3>Instalation</h3>
intellead-classification is a very smaller component that provide a simple way to classify lead.
This way you do not need to install any other components for this to work.
<h4>Dependencies</h4>
Despite what has been said above, intellead-classification depends on intellead-data to retrieval information from lead and to store the identified lead status.
In addition, all libraries required by the service are described in requirements.txt document.
<h4>Get a copy</h4>
I like to encourage you to contribute to the repository.<br>
This should be as easy as possible for you but there are few things to consider when contributing. The following guidelines for contribution should be followed if you want to submit a pull request.
<ul>
  <li>You need a GitHub account</li>
  <li>Submit an issue ticket for your issue if there is no one yet.</li>
  <li>If you are able and want to fix this, fork the repository on GitHub</li>
  <li>Make commits of logical units and describe them properly.</li>
  <li>If possible, submit tests to your patch / new feature so it can be tested easily.</li>
  <li>Assure nothing is broken by running all the tests.</li>
  <li>Open a pull request to the original repository and choose the right original branch you want to patch.</li>
  <li>Even if you have write access to the repository, do not directly push or merge pull-requests. Let another team member review your pull request and approve.</li>
</ul>
<h3>Configuration</h3>
Once the application is installed (check Installation) define the following settings to enable the application behavior.
<h4>Config vars</h4>
The application uses a postgres database to store the dataset.<br>
For this it is necessary to configure the connection variables.<br>
You must config the following vars:<br>
DATABASE_URL - Full URL from database;<br>
DATABASE_HOST - Host from database;<br>
DATABASE_PORT - The port where database is connected;<br>
DATABASE_NAME - Database name;<br>
DATABASE_USER - User account to connect to the database;<br>
DATABASE_PASSWORD - Password to connect to the database.
<h3>Dataset</h3>
This dataset contains leads from construction industry.<br>
<h4>Dataset information</h4>
Data Set Characteristics: Multivariate<br>
Number of Instances: 595<br>
Attribute Characteristics: Integer<br>
Number of Attributes: 15<br>
Associated Tasks: Classification<br>
Missing Values?: No<br>
<h4>Attribute information</h4>
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
15. Lead status (class attribute)<br>
-- 1 = the lead bought the system<br>
-- 0 = the lead did not buy system<br>
<h3>Use Cases</h3>
Currently the application only proves the service to identify if the lead is qualified or not.
<h4>Lead status [/lead_status_by_id]</h4>
This service receive an id from the lead e returns the lead status.<br>
[0] - not qualified<br>
[1] - qualified<br>
To retrieval information about lead this application use a service from intellead-data (/lead-info).<br>
After that it normalizes the data of the lead to play in the classification algorithm of the machine.<br>
Finally, the lead status is persisted through the intellead-data service (/save-lead-status).<br>
We can call the API like this:

```javascript
request.get('https://your_domain.com/lead_status_by_id/'+lead_id);
```

<h3>Copyrights and Licence</h3>
TO DO
