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
  <li>Configuration
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
<h3>Use Cases</h3>
Currently the application only proves the service to identify if the lead is qualified or not.
<h4>Lead status [/lead_status_by_id]</h4>
This service receive an id from the lead e returns the lead status.<br>
[0] - not qualified<br>
[1] - qualified<br>
To retrieval information about lead this application use a service from intellead-data (/lead-info).
After that it normalizes the data of the lead to play in the classification algorithm of the machine.
Finally, the lead status is persisted through the intellead-data service (/save-lead-status).
We can call the API like this:

```javascript
request.get('https://iyour_domain.com/lead_status_by_id/'+lead_id);
```

<h3>Copyrights and Licence</h3>
TO DO
