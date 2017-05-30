import os
from SPARQLWrapper import SPARQLWrapper, JSON
from argparse import ArgumentParser


def get_languages():
    """
    Retrieve the language information.

    :return: The result of the query.
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    query = """
    PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>
    select ?code, ?label {
        ?language dbpedia-owl:iso6391Code ?code .
        ?language rdfs:label ?label .
        filter not exists { ?language rdf:type yago:Dialect107155661 }
    }
    """
    sparql.setQuery(query)

    return sparql.query().convert()


if __name__ == '__main__':
    parser = ArgumentParser(description='Store all DBPedia language information into a textfile.')
    parser.add_argument('outputfile', help='Path to the output file.')
    args = parser.parse_args()

    if len(os.path.dirname(args.outputfile)) > 0 and not os.path.exists(os.path.dirname(args.outputfile)):
        os.makedirs(os.path.dirname(args.outputfile))

    langs = get_languages()
    with open(args.outputfile, 'w') as output_file:
        for lang in langs['results']['bindings']:
            lang_code = lang['code']['value']
            label_lang = lang['label']['xml:lang']
            label_value = lang['label']['value']
            if '(' in label_value:
                label_value = label_value.split('(')[0].strip()
            if len(lang_code) == 2:
                output_file.write('%s\t%s\t%s\n' % (lang_code, label_lang, label_value))
