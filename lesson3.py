#import graphene
#import json

#Giving a list type to "database"
#Data = [

#    {
#        "name": "Ahad",
#        "age": "28"
#    },
#    {
#        "name": "Chunky Pandey",
#        "age": "58"
#    }
#]


#Schema to retrieve a list
#class Person(graphene.ObjectType):
#    name = graphene.String()
#    age = graphene.String()

#class Query(graphene.ObjectType):
#    array = graphene.List(Person)

 #   def resolve_array(root, info):
 #       return Data




#must resolve field after providing it!

#schema = graphene.Schema(query=Query)
#print(schema)

########QUERY THE ARRAY########

#query_graphql = """
#query myquery{
#    array{
#        BeautifulBlessingFromParents: name
#        BeautifulYearsOnEarth: age
#    }
#}
#"""


#result = schema.execute(query_graphql)
#print(json.dumps(result.data, indent=3))


