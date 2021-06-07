import graphene
import json


class Person(graphene.ObjectType):

    name = graphene.String()
    age = graphene.String()

#Modify this in order to take an object!

class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.String(required=True)

class CreatePerson(graphene.Mutation):
    class Arguments:
        #Replace previous code for name/age with object 
        person_data = PersonInput(required=True)

    person = graphene.Field(Person)

    #Whenever define mutation, need to "mutate"
    #Snake_case automatically gets converted to CamelCase for GraphQL, it is default

    def mutate(self, info, person_data):
        person = Person(name=person_data.name, age=person_data.age)
        ok = True
        return CreatePerson(person=person)

class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()

class Query(graphene.ObjectType):
    person = graphene.Field(Person)


schema = graphene.Schema(query=Query, mutation=MyMutation)
print(schema)

########QUERY THE ARRAY########

query_graphql = """
mutation myFirstMutation{
    createPerson (personData: {name: "Kiseey ka Dada", age: "77"}) {
        person {
            age
            name
        }
    }
}
"""

result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))


