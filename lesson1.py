#import graphene
#import json

#"""
#{
#    name: "Ahad"
#    age" "28"
#}
#"""


#class Query(graphene.ObjectType):
#    name = graphene.String()
#    age = graphene.String()

 #   def resolve_name(root,info): 
  #      return "Ahad"
  #  def resolve_age(root,info):
   #     return "28"

#must resolve field after providing it!

#schema = graphene.Schema(query=Query)
#print(schema)

########QUERY TIME########

#query_graphql = """
#query myquery{
#   my_name: name
#    my_age: age
#}
#"""
#can use alias for extracted data anytime, no need to change on back end!
#must execute to obtain data 

#result = schema.execute(query_graphql)
#print(json.dumps(result.data, indent=3))
#printing schema shows what fields you can query

