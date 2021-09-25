#Client API with containing get, post put and delete

    List of all clients
### use this:
### http://127.0.0.1:8000/client/

GET /clients/

[

	{

    		'id' : 1,

    		'client_name' : 'Nimap',

    		'created_at' : '2019-12-24T11:03:55.931739+05:30',

   	 	'created_by' : 'Rohit'

	},

	{

    		'id' : 2,

    		'client_name' : 'Infotech',

   	 	'created_at' : '2019-12-24T11:03:55.931739+05:30',

    		'created_by' : 'Rohit'

	}

]

-------------------------------------------------------------

 

    Create a new client

##POST /clients/
## http://127.0.0.1:8000/client/
## add the details 

Input = {

	'client_name' : 'company A'

}

 

Output = {

	    	'id' : 3,

        		'client_name' : 'company A',

	    	'created_at' : '2019-12-24T11:03:55.931739+05:30',

	    	'created_by' : 'Rohit'

}

 

------------------------------------------------------------

### use this:
### http://127.0.0.1:8000/client/2/ 

    Retrieve info of a client along with projects assigned to its users

GET /clients/:id   	

 

{

        	'id' : 2,

	    	'client_name' : 'Infotech',

	    	'projects' : [

    	            		{

        	                                	'id' : 1,

        	                                	'name' : 'project A'

    	            		}

	    	]

	    	'created_at' : '2019-12-24T11:03:55.931739+05:30',

	    	'created_by' : 'Rohit'

	    	'updated_at' : '2019-12-24T11:03:55.931739+05:30',

}

 

------------------------------------------------------------
### use this:
### http://127.0.0.1:8000/client/2/ 
update
 

    Update info of a client

PUT-PATCH /clients/:id

 

Input = {

	                	'client_name' : 'company A'

}

 

Output = {

                    	 	'id' : 3,

	                	'client_name' : 'company A',

	                	'created_at' : '2019-12-24T11:03:55.931739+05:30',

	                	'created_by' : 'Rohit',

	                	'updated_at' : '2019-12-24T11:03:55.931739+05:30'

	}

 

------------------------------------------------------------
### use this:
### http://127.0.0.1:8000/client/2/ 
delete
 

    DELETE /clients/:id

 

The response status should be 204.

 

------------------------------------------------------------

 

    Create a new project

POST clients/:id/projects/

 

Here you do not need to create any new user but assign already registered users.

retrieve client id from the url and assign it to a project.

 

Input = {

	'project_name' : 'Project A'

	'users' : [

    		{

        			'id' : 1,

        			'name' : 'Rohit'

    		}

	]

}

 

Output = {

        	 	'id' : 3,

        		'project_name' : 'Project A',

	    	'client' : 'Nimap'

	    	'users' :         	[

    	            		{

        	                                	'id' : 1,

        	                                	'name' : 'Rohit'

    	            		}

	    	]

	    	'created_at' : '2019-12-24T11:03:55.931739+05:30'

	    	'created_by' : 'Ganesh'

}

 

-------------------------------------------------------------

 

 

    List of all projects assigned to the logged-in user

GET /projects/

[

	{

   	 	'id' : 1,

    		'project_name' : 'Project A',

   	 	'created_at' : '2019-12-24T11:03:55.931739+05:30',

   	 	'created_by' : 'Ganesh'

	},

	{