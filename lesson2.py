#import graphene
#import json

#"""
#{
#    name: "Ahad"
#    age" "28"
#}
#"""

#Passing Arguments with default argument
#class Query(graphene.ObjectType):
#    name = graphene.String(value=graphene.String(default_value="Susan"))
#    age = graphene.String(value=graphene.String(default_value="52"))
#
#    def resolve_name(root,info, value): 
#       return value
#    def resolve_age(root,info, value):
#        return value

#must resolve field after providing it!

#schema = graphene.Schema(query=Query)
#print(schema)

########QUERY TIME########

#query_graphql = """
#query myquery{
#    my_name: name (value: "Ahad")
#    my_age: age (value: "28")
#}
#"""
#can use alias for extracted data anytime, no need to change on back end!
#must execute to obtain data 

#result = schema.execute(query_graphql)
#print(json.dumps(result.data, indent=3))
#printing schema shows what fields you can query

