import sys
#  公司电脑
sys.path.append("E:/Code/PublicationMS/app")
# sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from sparql_tools import imdb_sparql, dbpedia_sparql, sparql_runner

query_movie_dirBySofia = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?dir  m:director_name "Sofia Coppola".
}
"""

query_movie_by_movie = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
    ?film rdfs:label ' '.
    ?film m:director ?director.
    ?director m:made ?other_movie.
    ?other_movie m:label ?filmTitle.
    FILTER(?filmTitle!='') 
}
LIMIT 3
"""


# 通过字符串拼接传参数，需要加单引号
# def recommand_by_movie_name(name=""):
#     query = """
# PREFIX m: <http://data.linkedmdb.org/resource/movie/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# SELECT ?filmTitle WHERE {
#   ?film rdfs:label ?filmTitle.
#   ?film m:director ?dir.
#   ?dir  m:director_name '"""+name+"""'.
# } LIMIT 3
#     """
#     # print(query)
#     return sparql_runner(imdb_sparql, query)

def recommand_by_movie_name(name=""):
    query = """
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
        SELECT ?filmTitle WHERE {
            ?film rdfs:label '"""+name+"""'.
            ?film m:director ?director.
            ?director foaf:made ?other_movie.
            ?other_movie rdfs:label ?filmTitle.
            FILTER(?filmTitle != '"""+name+"""') 
        }
        LIMIT 3
    """
    print(query)
    return sparql_runner(imdb_sparql, query)