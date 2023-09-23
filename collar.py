from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace



# Set the paths to your CSV file and the ontology file
csv_file = "collar.csv"  # Replace with the data source 
ontology_file = "foo.ttl" # Replace with the ontology

# Create an RDF graph
graph = Graph()

# Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

# Set the namespace for your ontology
namespace = Namespace("http://w3id.org/def/foo#")
namespace1 = Namespace("http://w3.org/ns/sosa/")
namespace2 = Namespace("http://w3.org/2003/01/geo/wgs84_pos#")

# RML mapping code
# Iterate over the CSV file and map the data to RDF triples
with open(csv_file, 'r') as file:
    # Skip the header row if present
    next(file)

    for line in file:
        # Split the CSV line into columns
        columns = line.strip().split(',')

        # Extract column values (modify as per your CSV structure)
        column1 = columns[0]
        column2 = columns[1]
        column3 = columns[2]
        column4 = columns[3]
        column5 = columns[4]
        column6 = columns[5]
        column7 = columns[6]
        column8 = columns[7]
        column9 = columns[8]
        column10 = columns[9]
        column11 = columns[10]
        column12 = columns[11]
        column13 = columns[12]
        column14 = columns[13]
        column15 = columns[14]
        

        # Create subject URI
        subject_uri = URIRef(namespace + column1)

        # Add triples to the graph
        graph.add((subject_uri, RDF.type, namespace1.Observation))  # Replace with the appropriate class from your ontology
        graph.add((subject_uri, namespace.LocalDate, Literal(column2)))  # Replace with the appropriate predicate from your ontology
        graph.add((subject_uri, namespace.LocalTime, Literal(column3)))
        graph.add((subject_uri, namespace.GMTDate, Literal(column4)))
        graph.add((subject_uri, namespace.GMTTime, Literal(column5)))
        graph.add((subject_uri, namespace2.lat, Literal(column6)))
        graph.add((subject_uri, namespace2.long Literal(column7)))
        graph.add((subject_uri, namespace2.Altitude, Literal(column8)))
        graph.add((subject_uri, namespace.Temperature, Literal(column9)))
        graph.add((subject_uri, namespace.Speed, Literal(column10)))
        graph.add((subject_uri, namespace.Direction, Literal(column11)))
        graph.add((subject_uri, namespace.Cov, Literal(column12)))
        graph.add((subject_uri, namespace.HDOP, Literal(column13)))
        graph.add((subject_uri, namespace.Distance, Literal(column14)))
        graph.add((subject_uri, namespace.Count, Literal(column15)))
      

# Save the resulting knowledge graph to a file
output_file = "CollarKG.rdf"
graph.serialize(destination=output_file, format="ttl")

