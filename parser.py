from __future__ import print_function
import json


class Parser(object):

    def __init__(self, filename):
        self.properties = []
        self.brokers = []
        self.graphs = []
        with open(filename) as data:
            self.data = json.load(data)

    def parse(self):
        graph_counter = 1
        prop_counter = 1
        brok_counter = 1
        for prop in self.data['results']:
            broker = prop['broker']
            prop['broker'] = brok_counter
            stats = prop['stats']
            del prop['stats']
            for _, graph in stats.iteritems():              
                self.graphs.append({
                    "model": "properties.graph",
                    "pk": graph_counter,
                    "fields":{
                        "graph": graph,
                        "property": prop_counter
                    }
                })
                graph_counter+=1

            del broker["id"]
            self.brokers.append({
                "model": "properties.broker",
                "pk": brok_counter,
                "fields": broker
            })
            brok_counter+=1

            del prop['id']
            del prop['type_id']
            if not prop['openhousedate']:
                prop['openhousedate'] = None
            if not prop['openhouseduration']:
                prop['openhouseduration'] = None
            self.properties.append({
                "model": "properties.property",
                "pk": prop_counter,
                "fields": prop
            })
            prop_counter+=1

    def to_django_models(self):
        with open('fixtures/brokers.json', 'w') as br:
            json.dump(self.brokers, br)
        with open('fixtures/propertiestest.json', 'w') as pr:
            json.dump(self.properties[0:20], pr)
        with open('fixtures/properties.json', 'w') as pr:
            json.dump(self.properties, pr)
        with open('fixtures/graphs.json', 'w') as gr:
            json.dump(self.graphs, gr)

if __name__ == '__main__':
    a = Parser("search.json")
    a.parse()
    a.to_django_models()
        