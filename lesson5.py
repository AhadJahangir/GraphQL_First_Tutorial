import graphene
import json




#Schema to retrieve a list, specifiy size of retrieval!
class Person(graphene.ObjectType):

    name = graphene.String()
    age = graphene.String()

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    ok = graphene.Boolean()
    person = graphene.Field(Person)

    #Whenever define mutation, need to "mutate"
    #Snake_case automatically gets converted to CamelCase for GraphQL, it is default

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)

class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()

class Query(graphene.ObjectType):
    person = graphene.Field(Person)


schema = graphene.Schema(query=Query, mutation=MyMutation)
print(schema)

########QUERY THE ARRAY########

query_graphql = """
mutation myFirstMutation{
    createPerson(name: "Kiseey Ka Mama") {
        person {
            name
        }
        ok
    }
}
"""

result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))


