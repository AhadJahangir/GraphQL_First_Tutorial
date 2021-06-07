import graphene
import json

#Giving a list type to "database"
DATA = [

    {
        "name": "Ahad",
        "age": "28"
    },
    {
        "name": "Chunky Pandey",
        "age": "58"
    }
]


#Schema to retrieve a list, specifiy size of retrieval!
class Person(graphene.ObjectType):

    name = graphene.String()
    age = graphene.String()

class Query(graphene.ObjectType):

    array = graphene.List(Person) #size= graphene.Int(default_value=1))

    def resolve_array(root, info):
        return DATA #[:size]


#Cannot get size functionality to work! This would query only one person from the array

#must resolve field after providing it!

schema = graphene.Schema(query=Query)
#print(schema)

########QUERY THE ARRAY########

query_graphql = """
query myquery{
    array 
    {
        age
        name
    }
}
"""
####SIZE QUERY BROKEN?###
#query_graphql = """
#query myquery{
#    array (size : 2)
#    {
#        age
#        name
#    }
#}
#""""
result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))


