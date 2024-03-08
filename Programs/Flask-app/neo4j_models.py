from py2neo import Graph, Node, Relationship

class Neo4jTool:
    graph = None

    def __init__(self):
        print("Initialize Neo4j tools...")

    def connect2neo4j(self):
        # Connect to Neo4j database
        self.graph = Graph("neo4j+s://d3a947d5.databases.neo4j.io", auth=("neo4j", "SC3NYzP1w2IG2JfYgFqgaDq-BfB66uVZ4j6bOEMx7ik"))

    def create_candidate(self, candidate_info):
        # Create a candidate node with candidate_info
        candidate_properties = {'Candidate ID': candidate_info["candidate_id"]}
        candidate = Node("Candidate", **candidate_properties)

        # Find or create related nodes (Country, State, City, Education, Experience)
        country_properties = {"Country": candidate_info["country"]}
        country  = list(self.graph.nodes.match("Country", **country_properties))
        if len(country):
            country = country[0]

        state_properties = {"Location": candidate_info["state"]}
        state  = list(self.graph.nodes.match("State", **state_properties))
        if len(state):
            state = state[0]

        city_properties = {"City": candidate_info["city"]}
        city  = list(self.graph.nodes.match("City", **city_properties))
        if len(city):
            city = city[0]

        education_properties = {"Major": candidate_info["education"]}
        education  = list(self.graph.nodes.match("Education", **education_properties))
        if len(education):
            education = education[0]        

        experience_properties = {"Experience": candidate_info["experience"]}
        experience  = list(self.graph.nodes.match("Experience", **experience_properties))
        if len(experience):
            experience = experience[0]   

        # Create relationships between candidate and related nodes
        candidate_country = Relationship(candidate, "SEEK_LOCATION_COUNTRY", country)
        candidate_state = Relationship(candidate, "SEEK_LOCATION_STATE", state)
        candidate_city = Relationship(candidate, "SEEK_LOCATION_CITY", city)
        candidate_education = Relationship(candidate, "HAS_EDUCATION", education)
        candidate_experience = Relationship(candidate, "HAS_EXPERIENCE", experience)

        # Create nodes and relationships in the graph
        self.graph.create(candidate)
        self.graph.create(country)
        self.graph.create(state)
        self.graph.create(city)
        self.graph.create(education)
        self.graph.create(experience)
        self.graph.create(candidate_country)
        self.graph.create(candidate_state)
        self.graph.create(candidate_city)
        self.graph.create(candidate_education)
        self.graph.create(candidate_experience)

        return candidate_info

    def create_job(self, job_info):
        # Create a job node with job_info
        job_properties = {'Job ID': job_info["job_id"]}
        job = Node("Job", **job_properties)

        # Find or create related nodes (Country, Education)
        country_properties = {"Country": job_info["country"]}
        country  = list(self.graph.nodes.match("Country", **country_properties))
        if len(country):
            country = country[0]

        education_properties = {"Major": job_info["education"]}
        education  = list(self.graph.nodes.match("Education", **education_properties))
        if len(education):
            education = education[0]        

        # Create relationships between job and related nodes
        candidate_country = Relationship(job, "SEEK_LOCATION_COUNTRY", country)
        candidate_education = Relationship(job, "HAS_EDUCATION", education)

        # Create nodes and relationships in the graph
        self.graph.create(job)
        self.graph.create(country)
        self.graph.create(education)
        self.graph.create(candidate_country)
        self.graph.create(candidate_education)

        return job_info

    def get_countries(self):
        # Get distinct countries from the graph
        sql = "MATCH (n) WHERE n.Country IS NOT NULL RETURN DISTINCT n.Country AS Country"
        choices = self.graph.run(sql)
        return [(choice['Country'], choice['Country']) for choice in choices]
    
    def get_states(self):
        # Get distinct states from the graph
        sql = "MATCH (n) WHERE n.State IS NOT NULL RETURN DISTINCT n.State AS State"
        choices = self.graph.run(sql)
        return [(choice['State'], choice['State']) for choice in choices]
    
    def get_cities(self):
        # Get distinct cities from the graph
        sql = "MATCH (n) WHERE n.Location IS NOT NULL RETURN DISTINCT n.Location AS City"
        choices = self.graph.run(sql)
        return [(choice['City'], choice['City']) for choice in choices]
    
    def get_education_choices(self):
        # Get distinct education choices from the graph
        sql = "MATCH (n) WHERE n.Major IS NOT NULL RETURN DISTINCT n.Major AS Education"
        choices = self.graph.run(sql)
        return [(choice['Education'], choice['Education']) for choice in choices]

    def get_skill_choices(self):
        # Get distinct skill choices from the graph
        sql = "MATCH (n) WHERE n.Skill IS NOT NULL RETURN DISTINCT n.Skill AS Skill"
        choices = self.graph.run(sql)
        return [(choice['Skill'], choice['Skill']) for choice in choices]
